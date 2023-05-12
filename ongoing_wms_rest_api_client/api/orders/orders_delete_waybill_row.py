from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.post_parcel_response import PostParcelResponse
from ...types import Response


def _get_kwargs(
    order_id: int,
    way_bill_row_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/orders/{orderId}/wayBillRows/{wayBillRowId}".format(
        client.base_url, orderId=order_id, wayBillRowId=way_bill_row_id
    )

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostParcelResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostParcelResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostParcelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: int,
    way_bill_row_id: int,
    *,
    client: Client,
) -> Response[PostParcelResponse]:
    """Deletes a waybill row.

    Args:
        order_id (int):
        way_bill_row_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostParcelResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        way_bill_row_id=way_bill_row_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: int,
    way_bill_row_id: int,
    *,
    client: Client,
) -> Optional[PostParcelResponse]:
    """Deletes a waybill row.

    Args:
        order_id (int):
        way_bill_row_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostParcelResponse
    """

    return sync_detailed(
        order_id=order_id,
        way_bill_row_id=way_bill_row_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_id: int,
    way_bill_row_id: int,
    *,
    client: Client,
) -> Response[PostParcelResponse]:
    """Deletes a waybill row.

    Args:
        order_id (int):
        way_bill_row_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostParcelResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        way_bill_row_id=way_bill_row_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: int,
    way_bill_row_id: int,
    *,
    client: Client,
) -> Optional[PostParcelResponse]:
    """Deletes a waybill row.

    Args:
        order_id (int):
        way_bill_row_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostParcelResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            way_bill_row_id=way_bill_row_id,
            client=client,
        )
    ).parsed
