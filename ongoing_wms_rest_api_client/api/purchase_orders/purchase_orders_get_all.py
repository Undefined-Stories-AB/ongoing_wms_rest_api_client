import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_purchase_order_model import GetPurchaseOrderModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    goods_owner_id: int,
    purchase_order_number: Union[Unset, None, str] = UNSET,
    last_receive_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_receive_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_status_from: Union[Unset, None, int] = UNSET,
    purchase_order_status_to: Union[Unset, None, int] = UNSET,
    only_purchase_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    purchase_order_id_from: Union[Unset, None, int] = UNSET,
    max_purchase_orders_to_get: Union[Unset, None, int] = UNSET,
    purchase_order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_numbers: Union[Unset, None, List[str]] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    in_date_from: Union[Unset, None, datetime.datetime] = UNSET,
    in_date_to: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/purchaseOrders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["goodsOwnerId"] = goods_owner_id

    params["purchaseOrderNumber"] = purchase_order_number

    json_last_receive_time_from: Union[Unset, None, str] = UNSET
    if not isinstance(last_receive_time_from, Unset):
        json_last_receive_time_from = last_receive_time_from.isoformat() if last_receive_time_from else None

    params["lastReceiveTimeFrom"] = json_last_receive_time_from

    json_last_receive_time_to: Union[Unset, None, str] = UNSET
    if not isinstance(last_receive_time_to, Unset):
        json_last_receive_time_to = last_receive_time_to.isoformat() if last_receive_time_to else None

    params["lastReceiveTimeTo"] = json_last_receive_time_to

    params["purchaseOrderStatusFrom"] = purchase_order_status_from

    params["purchaseOrderStatusTo"] = purchase_order_status_to

    params["onlyPurchaseOrdersWithOrderLinesToReport"] = only_purchase_orders_with_order_lines_to_report

    params["purchaseOrderIdFrom"] = purchase_order_id_from

    params["maxPurchaseOrdersToGet"] = max_purchase_orders_to_get

    json_purchase_order_status_changed_time_from: Union[Unset, None, str] = UNSET
    if not isinstance(purchase_order_status_changed_time_from, Unset):
        json_purchase_order_status_changed_time_from = (
            purchase_order_status_changed_time_from.isoformat() if purchase_order_status_changed_time_from else None
        )

    params["purchaseOrderStatusChangedTimeFrom"] = json_purchase_order_status_changed_time_from

    json_purchase_order_numbers: Union[Unset, None, List[str]] = UNSET
    if not isinstance(purchase_order_numbers, Unset):
        if purchase_order_numbers is None:
            json_purchase_order_numbers = None
        else:
            json_purchase_order_numbers = purchase_order_numbers

    params["purchaseOrderNumbers"] = json_purchase_order_numbers

    json_article_numbers: Union[Unset, None, List[str]] = UNSET
    if not isinstance(article_numbers, Unset):
        if article_numbers is None:
            json_article_numbers = None
        else:
            json_article_numbers = article_numbers

    params["articleNumbers"] = json_article_numbers

    json_in_date_from: Union[Unset, None, str] = UNSET
    if not isinstance(in_date_from, Unset):
        json_in_date_from = in_date_from.isoformat() if in_date_from else None

    params["inDateFrom"] = json_in_date_from

    json_in_date_to: Union[Unset, None, str] = UNSET
    if not isinstance(in_date_to, Unset):
        json_in_date_to = in_date_to.isoformat() if in_date_to else None

    params["inDateTo"] = json_in_date_to

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Optional[List["GetPurchaseOrderModel"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200 or []:
            response_200_item = GetPurchaseOrderModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Optional[List["GetPurchaseOrderModel"]]]:
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
    purchase_order_number: Union[Unset, None, str] = UNSET,
    last_receive_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_receive_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_status_from: Union[Unset, None, int] = UNSET,
    purchase_order_status_to: Union[Unset, None, int] = UNSET,
    only_purchase_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    purchase_order_id_from: Union[Unset, None, int] = UNSET,
    max_purchase_orders_to_get: Union[Unset, None, int] = UNSET,
    purchase_order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_numbers: Union[Unset, None, List[str]] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    in_date_from: Union[Unset, None, datetime.datetime] = UNSET,
    in_date_to: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Optional[List["GetPurchaseOrderModel"]]]:
    """Get all purchase orders which match the specified search criteria.

    Args:
        goods_owner_id (int):
        purchase_order_number (Union[Unset, None, str]):
        last_receive_time_from (Union[Unset, None, datetime.datetime]):
        last_receive_time_to (Union[Unset, None, datetime.datetime]):
        purchase_order_status_from (Union[Unset, None, int]):
        purchase_order_status_to (Union[Unset, None, int]):
        only_purchase_orders_with_order_lines_to_report (Union[Unset, None, bool]):
        purchase_order_id_from (Union[Unset, None, int]):
        max_purchase_orders_to_get (Union[Unset, None, int]):
        purchase_order_status_changed_time_from (Union[Unset, None, datetime.datetime]):
        purchase_order_numbers (Union[Unset, None, List[str]]):
        article_numbers (Union[Unset, None, List[str]]):
        in_date_from (Union[Unset, None, datetime.datetime]):
        in_date_to (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Optional[List['GetPurchaseOrderModel']]]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        purchase_order_number=purchase_order_number,
        last_receive_time_from=last_receive_time_from,
        last_receive_time_to=last_receive_time_to,
        purchase_order_status_from=purchase_order_status_from,
        purchase_order_status_to=purchase_order_status_to,
        only_purchase_orders_with_order_lines_to_report=only_purchase_orders_with_order_lines_to_report,
        purchase_order_id_from=purchase_order_id_from,
        max_purchase_orders_to_get=max_purchase_orders_to_get,
        purchase_order_status_changed_time_from=purchase_order_status_changed_time_from,
        purchase_order_numbers=purchase_order_numbers,
        article_numbers=article_numbers,
        in_date_from=in_date_from,
        in_date_to=in_date_to,
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
    purchase_order_number: Union[Unset, None, str] = UNSET,
    last_receive_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_receive_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_status_from: Union[Unset, None, int] = UNSET,
    purchase_order_status_to: Union[Unset, None, int] = UNSET,
    only_purchase_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    purchase_order_id_from: Union[Unset, None, int] = UNSET,
    max_purchase_orders_to_get: Union[Unset, None, int] = UNSET,
    purchase_order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_numbers: Union[Unset, None, List[str]] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    in_date_from: Union[Unset, None, datetime.datetime] = UNSET,
    in_date_to: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Optional[List["GetPurchaseOrderModel"]]]:
    """Get all purchase orders which match the specified search criteria.

    Args:
        goods_owner_id (int):
        purchase_order_number (Union[Unset, None, str]):
        last_receive_time_from (Union[Unset, None, datetime.datetime]):
        last_receive_time_to (Union[Unset, None, datetime.datetime]):
        purchase_order_status_from (Union[Unset, None, int]):
        purchase_order_status_to (Union[Unset, None, int]):
        only_purchase_orders_with_order_lines_to_report (Union[Unset, None, bool]):
        purchase_order_id_from (Union[Unset, None, int]):
        max_purchase_orders_to_get (Union[Unset, None, int]):
        purchase_order_status_changed_time_from (Union[Unset, None, datetime.datetime]):
        purchase_order_numbers (Union[Unset, None, List[str]]):
        article_numbers (Union[Unset, None, List[str]]):
        in_date_from (Union[Unset, None, datetime.datetime]):
        in_date_to (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[List['GetPurchaseOrderModel']]
    """

    return sync_detailed(
        client=client,
        goods_owner_id=goods_owner_id,
        purchase_order_number=purchase_order_number,
        last_receive_time_from=last_receive_time_from,
        last_receive_time_to=last_receive_time_to,
        purchase_order_status_from=purchase_order_status_from,
        purchase_order_status_to=purchase_order_status_to,
        only_purchase_orders_with_order_lines_to_report=only_purchase_orders_with_order_lines_to_report,
        purchase_order_id_from=purchase_order_id_from,
        max_purchase_orders_to_get=max_purchase_orders_to_get,
        purchase_order_status_changed_time_from=purchase_order_status_changed_time_from,
        purchase_order_numbers=purchase_order_numbers,
        article_numbers=article_numbers,
        in_date_from=in_date_from,
        in_date_to=in_date_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    goods_owner_id: int,
    purchase_order_number: Union[Unset, None, str] = UNSET,
    last_receive_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_receive_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_status_from: Union[Unset, None, int] = UNSET,
    purchase_order_status_to: Union[Unset, None, int] = UNSET,
    only_purchase_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    purchase_order_id_from: Union[Unset, None, int] = UNSET,
    max_purchase_orders_to_get: Union[Unset, None, int] = UNSET,
    purchase_order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_numbers: Union[Unset, None, List[str]] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    in_date_from: Union[Unset, None, datetime.datetime] = UNSET,
    in_date_to: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Optional[List["GetPurchaseOrderModel"]]]:
    """Get all purchase orders which match the specified search criteria.

    Args:
        goods_owner_id (int):
        purchase_order_number (Union[Unset, None, str]):
        last_receive_time_from (Union[Unset, None, datetime.datetime]):
        last_receive_time_to (Union[Unset, None, datetime.datetime]):
        purchase_order_status_from (Union[Unset, None, int]):
        purchase_order_status_to (Union[Unset, None, int]):
        only_purchase_orders_with_order_lines_to_report (Union[Unset, None, bool]):
        purchase_order_id_from (Union[Unset, None, int]):
        max_purchase_orders_to_get (Union[Unset, None, int]):
        purchase_order_status_changed_time_from (Union[Unset, None, datetime.datetime]):
        purchase_order_numbers (Union[Unset, None, List[str]]):
        article_numbers (Union[Unset, None, List[str]]):
        in_date_from (Union[Unset, None, datetime.datetime]):
        in_date_to (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Optional[List['GetPurchaseOrderModel']]]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        purchase_order_number=purchase_order_number,
        last_receive_time_from=last_receive_time_from,
        last_receive_time_to=last_receive_time_to,
        purchase_order_status_from=purchase_order_status_from,
        purchase_order_status_to=purchase_order_status_to,
        only_purchase_orders_with_order_lines_to_report=only_purchase_orders_with_order_lines_to_report,
        purchase_order_id_from=purchase_order_id_from,
        max_purchase_orders_to_get=max_purchase_orders_to_get,
        purchase_order_status_changed_time_from=purchase_order_status_changed_time_from,
        purchase_order_numbers=purchase_order_numbers,
        article_numbers=article_numbers,
        in_date_from=in_date_from,
        in_date_to=in_date_to,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    goods_owner_id: int,
    purchase_order_number: Union[Unset, None, str] = UNSET,
    last_receive_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    last_receive_time_to: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_status_from: Union[Unset, None, int] = UNSET,
    purchase_order_status_to: Union[Unset, None, int] = UNSET,
    only_purchase_orders_with_order_lines_to_report: Union[Unset, None, bool] = UNSET,
    purchase_order_id_from: Union[Unset, None, int] = UNSET,
    max_purchase_orders_to_get: Union[Unset, None, int] = UNSET,
    purchase_order_status_changed_time_from: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_numbers: Union[Unset, None, List[str]] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    in_date_from: Union[Unset, None, datetime.datetime] = UNSET,
    in_date_to: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Optional[List["GetPurchaseOrderModel"]]]:
    """Get all purchase orders which match the specified search criteria.

    Args:
        goods_owner_id (int):
        purchase_order_number (Union[Unset, None, str]):
        last_receive_time_from (Union[Unset, None, datetime.datetime]):
        last_receive_time_to (Union[Unset, None, datetime.datetime]):
        purchase_order_status_from (Union[Unset, None, int]):
        purchase_order_status_to (Union[Unset, None, int]):
        only_purchase_orders_with_order_lines_to_report (Union[Unset, None, bool]):
        purchase_order_id_from (Union[Unset, None, int]):
        max_purchase_orders_to_get (Union[Unset, None, int]):
        purchase_order_status_changed_time_from (Union[Unset, None, datetime.datetime]):
        purchase_order_numbers (Union[Unset, None, List[str]]):
        article_numbers (Union[Unset, None, List[str]]):
        in_date_from (Union[Unset, None, datetime.datetime]):
        in_date_to (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[List['GetPurchaseOrderModel']]
    """

    return (
        await asyncio_detailed(
            client=client,
            goods_owner_id=goods_owner_id,
            purchase_order_number=purchase_order_number,
            last_receive_time_from=last_receive_time_from,
            last_receive_time_to=last_receive_time_to,
            purchase_order_status_from=purchase_order_status_from,
            purchase_order_status_to=purchase_order_status_to,
            only_purchase_orders_with_order_lines_to_report=only_purchase_orders_with_order_lines_to_report,
            purchase_order_id_from=purchase_order_id_from,
            max_purchase_orders_to_get=max_purchase_orders_to_get,
            purchase_order_status_changed_time_from=purchase_order_status_changed_time_from,
            purchase_order_numbers=purchase_order_numbers,
            article_numbers=article_numbers,
            in_date_from=in_date_from,
            in_date_to=in_date_to,
        )
    ).parsed
