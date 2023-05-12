import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_order_model import GetOrderModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    goods_owner_id: int,
    order_number: Union[Unset, None, str] = UNSET,
    shipped_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    shipped_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    order_status_from: Union[Unset, None, int] = UNSET,
    order_status_to: Union[Unset, None, int] = UNSET,
    only_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    order_id_from: Union[Unset, None, int] = UNSET,
    max_orders_to_get: Union[Unset, None, int] = UNSET,
    order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_returned_from: Union[Unset, None, datetime.datetime] = UNSET,
    order_numbers: Union[Unset, None, List[str]] = UNSET,
    order_created_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_orders_with_order_lines_to_report_returned: Union[Unset, None, bool] = UNSET,
    only_if_transport_printed: Union[Unset, None, bool] = UNSET,
    shipment_id: Union[Unset, None, int] = UNSET,
    pickable: Union[Unset, None, str] = UNSET,
    parcel_number: Union[Unset, None, str] = UNSET,
    order_created_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    serial: Union[Unset, None, str] = UNSET,
    market_place: Union[Unset, None, str] = UNSET,
    order_updated_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    back_order_for_order_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/orders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["goodsOwnerId"] = goods_owner_id

    params["orderNumber"] = order_number

    json_shipped_time_from: Union[Unset, None, str] = UNSET
    if not isinstance(shipped_time_from, Unset):
        json_shipped_time_from = shipped_time_from.isoformat() if shipped_time_from else None

    params["shippedTimeFrom"] = json_shipped_time_from

    json_shipped_time_to: Union[Unset, None, str] = UNSET
    if not isinstance(shipped_time_to, Unset):
        json_shipped_time_to = shipped_time_to.isoformat() if shipped_time_to else None

    params["shippedTimeTo"] = json_shipped_time_to

    params["orderStatusFrom"] = order_status_from

    params["orderStatusTo"] = order_status_to

    params["onlyOrdersWithOrderLinesToReport"] = only_orders_with_order_lines_to_report

    params["orderIdFrom"] = order_id_from

    params["maxOrdersToGet"] = max_orders_to_get

    json_order_status_changed_time_from: Union[Unset, None, str] = UNSET
    if not isinstance(order_status_changed_time_from, Unset):
        json_order_status_changed_time_from = (
            order_status_changed_time_from.isoformat() if order_status_changed_time_from else None
        )

    params["orderStatusChangedTimeFrom"] = json_order_status_changed_time_from

    json_last_returned_from: Union[Unset, None, str] = UNSET
    if not isinstance(last_returned_from, Unset):
        json_last_returned_from = last_returned_from.isoformat() if last_returned_from else None

    params["lastReturnedFrom"] = json_last_returned_from

    json_order_numbers: Union[Unset, None, List[str]] = UNSET
    if not isinstance(order_numbers, Unset):
        if order_numbers is None:
            json_order_numbers = None
        else:
            json_order_numbers = order_numbers

    params["orderNumbers"] = json_order_numbers

    json_order_created_time_from: Union[Unset, None, str] = UNSET
    if not isinstance(order_created_time_from, Unset):
        json_order_created_time_from = order_created_time_from.isoformat() if order_created_time_from else None

    params["orderCreatedTimeFrom"] = json_order_created_time_from

    params["onlyOrdersWithOrderLinesToReportReturned"] = only_orders_with_order_lines_to_report_returned

    params["onlyIfTransportPrinted"] = only_if_transport_printed

    params["shipmentId"] = shipment_id

    params["pickable"] = pickable

    params["parcelNumber"] = parcel_number

    json_order_created_time_to: Union[Unset, None, str] = UNSET
    if not isinstance(order_created_time_to, Unset):
        json_order_created_time_to = order_created_time_to.isoformat() if order_created_time_to else None

    params["orderCreatedTimeTo"] = json_order_created_time_to

    json_article_numbers: Union[Unset, None, List[str]] = UNSET
    if not isinstance(article_numbers, Unset):
        if article_numbers is None:
            json_article_numbers = None
        else:
            json_article_numbers = article_numbers

    params["articleNumbers"] = json_article_numbers

    params["serial"] = serial

    params["marketPlace"] = market_place

    json_order_updated_time_from: Union[Unset, None, str] = UNSET
    if not isinstance(order_updated_time_from, Unset):
        json_order_updated_time_from = order_updated_time_from.isoformat() if order_updated_time_from else None

    params["orderUpdatedTimeFrom"] = json_order_updated_time_from

    params["backOrderForOrderId"] = back_order_for_order_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["GetOrderModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetOrderModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["GetOrderModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    goods_owner_id: int,
    order_number: Union[Unset, None, str] = UNSET,
    shipped_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    shipped_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    order_status_from: Union[Unset, None, int] = UNSET,
    order_status_to: Union[Unset, None, int] = UNSET,
    only_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    order_id_from: Union[Unset, None, int] = UNSET,
    max_orders_to_get: Union[Unset, None, int] = UNSET,
    order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_returned_from: Union[Unset, None, datetime.datetime] = UNSET,
    order_numbers: Union[Unset, None, List[str]] = UNSET,
    order_created_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_orders_with_order_lines_to_report_returned: Union[Unset, None, bool] = UNSET,
    only_if_transport_printed: Union[Unset, None, bool] = UNSET,
    shipment_id: Union[Unset, None, int] = UNSET,
    pickable: Union[Unset, None, str] = UNSET,
    parcel_number: Union[Unset, None, str] = UNSET,
    order_created_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    serial: Union[Unset, None, str] = UNSET,
    market_place: Union[Unset, None, str] = UNSET,
    order_updated_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    back_order_for_order_id: Union[Unset, None, int] = UNSET,
) -> Response[List["GetOrderModel"]]:
    """Get all orders which match the specified search criteria.

    Args:
        goods_owner_id (int):
        order_number (Union[Unset, None, str]):
        shipped_time_from (Union[Unset, None, datetime.datetime]):
        shipped_time_to (Union[Unset, None, datetime.datetime]):
        order_status_from (Union[Unset, None, int]):
        order_status_to (Union[Unset, None, int]):
        only_orders_with_order_lines_to_report (Union[Unset, None, bool]):
        order_id_from (Union[Unset, None, int]):
        max_orders_to_get (Union[Unset, None, int]):
        order_status_changed_time_from (Union[Unset, None, datetime.datetime]):
        last_returned_from (Union[Unset, None, datetime.datetime]):
        order_numbers (Union[Unset, None, List[str]]):
        order_created_time_from (Union[Unset, None, datetime.datetime]):
        only_orders_with_order_lines_to_report_returned (Union[Unset, None, bool]):
        only_if_transport_printed (Union[Unset, None, bool]):
        shipment_id (Union[Unset, None, int]):
        pickable (Union[Unset, None, str]):
        parcel_number (Union[Unset, None, str]):
        order_created_time_to (Union[Unset, None, datetime.datetime]):
        article_numbers (Union[Unset, None, List[str]]):
        serial (Union[Unset, None, str]):
        market_place (Union[Unset, None, str]):
        order_updated_time_from (Union[Unset, None, datetime.datetime]):
        back_order_for_order_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetOrderModel']]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        order_number=order_number,
        shipped_time_from=shipped_time_from,
        shipped_time_to=shipped_time_to,
        order_status_from=order_status_from,
        order_status_to=order_status_to,
        only_orders_with_order_lines_to_report=only_orders_with_order_lines_to_report,
        order_id_from=order_id_from,
        max_orders_to_get=max_orders_to_get,
        order_status_changed_time_from=order_status_changed_time_from,
        last_returned_from=last_returned_from,
        order_numbers=order_numbers,
        order_created_time_from=order_created_time_from,
        only_orders_with_order_lines_to_report_returned=only_orders_with_order_lines_to_report_returned,
        only_if_transport_printed=only_if_transport_printed,
        shipment_id=shipment_id,
        pickable=pickable,
        parcel_number=parcel_number,
        order_created_time_to=order_created_time_to,
        article_numbers=article_numbers,
        serial=serial,
        market_place=market_place,
        order_updated_time_from=order_updated_time_from,
        back_order_for_order_id=back_order_for_order_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    goods_owner_id: int,
    order_number: Union[Unset, None, str] = UNSET,
    shipped_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    shipped_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    order_status_from: Union[Unset, None, int] = UNSET,
    order_status_to: Union[Unset, None, int] = UNSET,
    only_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    order_id_from: Union[Unset, None, int] = UNSET,
    max_orders_to_get: Union[Unset, None, int] = UNSET,
    order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_returned_from: Union[Unset, None, datetime.datetime] = UNSET,
    order_numbers: Union[Unset, None, List[str]] = UNSET,
    order_created_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_orders_with_order_lines_to_report_returned: Union[Unset, None, bool] = UNSET,
    only_if_transport_printed: Union[Unset, None, bool] = UNSET,
    shipment_id: Union[Unset, None, int] = UNSET,
    pickable: Union[Unset, None, str] = UNSET,
    parcel_number: Union[Unset, None, str] = UNSET,
    order_created_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    serial: Union[Unset, None, str] = UNSET,
    market_place: Union[Unset, None, str] = UNSET,
    order_updated_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    back_order_for_order_id: Union[Unset, None, int] = UNSET,
) -> Optional[List["GetOrderModel"]]:
    """Get all orders which match the specified search criteria.

    Args:
        goods_owner_id (int):
        order_number (Union[Unset, None, str]):
        shipped_time_from (Union[Unset, None, datetime.datetime]):
        shipped_time_to (Union[Unset, None, datetime.datetime]):
        order_status_from (Union[Unset, None, int]):
        order_status_to (Union[Unset, None, int]):
        only_orders_with_order_lines_to_report (Union[Unset, None, bool]):
        order_id_from (Union[Unset, None, int]):
        max_orders_to_get (Union[Unset, None, int]):
        order_status_changed_time_from (Union[Unset, None, datetime.datetime]):
        last_returned_from (Union[Unset, None, datetime.datetime]):
        order_numbers (Union[Unset, None, List[str]]):
        order_created_time_from (Union[Unset, None, datetime.datetime]):
        only_orders_with_order_lines_to_report_returned (Union[Unset, None, bool]):
        only_if_transport_printed (Union[Unset, None, bool]):
        shipment_id (Union[Unset, None, int]):
        pickable (Union[Unset, None, str]):
        parcel_number (Union[Unset, None, str]):
        order_created_time_to (Union[Unset, None, datetime.datetime]):
        article_numbers (Union[Unset, None, List[str]]):
        serial (Union[Unset, None, str]):
        market_place (Union[Unset, None, str]):
        order_updated_time_from (Union[Unset, None, datetime.datetime]):
        back_order_for_order_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetOrderModel']
    """

    return sync_detailed(
        client=client,
        goods_owner_id=goods_owner_id,
        order_number=order_number,
        shipped_time_from=shipped_time_from,
        shipped_time_to=shipped_time_to,
        order_status_from=order_status_from,
        order_status_to=order_status_to,
        only_orders_with_order_lines_to_report=only_orders_with_order_lines_to_report,
        order_id_from=order_id_from,
        max_orders_to_get=max_orders_to_get,
        order_status_changed_time_from=order_status_changed_time_from,
        last_returned_from=last_returned_from,
        order_numbers=order_numbers,
        order_created_time_from=order_created_time_from,
        only_orders_with_order_lines_to_report_returned=only_orders_with_order_lines_to_report_returned,
        only_if_transport_printed=only_if_transport_printed,
        shipment_id=shipment_id,
        pickable=pickable,
        parcel_number=parcel_number,
        order_created_time_to=order_created_time_to,
        article_numbers=article_numbers,
        serial=serial,
        market_place=market_place,
        order_updated_time_from=order_updated_time_from,
        back_order_for_order_id=back_order_for_order_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    goods_owner_id: int,
    order_number: Union[Unset, None, str] = UNSET,
    shipped_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    shipped_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    order_status_from: Union[Unset, None, int] = UNSET,
    order_status_to: Union[Unset, None, int] = UNSET,
    only_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    order_id_from: Union[Unset, None, int] = UNSET,
    max_orders_to_get: Union[Unset, None, int] = UNSET,
    order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_returned_from: Union[Unset, None, datetime.datetime] = UNSET,
    order_numbers: Union[Unset, None, List[str]] = UNSET,
    order_created_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_orders_with_order_lines_to_report_returned: Union[Unset, None, bool] = UNSET,
    only_if_transport_printed: Union[Unset, None, bool] = UNSET,
    shipment_id: Union[Unset, None, int] = UNSET,
    pickable: Union[Unset, None, str] = UNSET,
    parcel_number: Union[Unset, None, str] = UNSET,
    order_created_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    serial: Union[Unset, None, str] = UNSET,
    market_place: Union[Unset, None, str] = UNSET,
    order_updated_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    back_order_for_order_id: Union[Unset, None, int] = UNSET,
) -> Response[List["GetOrderModel"]]:
    """Get all orders which match the specified search criteria.

    Args:
        goods_owner_id (int):
        order_number (Union[Unset, None, str]):
        shipped_time_from (Union[Unset, None, datetime.datetime]):
        shipped_time_to (Union[Unset, None, datetime.datetime]):
        order_status_from (Union[Unset, None, int]):
        order_status_to (Union[Unset, None, int]):
        only_orders_with_order_lines_to_report (Union[Unset, None, bool]):
        order_id_from (Union[Unset, None, int]):
        max_orders_to_get (Union[Unset, None, int]):
        order_status_changed_time_from (Union[Unset, None, datetime.datetime]):
        last_returned_from (Union[Unset, None, datetime.datetime]):
        order_numbers (Union[Unset, None, List[str]]):
        order_created_time_from (Union[Unset, None, datetime.datetime]):
        only_orders_with_order_lines_to_report_returned (Union[Unset, None, bool]):
        only_if_transport_printed (Union[Unset, None, bool]):
        shipment_id (Union[Unset, None, int]):
        pickable (Union[Unset, None, str]):
        parcel_number (Union[Unset, None, str]):
        order_created_time_to (Union[Unset, None, datetime.datetime]):
        article_numbers (Union[Unset, None, List[str]]):
        serial (Union[Unset, None, str]):
        market_place (Union[Unset, None, str]):
        order_updated_time_from (Union[Unset, None, datetime.datetime]):
        back_order_for_order_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetOrderModel']]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        order_number=order_number,
        shipped_time_from=shipped_time_from,
        shipped_time_to=shipped_time_to,
        order_status_from=order_status_from,
        order_status_to=order_status_to,
        only_orders_with_order_lines_to_report=only_orders_with_order_lines_to_report,
        order_id_from=order_id_from,
        max_orders_to_get=max_orders_to_get,
        order_status_changed_time_from=order_status_changed_time_from,
        last_returned_from=last_returned_from,
        order_numbers=order_numbers,
        order_created_time_from=order_created_time_from,
        only_orders_with_order_lines_to_report_returned=only_orders_with_order_lines_to_report_returned,
        only_if_transport_printed=only_if_transport_printed,
        shipment_id=shipment_id,
        pickable=pickable,
        parcel_number=parcel_number,
        order_created_time_to=order_created_time_to,
        article_numbers=article_numbers,
        serial=serial,
        market_place=market_place,
        order_updated_time_from=order_updated_time_from,
        back_order_for_order_id=back_order_for_order_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    goods_owner_id: int,
    order_number: Union[Unset, None, str] = UNSET,
    shipped_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    shipped_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    order_status_from: Union[Unset, None, int] = UNSET,
    order_status_to: Union[Unset, None, int] = UNSET,
    only_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    order_id_from: Union[Unset, None, int] = UNSET,
    max_orders_to_get: Union[Unset, None, int] = UNSET,
    order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_returned_from: Union[Unset, None, datetime.datetime] = UNSET,
    order_numbers: Union[Unset, None, List[str]] = UNSET,
    order_created_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_orders_with_order_lines_to_report_returned: Union[Unset, None, bool] = UNSET,
    only_if_transport_printed: Union[Unset, None, bool] = UNSET,
    shipment_id: Union[Unset, None, int] = UNSET,
    pickable: Union[Unset, None, str] = UNSET,
    parcel_number: Union[Unset, None, str] = UNSET,
    order_created_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    serial: Union[Unset, None, str] = UNSET,
    market_place: Union[Unset, None, str] = UNSET,
    order_updated_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    back_order_for_order_id: Union[Unset, None, int] = UNSET,
) -> Optional[List["GetOrderModel"]]:
    """Get all orders which match the specified search criteria.

    Args:
        goods_owner_id (int):
        order_number (Union[Unset, None, str]):
        shipped_time_from (Union[Unset, None, datetime.datetime]):
        shipped_time_to (Union[Unset, None, datetime.datetime]):
        order_status_from (Union[Unset, None, int]):
        order_status_to (Union[Unset, None, int]):
        only_orders_with_order_lines_to_report (Union[Unset, None, bool]):
        order_id_from (Union[Unset, None, int]):
        max_orders_to_get (Union[Unset, None, int]):
        order_status_changed_time_from (Union[Unset, None, datetime.datetime]):
        last_returned_from (Union[Unset, None, datetime.datetime]):
        order_numbers (Union[Unset, None, List[str]]):
        order_created_time_from (Union[Unset, None, datetime.datetime]):
        only_orders_with_order_lines_to_report_returned (Union[Unset, None, bool]):
        only_if_transport_printed (Union[Unset, None, bool]):
        shipment_id (Union[Unset, None, int]):
        pickable (Union[Unset, None, str]):
        parcel_number (Union[Unset, None, str]):
        order_created_time_to (Union[Unset, None, datetime.datetime]):
        article_numbers (Union[Unset, None, List[str]]):
        serial (Union[Unset, None, str]):
        market_place (Union[Unset, None, str]):
        order_updated_time_from (Union[Unset, None, datetime.datetime]):
        back_order_for_order_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetOrderModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            goods_owner_id=goods_owner_id,
            order_number=order_number,
            shipped_time_from=shipped_time_from,
            shipped_time_to=shipped_time_to,
            order_status_from=order_status_from,
            order_status_to=order_status_to,
            only_orders_with_order_lines_to_report=only_orders_with_order_lines_to_report,
            order_id_from=order_id_from,
            max_orders_to_get=max_orders_to_get,
            order_status_changed_time_from=order_status_changed_time_from,
            last_returned_from=last_returned_from,
            order_numbers=order_numbers,
            order_created_time_from=order_created_time_from,
            only_orders_with_order_lines_to_report_returned=only_orders_with_order_lines_to_report_returned,
            only_if_transport_printed=only_if_transport_printed,
            shipment_id=shipment_id,
            pickable=pickable,
            parcel_number=parcel_number,
            order_created_time_to=order_created_time_to,
            article_numbers=article_numbers,
            serial=serial,
            market_place=market_place,
            order_updated_time_from=order_updated_time_from,
            back_order_for_order_id=back_order_for_order_id,
        )
    ).parsed
