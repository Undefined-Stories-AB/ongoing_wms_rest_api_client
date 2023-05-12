from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patch_order_reported_returned_number_of_items_model import PatchOrderReportedReturnedNumberOfItemsModel
from ...types import File, Response


def _get_kwargs(
    order_id: int,
    order_line_id: int,
    *,
    client: Client,
    json_body: PatchOrderReportedReturnedNumberOfItemsModel,
) -> Dict[str, Any]:
    url = "{}/api/v1/orders/{orderId}/lines/{orderLineId}/reportedReturnedNumberOfItems".format(
        client.base_url, orderId=order_id, orderLineId=order_line_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[File]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: int,
    order_line_id: int,
    *,
    client: Client,
    json_body: PatchOrderReportedReturnedNumberOfItemsModel,
) -> Response[File]:
    """Update the reported returned number of items on a particular order line.

    Args:
        order_id (int):
        order_line_id (int):
        json_body (PatchOrderReportedReturnedNumberOfItemsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        order_line_id=order_line_id,
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
    order_line_id: int,
    *,
    client: Client,
    json_body: PatchOrderReportedReturnedNumberOfItemsModel,
) -> Optional[File]:
    """Update the reported returned number of items on a particular order line.

    Args:
        order_id (int):
        order_line_id (int):
        json_body (PatchOrderReportedReturnedNumberOfItemsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        order_id=order_id,
        order_line_id=order_line_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    order_id: int,
    order_line_id: int,
    *,
    client: Client,
    json_body: PatchOrderReportedReturnedNumberOfItemsModel,
) -> Response[File]:
    """Update the reported returned number of items on a particular order line.

    Args:
        order_id (int):
        order_line_id (int):
        json_body (PatchOrderReportedReturnedNumberOfItemsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        order_line_id=order_line_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: int,
    order_line_id: int,
    *,
    client: Client,
    json_body: PatchOrderReportedReturnedNumberOfItemsModel,
) -> Optional[File]:
    """Update the reported returned number of items on a particular order line.

    Args:
        order_id (int):
        order_line_id (int):
        json_body (PatchOrderReportedReturnedNumberOfItemsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            order_line_id=order_line_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
