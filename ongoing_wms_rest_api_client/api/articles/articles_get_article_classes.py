from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_article_classes_model import GetArticleClassesModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    goods_owner_id: int,
) -> Dict[str, Any]:
    url = "{}/api/v1/articles/classes".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetArticleClassesModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetArticleClassesModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetArticleClassesModel]:
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
) -> Response[GetArticleClassesModel]:
    """Get all article classes.

    Args:
        goods_owner_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetArticleClassesModel]
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
) -> Optional[GetArticleClassesModel]:
    """Get all article classes.

    Args:
        goods_owner_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetArticleClassesModel
    """

    return sync_detailed(
        client=client,
        goods_owner_id=goods_owner_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    goods_owner_id: int,
) -> Response[GetArticleClassesModel]:
    """Get all article classes.

    Args:
        goods_owner_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetArticleClassesModel]
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
) -> Optional[GetArticleClassesModel]:
    """Get all article classes.

    Args:
        goods_owner_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetArticleClassesModel
    """

    return (
        await asyncio_detailed(
            client=client,
            goods_owner_id=goods_owner_id,
        )
    ).parsed
