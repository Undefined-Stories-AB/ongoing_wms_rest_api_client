from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.post_way_of_delivery_type_response import PostWayOfDeliveryTypeResponse
from ...types import Response


def _get_kwargs(
    way_of_delivery_type_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/orders/wayOfDeliveryTypes/{wayOfDeliveryTypeId}".format(
        client.base_url, wayOfDeliveryTypeId=way_of_delivery_type_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostWayOfDeliveryTypeResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostWayOfDeliveryTypeResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostWayOfDeliveryTypeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    way_of_delivery_type_id: int,
    *,
    client: Client,
) -> Response[PostWayOfDeliveryTypeResponse]:
    """Delete a way of delivery type.

    Args:
        way_of_delivery_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostWayOfDeliveryTypeResponse]
    """

    kwargs = _get_kwargs(
        way_of_delivery_type_id=way_of_delivery_type_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    way_of_delivery_type_id: int,
    *,
    client: Client,
) -> Optional[PostWayOfDeliveryTypeResponse]:
    """Delete a way of delivery type.

    Args:
        way_of_delivery_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostWayOfDeliveryTypeResponse
    """

    return sync_detailed(
        way_of_delivery_type_id=way_of_delivery_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    way_of_delivery_type_id: int,
    *,
    client: Client,
) -> Response[PostWayOfDeliveryTypeResponse]:
    """Delete a way of delivery type.

    Args:
        way_of_delivery_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostWayOfDeliveryTypeResponse]
    """

    kwargs = _get_kwargs(
        way_of_delivery_type_id=way_of_delivery_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    way_of_delivery_type_id: int,
    *,
    client: Client,
) -> Optional[PostWayOfDeliveryTypeResponse]:
    """Delete a way of delivery type.

    Args:
        way_of_delivery_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostWayOfDeliveryTypeResponse
    """

    return (
        await asyncio_detailed(
            way_of_delivery_type_id=way_of_delivery_type_id,
            client=client,
        )
    ).parsed
