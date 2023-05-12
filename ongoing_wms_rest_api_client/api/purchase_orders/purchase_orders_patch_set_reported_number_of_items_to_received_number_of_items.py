from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...types import File, Response


def _get_kwargs(
    purchase_order_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/purchaseOrders/{purchaseOrderId}/setReportedNumberOfItemsToReceivedNumberOfItems".format(
        client.base_url, purchaseOrderId=purchase_order_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[File]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    purchase_order_id: int,
    *,
    client: Client,
) -> Response[File]:
    """Sets the reported number of items on each purchase order line to the received number of items.

    Args:
        purchase_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        purchase_order_id=purchase_order_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    purchase_order_id: int,
    *,
    client: Client,
) -> Optional[File]:
    """Sets the reported number of items on each purchase order line to the received number of items.

    Args:
        purchase_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        purchase_order_id=purchase_order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    purchase_order_id: int,
    *,
    client: Client,
) -> Response[File]:
    """Sets the reported number of items on each purchase order line to the received number of items.

    Args:
        purchase_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        purchase_order_id=purchase_order_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    purchase_order_id: int,
    *,
    client: Client,
) -> Optional[File]:
    """Sets the reported number of items on each purchase order line to the received number of items.

    Args:
        purchase_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            purchase_order_id=purchase_order_id,
            client=client,
        )
    ).parsed
