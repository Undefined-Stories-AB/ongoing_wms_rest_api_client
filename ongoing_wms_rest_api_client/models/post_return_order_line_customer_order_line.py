from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostReturnOrderLineCustomerOrderLine")


@attr.s(auto_attribs=True)
class PostReturnOrderLineCustomerOrderLine:
    """
    Attributes:
        order_line_id (Union[Unset, int]):
    """

    order_line_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_line_id = self.order_line_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_line_id is not UNSET:
            field_dict["orderLineId"] = order_line_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_line_id = d.pop("orderLineId", UNSET)

        post_return_order_line_customer_order_line = cls(
            order_line_id=order_line_id,
        )

        return post_return_order_line_customer_order_line
