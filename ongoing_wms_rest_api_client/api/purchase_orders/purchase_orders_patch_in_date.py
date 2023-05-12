from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patch_purchase_order_in_date import PatchPurchaseOrderInDate
from ...models.patch_purchase_order_response import PatchPurchaseOrderResponse
from ...types import Response


def _get_kwargs(
    purchase_order_id: int,
    *,
    client: Client,
    json_body: PatchPurchaseOrderInDate,
) -> Dict[str, Any]:
    url = "{}/api/v1/purchaseOrders/{purchaseOrderId}/inDate".format(client.base_url, purchaseOrderId=purchase_order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PatchPurchaseOrderResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PatchPurchaseOrderResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PatchPurchaseOrderResponse]:
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
    json_body: PatchPurchaseOrderInDate,
) -> Response[PatchPurchaseOrderResponse]:
    """Update the indate on purchase order.

    Args:
        purchase_order_id (int):
        json_body (PatchPurchaseOrderInDate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchPurchaseOrderResponse]
    """

    kwargs = _get_kwargs(
        purchase_order_id=purchase_order_id,
        client=client,
        json_body=json_body,
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
    json_body: PatchPurchaseOrderInDate,
) -> Optional[PatchPurchaseOrderResponse]:
    """Update the indate on purchase order.

    Args:
        purchase_order_id (int):
        json_body (PatchPurchaseOrderInDate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchPurchaseOrderResponse
    """

    return sync_detailed(
        purchase_order_id=purchase_order_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    purchase_order_id: int,
    *,
    client: Client,
    json_body: PatchPurchaseOrderInDate,
) -> Response[PatchPurchaseOrderResponse]:
    """Update the indate on purchase order.

    Args:
        purchase_order_id (int):
        json_body (PatchPurchaseOrderInDate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchPurchaseOrderResponse]
    """

    kwargs = _get_kwargs(
        purchase_order_id=purchase_order_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    purchase_order_id: int,
    *,
    client: Client,
    json_body: PatchPurchaseOrderInDate,
) -> Optional[PatchPurchaseOrderResponse]:
    """Update the indate on purchase order.

    Args:
        purchase_order_id (int):
        json_body (PatchPurchaseOrderInDate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchPurchaseOrderResponse
    """

    return (
        await asyncio_detailed(
            purchase_order_id=purchase_order_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
