from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.post_purchase_order_response import PostPurchaseOrderResponse
from ...types import Response


def _get_kwargs(
    purchase_order_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/purchaseOrders/{purchaseOrderId}".format(client.base_url, purchaseOrderId=purchase_order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostPurchaseOrderResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostPurchaseOrderResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostPurchaseOrderResponse]:
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
) -> Response[PostPurchaseOrderResponse]:
    """Cancel a purchase order.

    Args:
        purchase_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPurchaseOrderResponse]
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
) -> Optional[PostPurchaseOrderResponse]:
    """Cancel a purchase order.

    Args:
        purchase_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPurchaseOrderResponse
    """

    return sync_detailed(
        purchase_order_id=purchase_order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    purchase_order_id: int,
    *,
    client: Client,
) -> Response[PostPurchaseOrderResponse]:
    """Cancel a purchase order.

    Args:
        purchase_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPurchaseOrderResponse]
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
) -> Optional[PostPurchaseOrderResponse]:
    """Cancel a purchase order.

    Args:
        purchase_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPurchaseOrderResponse
    """

    return (
        await asyncio_detailed(
            purchase_order_id=purchase_order_id,
            client=client,
        )
    ).parsed
