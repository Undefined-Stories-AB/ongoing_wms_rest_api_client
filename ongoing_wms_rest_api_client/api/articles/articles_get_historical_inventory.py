import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_historical_inventory_model import GetHistoricalInventoryModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    goods_owner_id: int,
    stock_date: datetime.datetime,
    warehouse_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/articles/historicalInventory".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["goodsOwnerId"] = goods_owner_id

    json_stock_date = stock_date.isoformat()

    params["stockDate"] = json_stock_date

    params["warehouseId"] = warehouse_id

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["GetHistoricalInventoryModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetHistoricalInventoryModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["GetHistoricalInventoryModel"]]:
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
    stock_date: datetime.datetime,
    warehouse_id: Union[Unset, None, int] = UNSET,
) -> Response[List["GetHistoricalInventoryModel"]]:
    """Get the historical stock balances for all articles at a specific time in the past.

    Args:
        goods_owner_id (int):
        stock_date (datetime.datetime):
        warehouse_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetHistoricalInventoryModel']]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        stock_date=stock_date,
        warehouse_id=warehouse_id,
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
    stock_date: datetime.datetime,
    warehouse_id: Union[Unset, None, int] = UNSET,
) -> Optional[List["GetHistoricalInventoryModel"]]:
    """Get the historical stock balances for all articles at a specific time in the past.

    Args:
        goods_owner_id (int):
        stock_date (datetime.datetime):
        warehouse_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetHistoricalInventoryModel']
    """

    return sync_detailed(
        client=client,
        goods_owner_id=goods_owner_id,
        stock_date=stock_date,
        warehouse_id=warehouse_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    goods_owner_id: int,
    stock_date: datetime.datetime,
    warehouse_id: Union[Unset, None, int] = UNSET,
) -> Response[List["GetHistoricalInventoryModel"]]:
    """Get the historical stock balances for all articles at a specific time in the past.

    Args:
        goods_owner_id (int):
        stock_date (datetime.datetime):
        warehouse_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetHistoricalInventoryModel']]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        stock_date=stock_date,
        warehouse_id=warehouse_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    goods_owner_id: int,
    stock_date: datetime.datetime,
    warehouse_id: Union[Unset, None, int] = UNSET,
) -> Optional[List["GetHistoricalInventoryModel"]]:
    """Get the historical stock balances for all articles at a specific time in the past.

    Args:
        goods_owner_id (int):
        stock_date (datetime.datetime):
        warehouse_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetHistoricalInventoryModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            goods_owner_id=goods_owner_id,
            stock_date=stock_date,
            warehouse_id=warehouse_id,
        )
    ).parsed
