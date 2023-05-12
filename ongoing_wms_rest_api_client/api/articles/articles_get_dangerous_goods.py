from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_article_dangerous_goods_model import GetArticleDangerousGoodsModel
from ...types import Response


def _get_kwargs(
    article_system_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/articles/{articleSystemId}/dangerousGoods".format(
        client.base_url, articleSystemId=article_system_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetArticleDangerousGoodsModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetArticleDangerousGoodsModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetArticleDangerousGoodsModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    article_system_id: int,
    *,
    client: Client,
) -> Response[GetArticleDangerousGoodsModel]:
    """Get dangerous goods info for an article.

    Args:
        article_system_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetArticleDangerousGoodsModel]
    """

    kwargs = _get_kwargs(
        article_system_id=article_system_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_system_id: int,
    *,
    client: Client,
) -> Optional[GetArticleDangerousGoodsModel]:
    """Get dangerous goods info for an article.

    Args:
        article_system_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetArticleDangerousGoodsModel
    """

    return sync_detailed(
        article_system_id=article_system_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    article_system_id: int,
    *,
    client: Client,
) -> Response[GetArticleDangerousGoodsModel]:
    """Get dangerous goods info for an article.

    Args:
        article_system_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetArticleDangerousGoodsModel]
    """

    kwargs = _get_kwargs(
        article_system_id=article_system_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_system_id: int,
    *,
    client: Client,
) -> Optional[GetArticleDangerousGoodsModel]:
    """Get dangerous goods info for an article.

    Args:
        article_system_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetArticleDangerousGoodsModel
    """

    return (
        await asyncio_detailed(
            article_system_id=article_system_id,
            client=client,
        )
    ).parsed
