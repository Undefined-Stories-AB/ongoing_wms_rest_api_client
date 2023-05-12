from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.post_return_order_line_customer_order_line import PostReturnOrderLineCustomerOrderLine


T = TypeVar("T", bound="PostReturnOrderLine")


@attr.s(auto_attribs=True)
class PostReturnOrderLine:
    """
    Attributes:
        return_order_row_number (str):
        customer_order_line (PostReturnOrderLineCustomerOrderLine):
        to_be_returned_number_of_items (float):
        return_cause (Union[Unset, None, CodeNamePair]):
    """

    return_order_row_number: str
    customer_order_line: "PostReturnOrderLineCustomerOrderLine"
    to_be_returned_number_of_items: float
    return_cause: Union[Unset, None, "CodeNamePair"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        return_order_row_number = self.return_order_row_number
        customer_order_line = self.customer_order_line.to_dict()

        to_be_returned_number_of_items = self.to_be_returned_number_of_items
        return_cause: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.return_cause, Unset):
            return_cause = self.return_cause.to_dict() if self.return_cause else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "returnOrderRowNumber": return_order_row_number,
                "customerOrderLine": customer_order_line,
                "toBeReturnedNumberOfItems": to_be_returned_number_of_items,
            }
        )
        if return_cause is not UNSET:
            field_dict["returnCause"] = return_cause

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.post_return_order_line_customer_order_line import PostReturnOrderLineCustomerOrderLine

        d = src_dict.copy()
        return_order_row_number = d.pop("returnOrderRowNumber")

        customer_order_line = PostReturnOrderLineCustomerOrderLine.from_dict(d.pop("customerOrderLine"))

        to_be_returned_number_of_items = d.pop("toBeReturnedNumberOfItems")

        _return_cause = d.pop("returnCause", UNSET)
        return_cause: Union[Unset, None, CodeNamePair]
        if _return_cause is None:
            return_cause = None
        elif isinstance(_return_cause, Unset):
            return_cause = UNSET
        else:
            return_cause = CodeNamePair.from_dict(_return_cause)

        post_return_order_line = cls(
            return_order_row_number=return_order_row_number,
            customer_order_line=customer_order_line,
            to_be_returned_number_of_items=to_be_returned_number_of_items,
            return_cause=return_cause,
        )

        return post_return_order_line
