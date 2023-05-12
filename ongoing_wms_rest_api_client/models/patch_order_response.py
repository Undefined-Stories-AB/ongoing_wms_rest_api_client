from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchOrderResponse")


@attr.s(auto_attribs=True)
class PatchOrderResponse:
    """
    Attributes:
        order_id (Union[Unset, int]):
        message (Union[Unset, None, str]):
    """

    order_id: Union[Unset, int] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId", UNSET)

        message = d.pop("message", UNSET)

        patch_order_response = cls(
            order_id=order_id,
            message=message,
        )

        return patch_order_response
