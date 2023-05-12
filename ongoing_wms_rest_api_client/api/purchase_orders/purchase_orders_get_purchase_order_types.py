from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_purchase_order_types_model import GetPurchaseOrderTypesModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    goods_owner_id: int,
) -> Dict[str, Any]:
    url = "{}/api/v1/purchaseOrders/types".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["goodsOwnerId"] = goods_owner_id

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetPurchaseOrderTypesModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPurchaseOrderTypesModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetPurchaseOrderTypesModel]:
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
) -> Response[GetPurchaseOrderTypesModel]:
    """Get all purchase order types for a particular goods owner.

    Args:
        goods_owner_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrderTypesModel]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
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
) -> Optional[GetPurchaseOrderTypesModel]:
    """Get all purchase order types for a particular goods owner.

    Args:
        goods_owner_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPurchaseOrderTypesModel
    """

    return sync_detailed(
        client=client,
        goods_owner_id=goods_owner_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    goods_owner_id: int,
) -> Response[GetPurchaseOrderTypesModel]:
    """Get all purchase order types for a particular goods owner.

    Args:
        goods_owner_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrderTypesModel]
    """

    kwargs = _get_kwargs(
        client=client,
        goods_owner_id=goods_owner_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    goods_owner_id: int,
) -> Optional[GetPurchaseOrderTypesModel]:
    """Get all purchase order types for a particular goods owner.

    Args:
        goods_owner_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPurchaseOrderTypesModel
    """

    return (
        await asyncio_detailed(
            client=client,
            goods_owner_id=goods_owner_id,
        )
    ).parsed
