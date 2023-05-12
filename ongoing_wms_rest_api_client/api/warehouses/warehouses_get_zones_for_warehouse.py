from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.zone_model import ZoneModel
from ...types import Response


def _get_kwargs(
    warehouse_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/warehouses/{warehouseId}/zones".format(client.base_url, warehouseId=warehouse_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Optional[List["ZoneModel"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200 or []:
            response_200_item = ZoneModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Optional[List["ZoneModel"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    warehouse_id: int,
    *,
    client: Client,
) -> Response[Optional[List["ZoneModel"]]]:
    """Get all zones (including aisles and locations) for a particular warehouse.

    Args:
        warehouse_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Optional[List['ZoneModel']]]
    """

    kwargs = _get_kwargs(
        warehouse_id=warehouse_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    warehouse_id: int,
    *,
    client: Client,
) -> Optional[Optional[List["ZoneModel"]]]:
    """Get all zones (including aisles and locations) for a particular warehouse.

    Args:
        warehouse_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[List['ZoneModel']]
    """

    return sync_detailed(
        warehouse_id=warehouse_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    warehouse_id: int,
    *,
    client: Client,
) -> Response[Optional[List["ZoneModel"]]]:
    """Get all zones (including aisles and locations) for a particular warehouse.

    Args:
        warehouse_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Optional[List['ZoneModel']]]
    """

    kwargs = _get_kwargs(
        warehouse_id=warehouse_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    warehouse_id: int,
    *,
    client: Client,
) -> Optional[Optional[List["ZoneModel"]]]:
    """Get all zones (including aisles and locations) for a particular warehouse.

    Args:
        warehouse_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[List['ZoneModel']]
    """

    return (
        await asyncio_detailed(
            warehouse_id=warehouse_id,
            client=client,
        )
    ).parsed
