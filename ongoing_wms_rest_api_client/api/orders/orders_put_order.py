from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.post_order_model import PostOrderModel
from ...models.post_order_response import PostOrderResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PostOrderModel,
) -> Dict[str, Any]:
    url = "{}/api/v1/orders".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostOrderResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostOrderResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = PostOrderResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PostOrderModel,
) -> Response[PostOrderResponse]:
    """Create or update an order. If there is no order with the specified order number, it will be created.
    Otherwise, the existing order will be updated. Note that you are not allowed to update an order
    after the warehouse has started working on it.

    Args:
        json_body (PostOrderModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOrderResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: PostOrderModel,
) -> Optional[PostOrderResponse]:
    """Create or update an order. If there is no order with the specified order number, it will be created.
    Otherwise, the existing order will be updated. Note that you are not allowed to update an order
    after the warehouse has started working on it.

    Args:
        json_body (PostOrderModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOrderResponse
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PostOrderModel,
) -> Response[PostOrderResponse]:
    """Create or update an order. If there is no order with the specified order number, it will be created.
    Otherwise, the existing order will be updated. Note that you are not allowed to update an order
    after the warehouse has started working on it.

    Args:
        json_body (PostOrderModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOrderResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PostOrderModel,
) -> Optional[PostOrderResponse]:
    """Create or update an order. If there is no order with the specified order number, it will be created.
    Otherwise, the existing order will be updated. Note that you are not allowed to update an order
    after the warehouse has started working on it.

    Args:
        json_body (PostOrderModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOrderResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
