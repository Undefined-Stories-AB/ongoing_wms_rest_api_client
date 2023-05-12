from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.post_file_no_filename_model import PostFileNoFilenameModel
from ...models.post_file_response import PostFileResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    article_system_id: int,
    *,
    client: Client,
    json_body: PostFileNoFilenameModel,
    file_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/articles/{articleSystemId}/files".format(client.base_url, articleSystemId=article_system_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fileName"] = file_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostFileResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostFileResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostFileResponse]:
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
    json_body: PostFileNoFilenameModel,
    file_name: Union[Unset, None, str] = UNSET,
) -> Response[PostFileResponse]:
    """Create or update a file which is attached to an article. The filename will be used to check if the
    file already exists.

    Args:
        article_system_id (int):
        file_name (Union[Unset, None, str]):
        json_body (PostFileNoFilenameModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFileResponse]
    """

    kwargs = _get_kwargs(
        article_system_id=article_system_id,
        client=client,
        json_body=json_body,
        file_name=file_name,
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
    json_body: PostFileNoFilenameModel,
    file_name: Union[Unset, None, str] = UNSET,
) -> Optional[PostFileResponse]:
    """Create or update a file which is attached to an article. The filename will be used to check if the
    file already exists.

    Args:
        article_system_id (int):
        file_name (Union[Unset, None, str]):
        json_body (PostFileNoFilenameModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFileResponse
    """

    return sync_detailed(
        article_system_id=article_system_id,
        client=client,
        json_body=json_body,
        file_name=file_name,
    ).parsed


async def asyncio_detailed(
    article_system_id: int,
    *,
    client: Client,
    json_body: PostFileNoFilenameModel,
    file_name: Union[Unset, None, str] = UNSET,
) -> Response[PostFileResponse]:
    """Create or update a file which is attached to an article. The filename will be used to check if the
    file already exists.

    Args:
        article_system_id (int):
        file_name (Union[Unset, None, str]):
        json_body (PostFileNoFilenameModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFileResponse]
    """

    kwargs = _get_kwargs(
        article_system_id=article_system_id,
        client=client,
        json_body=json_body,
        file_name=file_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_system_id: int,
    *,
    client: Client,
    json_body: PostFileNoFilenameModel,
    file_name: Union[Unset, None, str] = UNSET,
) -> Optional[PostFileResponse]:
    """Create or update a file which is attached to an article. The filename will be used to check if the
    file already exists.

    Args:
        article_system_id (int):
        file_name (Union[Unset, None, str]):
        json_body (PostFileNoFilenameModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFileResponse
    """

    return (
        await asyncio_detailed(
            article_system_id=article_system_id,
            client=client,
            json_body=json_body,
            file_name=file_name,
        )
    ).parsed
