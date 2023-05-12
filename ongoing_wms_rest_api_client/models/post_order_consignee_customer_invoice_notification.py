from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOrderConsigneeCustomerInvoiceNotification")


@attr.s(auto_attribs=True)
class PostOrderConsigneeCustomerInvoiceNotification:
    """
    Attributes:
        value (Union[Unset, None, str]):
    """

    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        post_order_consignee_customer_invoice_notification = cls(
            value=value,
        )

        return post_order_consignee_customer_invoice_notification
