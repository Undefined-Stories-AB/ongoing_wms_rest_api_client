from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patch_inventory_adjustment_articles_reported_response import (
    PatchInventoryAdjustmentArticlesReportedResponse,
)
from ...types import Response


def _get_kwargs(
    inventory_id: int,
    article_system_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/inventoryAdjustments/{inventoryId}/articles/{articleSystemId}/setReported".format(
        client.base_url, inventoryId=inventory_id, articleSystemId=article_system_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[PatchInventoryAdjustmentArticlesReportedResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PatchInventoryAdjustmentArticlesReportedResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PatchInventoryAdjustmentArticlesReportedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inventory_id: int,
    article_system_id: int,
    *,
    client: Client,
) -> Response[PatchInventoryAdjustmentArticlesReportedResponse]:
    """Sets the 'reported' flag on an inventory to true for the specified article.

    Args:
        inventory_id (int):
        article_system_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInventoryAdjustmentArticlesReportedResponse]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        article_system_id=article_system_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    inventory_id: int,
    article_system_id: int,
    *,
    client: Client,
) -> Optional[PatchInventoryAdjustmentArticlesReportedResponse]:
    """Sets the 'reported' flag on an inventory to true for the specified article.

    Args:
        inventory_id (int):
        article_system_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInventoryAdjustmentArticlesReportedResponse
    """

    return sync_detailed(
        inventory_id=inventory_id,
        article_system_id=article_system_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    inventory_id: int,
    article_system_id: int,
    *,
    client: Client,
) -> Response[PatchInventoryAdjustmentArticlesReportedResponse]:
    """Sets the 'reported' flag on an inventory to true for the specified article.

    Args:
        inventory_id (int):
        article_system_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInventoryAdjustmentArticlesReportedResponse]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        article_system_id=article_system_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    inventory_id: int,
    article_system_id: int,
    *,
    client: Client,
) -> Optional[PatchInventoryAdjustmentArticlesReportedResponse]:
    """Sets the 'reported' flag on an inventory to true for the specified article.

    Args:
        inventory_id (int):
        article_system_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInventoryAdjustmentArticlesReportedResponse
    """

    return (
        await asyncio_detailed(
            inventory_id=inventory_id,
            article_system_id=article_system_id,
            client=client,
        )
    ).parsed
