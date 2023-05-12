from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.post_article_class_model import PostArticleClassModel
from ...models.post_article_class_response import PostArticleClassResponse
from ...types import Response


def _get_kwargs(
    article_class_id: int,
    *,
    client: Client,
    json_body: PostArticleClassModel,
) -> Dict[str, Any]:
    url = "{}/api/v1/articles/classes/{articleClassId}".format(client.base_url, articleClassId=article_class_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostArticleClassResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostArticleClassResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostArticleClassResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    article_class_id: int,
    *,
    client: Client,
    json_body: PostArticleClassModel,
) -> Response[PostArticleClassResponse]:
    """Update an article class. The ID will be used to identify the article class.

    Args:
        article_class_id (int):
        json_body (PostArticleClassModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostArticleClassResponse]
    """

    kwargs = _get_kwargs(
        article_class_id=article_class_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_class_id: int,
    *,
    client: Client,
    json_body: PostArticleClassModel,
) -> Optional[PostArticleClassResponse]:
    """Update an article class. The ID will be used to identify the article class.

    Args:
        article_class_id (int):
        json_body (PostArticleClassModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostArticleClassResponse
    """

    return sync_detailed(
        article_class_id=article_class_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    article_class_id: int,
    *,
    client: Client,
    json_body: PostArticleClassModel,
) -> Response[PostArticleClassResponse]:
    """Update an article class. The ID will be used to identify the article class.

    Args:
        article_class_id (int):
        json_body (PostArticleClassModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostArticleClassResponse]
    """

    kwargs = _get_kwargs(
        article_class_id=article_class_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_class_id: int,
    *,
    client: Client,
    json_body: PostArticleClassModel,
) -> Optional[PostArticleClassResponse]:
    """Update an article class. The ID will be used to identify the article class.

    Args:
        article_class_id (int):
        json_body (PostArticleClassModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostArticleClassResponse
    """

    return (
        await asyncio_detailed(
            article_class_id=article_class_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
