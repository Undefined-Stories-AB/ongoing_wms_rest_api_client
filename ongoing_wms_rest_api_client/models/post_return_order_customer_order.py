from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostReturnOrderCustomerOrder")


@attr.s(auto_attribs=True)
class PostReturnOrderCustomerOrder:
    """
    Attributes:
        order_id (Union[Unset, int]):
    """

    order_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId", UNSET)

        post_return_order_customer_order = cls(
            order_id=order_id,
        )

        return post_return_order_customer_order
