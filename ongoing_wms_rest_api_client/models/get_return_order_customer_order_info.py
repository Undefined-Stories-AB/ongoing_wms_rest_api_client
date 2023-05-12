from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetReturnOrderCustomerOrderInfo")


@attr.s(auto_attribs=True)
class GetReturnOrderCustomerOrderInfo:
    """
    Attributes:
        order_id (Union[Unset, int]):
        order_number (Union[Unset, None, str]):
    """

    order_id: Union[Unset, int] = UNSET
    order_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        order_number = self.order_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if order_number is not UNSET:
            field_dict["orderNumber"] = order_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId", UNSET)

        order_number = d.pop("orderNumber", UNSET)

        get_return_order_customer_order_info = cls(
            order_id=order_id,
            order_number=order_number,
        )

        return get_return_order_customer_order_info
