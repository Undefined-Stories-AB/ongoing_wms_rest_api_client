from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPurchaseOrderResponse")


@attr.s(auto_attribs=True)
class PostPurchaseOrderResponse:
    """
    Attributes:
        purchase_order_id (Union[Unset, None, int]):
        message (Union[Unset, None, str]):
    """

    purchase_order_id: Union[Unset, None, int] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_id = self.purchase_order_id
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if purchase_order_id is not UNSET:
            field_dict["purchaseOrderId"] = purchase_order_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        purchase_order_id = d.pop("purchaseOrderId", UNSET)

        message = d.pop("message", UNSET)

        post_purchase_order_response = cls(
            purchase_order_id=purchase_order_id,
            message=message,
        )

        return post_purchase_order_response
