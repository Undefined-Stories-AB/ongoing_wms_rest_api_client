from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.post_parcel_response import PostParcelResponse
from ...models.post_parcel_type_model import PostParcelTypeModel
from ...types import Response


def _get_kwargs(
    order_id: int,
    *,
    client: Client,
    json_body: PostParcelTypeModel,
) -> Dict[str, Any]:
    url = "{}/api/v1/orders/{orderId}/parcels".format(client.base_url, orderId=order_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostParcelResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostParcelResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostParcelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: int,
    *,
    client: Client,
    json_body: PostParcelTypeModel,
) -> Response[PostParcelResponse]:
    """Create or update a parcel on an order.

    Args:
        order_id (int):
        json_body (PostParcelTypeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostParcelResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: int,
    *,
    client: Client,
    json_body: PostParcelTypeModel,
) -> Optional[PostParcelResponse]:
    """Create or update a parcel on an order.

    Args:
        order_id (int):
        json_body (PostParcelTypeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostParcelResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    order_id: int,
    *,
    client: Client,
    json_body: PostParcelTypeModel,
) -> Response[PostParcelResponse]:
    """Create or update a parcel on an order.

    Args:
        order_id (int):
        json_body (PostParcelTypeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostParcelResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: int,
    *,
    client: Client,
    json_body: PostParcelTypeModel,
) -> Optional[PostParcelResponse]:
    """Create or update a parcel on an order.

    Args:
        order_id (int):
        json_body (PostParcelTypeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostParcelResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
