from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderBackOrderInfo")


@attr.s(auto_attribs=True)
class GetOrderBackOrderInfo:
    """
    Attributes:
        back_order_for_order_id (Union[Unset, int]):
    """

    back_order_for_order_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        back_order_for_order_id = self.back_order_for_order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if back_order_for_order_id is not UNSET:
            field_dict["backOrderForOrderId"] = back_order_for_order_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        back_order_for_order_id = d.pop("backOrderForOrderId", UNSET)

        get_order_back_order_info = cls(
            back_order_for_order_id=back_order_for_order_id,
        )

        return get_order_back_order_info
