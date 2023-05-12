from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderArticleItemResponseMessage")


@attr.s(auto_attribs=True)
class PurchaseOrderArticleItemResponseMessage:
    """
    Attributes:
        purchase_order_line_id (Union[Unset, int]):
        article_item_id (Union[Unset, None, int]):
        success (Union[Unset, bool]):
        message (Union[Unset, None, str]):
    """

    purchase_order_line_id: Union[Unset, int] = UNSET
    article_item_id: Union[Unset, None, int] = UNSET
    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_line_id = self.purchase_order_line_id
        article_item_id = self.article_item_id
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if purchase_order_line_id is not UNSET:
            field_dict["purchaseOrderLineId"] = purchase_order_line_id
        if article_item_id is not UNSET:
            field_dict["articleItemId"] = article_item_id
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        purchase_order_line_id = d.pop("purchaseOrderLineId", UNSET)

        article_item_id = d.pop("articleItemId", UNSET)

        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        purchase_order_article_item_response_message = cls(
            purchase_order_line_id=purchase_order_line_id,
            article_item_id=article_item_id,
            success=success,
            message=message,
        )

        return purchase_order_article_item_response_message
