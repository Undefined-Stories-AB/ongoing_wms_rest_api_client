import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_article_model import GetArticleModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    goods_owner_id: int,
    article_number: Union[Unset, None, str] = UNSET,
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    article_data_last_updated_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    product_code: Union[Unset, None, str] = UNSET,
    product_codes: Union[Unset, None, List[str]] = UNSET,
    article_name_contains: Union[Unset, None, List[str]] = UNSET,
    article_class_ids: Union[Unset, None, List[int]] = UNSET,
    bar_codes: Union[Unset, None, List[str]] = UNSET,
    only_articles_below_stock_limit: Union[Unset, None, bool] = UNSET,
    only_articles_below_stock_limit_considering_number_of_booked_items: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/articles".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["goodsOwnerId"] = goods_owner_id

    params["articleNumber"] = article_number

    params["articleSystemIdFrom"] = article_system_id_from

    params["maxArticlesToGet"] = max_articles_to_get

    json_stock_info_changed_from: Union[Unset, None, str] = UNSET
    if not isinstance(stock_info_changed_from, Unset):
        json_stock_info_changed_from = stock_info_changed_from.isoformat() if stock_info_changed_from else None

    params["stockInfoChangedFrom"] = json_stock_info_changed_from

    json_article_numbers: Union[Unset, None, List[str]] = UNSET
    if not isinstance(article_numbers, Unset):
        if article_numbers is None:
            json_article_numbers = None
        else:
            json_article_numbers = article_numbers

    params["articleNumbers"] = json_article_numbers

    json_article_data_last_updated_from: Union[Unset, None, str] = UNSET
    if not isinstance(article_data_last_updated_from, Unset):
        json_article_data_last_updated_from = (
            article_data_last_updated_from.isoformat() if article_data_last_updated_from else None
        )

    params["articleDataLastUpdatedFrom"] = json_article_data_last_updated_from

    params["onlyArticlesInStock"] = only_articles_in_stock

    params["productCode"] = product_code

    json_product_codes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(product_codes, Unset):
        if product_codes is None:
            json_product_codes = None
        else:
            json_product_codes = product_codes

    params["productCodes"] = json_product_codes

    json_article_name_contains: Union[Unset, None, List[str]] = UNSET
    if not isinstance(article_name_contains, Unset):
        if article_name_contains is None:
            json_article_name_contains = None
        else:
            json_article_name_contains = article_name_contains

    params["articleNameContains"] = json_article_name_contains

    json_article_class_ids: Union[Unset, None, List[int]] = UNSET
    if not isinstance(article_class_ids, Unset):
        if article_class_ids is None:
            json_article_class_ids = None
        else:
            json_article_class_ids = article_class_ids

    params["articleClassIds"] = json_article_class_ids

    json_bar_codes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(bar_codes, Unset):
        if bar_codes is None:
            json_bar_codes = None
        else:
            json_bar_codes = bar_codes

    params["barCodes"] = json_bar_codes

    params["onlyArticlesBelowStockLimit"] = only_articles_below_stock_limit

    params[
        "onlyArticlesBelowStockLimitConsideringNumberOfBookedItems"
    ] = only_articles_below_stock_limit_considering_number_of_booked_items

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Optional[List["GetArticleModel"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200 or []:
            response_200_item = GetArticleModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Optional[List["GetArticleModel"]]]:
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
    article_number: Union[Unset, None, str] = UNSET,
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    article_data_last_updated_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    product_code: Union[Unset, None, str] = UNSET,
    product_codes: Union[Unset, None, List[str]] = UNSET,
    article_name_contains: Union[Unset, None, List[str]] = UNSET,
    article_class_ids: Union[Unset, None, List[int]] = UNSET,
    bar_codes: Union[Unset, None, List[str]] = UNSET,
    only_articles_below_stock_limit: Union[Unset, None, bool] = UNSET,
    only_articles_below_stock_limit_considering_number_of_booked_items: Union[Unset, None, bool] = UNSET,
) -> Response[Optional[List["GetArticleModel"]]]:
    """Get all articles which match the specified search criteria.

    Args:
        goods_owner_id (int):
        article_number (Union[Unset, None, str]):
        article_system_id_from (Union[Unset, None, int]):
        max_articles_to_get (Union[Unset, None, int]):
        stock_info_changed_from (Union[Unset, None, datetime.datetime]):
        article_numbers (Union[Unset, None, List[str]]):
        article_data_last_updated_from (Union[Unset, None, datetime.datetime]):
        only_articles_in_stock (Union[Unset, None, bool]):
        product_code (Union[Unset, None, str]):
        product_codes (Union[Unset, None, List[str]]):
        article_name_contains (Union[Unset, None, List[str]]):
        article_class_ids (Union[Unset, None, List[int]]):
        bar_codes (Union[Unset, None, List[str]]):
        only_articles_below_stock_limit (Union[Unset, None, bool]):
        only_articles_below_stock_limit_considering_number_of_booked_items (Union[Unset, None,
            bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Optional[List['GetArticleModel']]]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        article_number=article_number,
        article_system_id_from=article_system_id_from,
        max_articles_to_get=max_articles_to_get,
        stock_info_changed_from=stock_info_changed_from,
        article_numbers=article_numbers,
        article_data_last_updated_from=article_data_last_updated_from,
        only_articles_in_stock=only_articles_in_stock,
        product_code=product_code,
        product_codes=product_codes,
        article_name_contains=article_name_contains,
        article_class_ids=article_class_ids,
        bar_codes=bar_codes,
        only_articles_below_stock_limit=only_articles_below_stock_limit,
        only_articles_below_stock_limit_considering_number_of_booked_items=only_articles_below_stock_limit_considering_number_of_booked_items,
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
    article_number: Union[Unset, None, str] = UNSET,
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    article_data_last_updated_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    product_code: Union[Unset, None, str] = UNSET,
    product_codes: Union[Unset, None, List[str]] = UNSET,
    article_name_contains: Union[Unset, None, List[str]] = UNSET,
    article_class_ids: Union[Unset, None, List[int]] = UNSET,
    bar_codes: Union[Unset, None, List[str]] = UNSET,
    only_articles_below_stock_limit: Union[Unset, None, bool] = UNSET,
    only_articles_below_stock_limit_considering_number_of_booked_items: Union[Unset, None, bool] = UNSET,
) -> Optional[Optional[List["GetArticleModel"]]]:
    """Get all articles which match the specified search criteria.

    Args:
        goods_owner_id (int):
        article_number (Union[Unset, None, str]):
        article_system_id_from (Union[Unset, None, int]):
        max_articles_to_get (Union[Unset, None, int]):
        stock_info_changed_from (Union[Unset, None, datetime.datetime]):
        article_numbers (Union[Unset, None, List[str]]):
        article_data_last_updated_from (Union[Unset, None, datetime.datetime]):
        only_articles_in_stock (Union[Unset, None, bool]):
        product_code (Union[Unset, None, str]):
        product_codes (Union[Unset, None, List[str]]):
        article_name_contains (Union[Unset, None, List[str]]):
        article_class_ids (Union[Unset, None, List[int]]):
        bar_codes (Union[Unset, None, List[str]]):
        only_articles_below_stock_limit (Union[Unset, None, bool]):
        only_articles_below_stock_limit_considering_number_of_booked_items (Union[Unset, None,
            bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[List['GetArticleModel']]
    """

    return sync_detailed(
        client=client,
        goods_owner_id=goods_owner_id,
        article_number=article_number,
        article_system_id_from=article_system_id_from,
        max_articles_to_get=max_articles_to_get,
        stock_info_changed_from=stock_info_changed_from,
        article_numbers=article_numbers,
        article_data_last_updated_from=article_data_last_updated_from,
        only_articles_in_stock=only_articles_in_stock,
        product_code=product_code,
        product_codes=product_codes,
        article_name_contains=article_name_contains,
        article_class_ids=article_class_ids,
        bar_codes=bar_codes,
        only_articles_below_stock_limit=only_articles_below_stock_limit,
        only_articles_below_stock_limit_considering_number_of_booked_items=only_articles_below_stock_limit_considering_number_of_booked_items,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    goods_owner_id: int,
    article_number: Union[Unset, None, str] = UNSET,
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    article_data_last_updated_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    product_code: Union[Unset, None, str] = UNSET,
    product_codes: Union[Unset, None, List[str]] = UNSET,
    article_name_contains: Union[Unset, None, List[str]] = UNSET,
    article_class_ids: Union[Unset, None, List[int]] = UNSET,
    bar_codes: Union[Unset, None, List[str]] = UNSET,
    only_articles_below_stock_limit: Union[Unset, None, bool] = UNSET,
    only_articles_below_stock_limit_considering_number_of_booked_items: Union[Unset, None, bool] = UNSET,
) -> Response[Optional[List["GetArticleModel"]]]:
    """Get all articles which match the specified search criteria.

    Args:
        goods_owner_id (int):
        article_number (Union[Unset, None, str]):
        article_system_id_from (Union[Unset, None, int]):
        max_articles_to_get (Union[Unset, None, int]):
        stock_info_changed_from (Union[Unset, None, datetime.datetime]):
        article_numbers (Union[Unset, None, List[str]]):
        article_data_last_updated_from (Union[Unset, None, datetime.datetime]):
        only_articles_in_stock (Union[Unset, None, bool]):
        product_code (Union[Unset, None, str]):
        product_codes (Union[Unset, None, List[str]]):
        article_name_contains (Union[Unset, None, List[str]]):
        article_class_ids (Union[Unset, None, List[int]]):
        bar_codes (Union[Unset, None, List[str]]):
        only_articles_below_stock_limit (Union[Unset, None, bool]):
        only_articles_below_stock_limit_considering_number_of_booked_items (Union[Unset, None,
            bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Optional[List['GetArticleModel']]]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        article_number=article_number,
        article_system_id_from=article_system_id_from,
        max_articles_to_get=max_articles_to_get,
        stock_info_changed_from=stock_info_changed_from,
        article_numbers=article_numbers,
        article_data_last_updated_from=article_data_last_updated_from,
        only_articles_in_stock=only_articles_in_stock,
        product_code=product_code,
        product_codes=product_codes,
        article_name_contains=article_name_contains,
        article_class_ids=article_class_ids,
        bar_codes=bar_codes,
        only_articles_below_stock_limit=only_articles_below_stock_limit,
        only_articles_below_stock_limit_considering_number_of_booked_items=only_articles_below_stock_limit_considering_number_of_booked_items,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    goods_owner_id: int,
    article_number: Union[Unset, None, str] = UNSET,
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    article_data_last_updated_from: Union[Unset, None, datetime.datetime] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    product_code: Union[Unset, None, str] = UNSET,
    product_codes: Union[Unset, None, List[str]] = UNSET,
    article_name_contains: Union[Unset, None, List[str]] = UNSET,
    article_class_ids: Union[Unset, None, List[int]] = UNSET,
    bar_codes: Union[Unset, None, List[str]] = UNSET,
    only_articles_below_stock_limit: Union[Unset, None, bool] = UNSET,
    only_articles_below_stock_limit_considering_number_of_booked_items: Union[Unset, None, bool] = UNSET,
) -> Optional[Optional[List["GetArticleModel"]]]:
    """Get all articles which match the specified search criteria.

    Args:
        goods_owner_id (int):
        article_number (Union[Unset, None, str]):
        article_system_id_from (Union[Unset, None, int]):
        max_articles_to_get (Union[Unset, None, int]):
        stock_info_changed_from (Union[Unset, None, datetime.datetime]):
        article_numbers (Union[Unset, None, List[str]]):
        article_data_last_updated_from (Union[Unset, None, datetime.datetime]):
        only_articles_in_stock (Union[Unset, None, bool]):
        product_code (Union[Unset, None, str]):
        product_codes (Union[Unset, None, List[str]]):
        article_name_contains (Union[Unset, None, List[str]]):
        article_class_ids (Union[Unset, None, List[int]]):
        bar_codes (Union[Unset, None, List[str]]):
        only_articles_below_stock_limit (Union[Unset, None, bool]):
        only_articles_below_stock_limit_considering_number_of_booked_items (Union[Unset, None,
            bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[List['GetArticleModel']]
    """

    return (
        await asyncio_detailed(
            client=client,
            goods_owner_id=goods_owner_id,
            article_number=article_number,
            article_system_id_from=article_system_id_from,
            max_articles_to_get=max_articles_to_get,
            stock_info_changed_from=stock_info_changed_from,
            article_numbers=article_numbers,
            article_data_last_updated_from=article_data_last_updated_from,
            only_articles_in_stock=only_articles_in_stock,
            product_code=product_code,
            product_codes=product_codes,
            article_name_contains=article_name_contains,
            article_class_ids=article_class_ids,
            bar_codes=bar_codes,
            only_articles_below_stock_limit=only_articles_below_stock_limit,
            only_articles_below_stock_limit_considering_number_of_booked_items=only_articles_below_stock_limit_considering_number_of_booked_items,
        )
    ).parsed
