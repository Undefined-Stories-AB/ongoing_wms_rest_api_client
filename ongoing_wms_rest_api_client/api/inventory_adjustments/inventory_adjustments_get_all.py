import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_inventory_adjustments_line import GetInventoryAdjustmentsLine
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    goods_owner_id: int,
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    to_time: Union[Unset, None, datetime.datetime] = UNSET,
    is_reported: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/inventoryAdjustments".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["goodsOwnerId"] = goods_owner_id

    json_from_: Union[Unset, None, str] = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat() if from_ else None

    params["from"] = json_from_

    json_to: Union[Unset, None, str] = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat() if to else None

    params["to"] = json_to

    json_to_time: Union[Unset, None, str] = UNSET
    if not isinstance(to_time, Unset):
        json_to_time = to_time.isoformat() if to_time else None

    params["toTime"] = json_to_time

    params["isReported"] = is_reported

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
) -> Optional[Optional[List["GetInventoryAdjustmentsLine"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200 or []:
            response_200_item = GetInventoryAdjustmentsLine.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Optional[List["GetInventoryAdjustmentsLine"]]]:
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
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    to_time: Union[Unset, None, datetime.datetime] = UNSET,
    is_reported: Union[Unset, None, bool] = UNSET,
) -> Response[Optional[List["GetInventoryAdjustmentsLine"]]]:
    """Get all inventory adjustments which match the specified search criteria.

    Args:
        goods_owner_id (int):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
        to_time (Union[Unset, None, datetime.datetime]):
        is_reported (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Optional[List['GetInventoryAdjustmentsLine']]]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        from_=from_,
        to=to,
        to_time=to_time,
        is_reported=is_reported,
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
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    to_time: Union[Unset, None, datetime.datetime] = UNSET,
    is_reported: Union[Unset, None, bool] = UNSET,
) -> Optional[Optional[List["GetInventoryAdjustmentsLine"]]]:
    """Get all inventory adjustments which match the specified search criteria.

    Args:
        goods_owner_id (int):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
        to_time (Union[Unset, None, datetime.datetime]):
        is_reported (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[List['GetInventoryAdjustmentsLine']]
    """

    return sync_detailed(
        client=client,
        goods_owner_id=goods_owner_id,
        from_=from_,
        to=to,
        to_time=to_time,
        is_reported=is_reported,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    goods_owner_id: int,
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    to_time: Union[Unset, None, datetime.datetime] = UNSET,
    is_reported: Union[Unset, None, bool] = UNSET,
) -> Response[Optional[List["GetInventoryAdjustmentsLine"]]]:
    """Get all inventory adjustments which match the specified search criteria.

    Args:
        goods_owner_id (int):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
        to_time (Union[Unset, None, datetime.datetime]):
        is_reported (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Optional[List['GetInventoryAdjustmentsLine']]]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
        from_=from_,
        to=to,
        to_time=to_time,
        is_reported=is_reported,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    goods_owner_id: int,
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    to_time: Union[Unset, None, datetime.datetime] = UNSET,
    is_reported: Union[Unset, None, bool] = UNSET,
) -> Optional[Optional[List["GetInventoryAdjustmentsLine"]]]:
    """Get all inventory adjustments which match the specified search criteria.

    Args:
        goods_owner_id (int):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
        to_time (Union[Unset, None, datetime.datetime]):
        is_reported (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[List['GetInventoryAdjustmentsLine']]
    """

    return (
        await asyncio_detailed(
            client=client,
            goods_owner_id=goods_owner_id,
            from_=from_,
            to=to,
            to_time=to_time,
            is_reported=is_reported,
        )
    ).parsed
