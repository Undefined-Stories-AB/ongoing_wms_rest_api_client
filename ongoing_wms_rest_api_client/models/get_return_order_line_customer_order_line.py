from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetReturnOrderLineCustomerOrderLine")


@attr.s(auto_attribs=True)
class GetReturnOrderLineCustomerOrderLine:
    """
    Attributes:
        order_line_id (Union[Unset, int]):
        customer_order_row_number (Union[Unset, None, str]):
    """

    order_line_id: Union[Unset, int] = UNSET
    customer_order_row_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_line_id = self.order_line_id
        customer_order_row_number = self.customer_order_row_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_line_id is not UNSET:
            field_dict["orderLineId"] = order_line_id
        if customer_order_row_number is not UNSET:
            field_dict["customerOrderRowNumber"] = customer_order_row_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_line_id = d.pop("orderLineId", UNSET)

        customer_order_row_number = d.pop("customerOrderRowNumber", UNSET)

        get_return_order_line_customer_order_line = cls(
            order_line_id=order_line_id,
            customer_order_row_number=customer_order_row_number,
        )

        return get_return_order_line_customer_order_line
