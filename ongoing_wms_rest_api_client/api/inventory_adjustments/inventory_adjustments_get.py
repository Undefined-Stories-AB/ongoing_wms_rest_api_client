from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_inventory_adjustments_line import GetInventoryAdjustmentsLine
from ...types import Response


def _get_kwargs(
    inventory_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/inventoryAdjustments/{inventoryId}".format(client.base_url, inventoryId=inventory_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetInventoryAdjustmentsLine]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetInventoryAdjustmentsLine.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetInventoryAdjustmentsLine]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inventory_id: int,
    *,
    client: Client,
) -> Response[GetInventoryAdjustmentsLine]:
    """Get a specific inventory adjustment.

    Args:
        inventory_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInventoryAdjustmentsLine]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    inventory_id: int,
    *,
    client: Client,
) -> Optional[GetInventoryAdjustmentsLine]:
    """Get a specific inventory adjustment.

    Args:
        inventory_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInventoryAdjustmentsLine
    """

    return sync_detailed(
        inventory_id=inventory_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    inventory_id: int,
    *,
    client: Client,
) -> Response[GetInventoryAdjustmentsLine]:
    """Get a specific inventory adjustment.

    Args:
        inventory_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInventoryAdjustmentsLine]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    inventory_id: int,
    *,
    client: Client,
) -> Optional[GetInventoryAdjustmentsLine]:
    """Get a specific inventory adjustment.

    Args:
        inventory_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInventoryAdjustmentsLine
    """

    return (
        await asyncio_detailed(
            inventory_id=inventory_id,
            client=client,
        )
    ).parsed
