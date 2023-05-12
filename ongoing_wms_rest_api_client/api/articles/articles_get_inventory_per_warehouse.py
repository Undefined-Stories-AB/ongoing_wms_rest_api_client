import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_article_inventory_per_warehouse_model import GetArticleInventoryPerWarehouseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    goods_owner_id: int,
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    warehouse_ids: Union[Unset, None, List[int]] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/articles/inventoryPerWarehouse".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["goodsOwnerId"] = goods_owner_id

    params["articleSystemIdFrom"] = article_system_id_from

    params["maxArticlesToGet"] = max_articles_to_get

    json_article_numbers: Union[Unset, None, List[str]] = UNSET
    if not isinstance(article_numbers, Unset):
        if article_numbers is None:
            json_article_numbers = None
        else:
            json_article_numbers = article_numbers

    params["articleNumbers"] = json_article_numbers

    json_warehouse_ids: Union[Unset, None, List[int]] = UNSET
    if not isinstance(warehouse_ids, Unset):
        if warehouse_ids is None:
            json_warehouse_ids = None
        else:
            json_warehouse_ids = warehouse_ids

    params["warehouseIds"] = json_warehouse_ids

    params["onlyArticlesInStock"] = only_articles_in_stock

    json_stock_info_changed_from: Union[Unset, None, str] = UNSET
    if not isinstance(stock_info_changed_from, Unset):
        json_stock_info_changed_from = stock_info_changed_from.isoformat() if stock_info_changed_from else None

    params["stockInfoChangedFrom"] = json_stock_info_changed_from

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[List["GetArticleInventoryPerWarehouseModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetArticleInventoryPerWarehouseModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[List["GetArticleInventoryPerWarehouseModel"]]:
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
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    warehouse_ids: Union[Unset, None, List[int]] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[List["GetArticleInventoryPerWarehouseModel"]]:
    """Get inventory info (specified per warehouse) for the articles which match the filter.

    Args:
        goods_owner_id (int):
        article_system_id_from (Union[Unset, None, int]):
        max_articles_to_get (Union[Unset, None, int]):
        article_numbers (Union[Unset, None, List[str]]):
        warehouse_ids (Union[Unset, None, List[int]]):
        only_articles_in_stock (Union[Unset, None, bool]):
        stock_info_changed_from (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetArticleInventoryPerWarehouseModel']]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        article_system_id_from=article_system_id_from,
        max_articles_to_get=max_articles_to_get,
        article_numbers=article_numbers,
        warehouse_ids=warehouse_ids,
        only_articles_in_stock=only_articles_in_stock,
        stock_info_changed_from=stock_info_changed_from,
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
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    warehouse_ids: Union[Unset, None, List[int]] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[List["GetArticleInventoryPerWarehouseModel"]]:
    """Get inventory info (specified per warehouse) for the articles which match the filter.

    Args:
        goods_owner_id (int):
        article_system_id_from (Union[Unset, None, int]):
        max_articles_to_get (Union[Unset, None, int]):
        article_numbers (Union[Unset, None, List[str]]):
        warehouse_ids (Union[Unset, None, List[int]]):
        only_articles_in_stock (Union[Unset, None, bool]):
        stock_info_changed_from (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetArticleInventoryPerWarehouseModel']
    """

    return sync_detailed(
        client=client,
        goods_owner_id=goods_owner_id,
        article_system_id_from=article_system_id_from,
        max_articles_to_get=max_articles_to_get,
        article_numbers=article_numbers,
        warehouse_ids=warehouse_ids,
        only_articles_in_stock=only_articles_in_stock,
        stock_info_changed_from=stock_info_changed_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    goods_owner_id: int,
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    warehouse_ids: Union[Unset, None, List[int]] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[List["GetArticleInventoryPerWarehouseModel"]]:
    """Get inventory info (specified per warehouse) for the articles which match the filter.

    Args:
        goods_owner_id (int):
        article_system_id_from (Union[Unset, None, int]):
        max_articles_to_get (Union[Unset, None, int]):
        article_numbers (Union[Unset, None, List[str]]):
        warehouse_ids (Union[Unset, None, List[int]]):
        only_articles_in_stock (Union[Unset, None, bool]):
        stock_info_changed_from (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetArticleInventoryPerWarehouseModel']]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        article_system_id_from=article_system_id_from,
        max_articles_to_get=max_articles_to_get,
        article_numbers=article_numbers,
        warehouse_ids=warehouse_ids,
        only_articles_in_stock=only_articles_in_stock,
        stock_info_changed_from=stock_info_changed_from,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    goods_owner_id: int,
    article_system_id_from: Union[Unset, None, int] = UNSET,
    max_articles_to_get: Union[Unset, None, int] = UNSET,
    article_numbers: Union[Unset, None, List[str]] = UNSET,
    warehouse_ids: Union[Unset, None, List[int]] = UNSET,
    only_articles_in_stock: Union[Unset, None, bool] = UNSET,
    stock_info_changed_from: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[List["GetArticleInventoryPerWarehouseModel"]]:
    """Get inventory info (specified per warehouse) for the articles which match the filter.

    Args:
        goods_owner_id (int):
        article_system_id_from (Union[Unset, None, int]):
        max_articles_to_get (Union[Unset, None, int]):
        article_numbers (Union[Unset, None, List[str]]):
        warehouse_ids (Union[Unset, None, List[int]]):
        only_articles_in_stock (Union[Unset, None, bool]):
        stock_info_changed_from (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetArticleInventoryPerWarehouseModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            goods_owner_id=goods_owner_id,
            article_system_id_from=article_system_id_from,
            max_articles_to_get=max_articles_to_get,
            article_numbers=article_numbers,
            warehouse_ids=warehouse_ids,
            only_articles_in_stock=only_articles_in_stock,
            stock_info_changed_from=stock_info_changed_from,
        )
    ).parsed
