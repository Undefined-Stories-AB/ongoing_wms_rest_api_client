from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderConsigneeCustomerNotification")


@attr.s(auto_attribs=True)
class GetOrderConsigneeCustomerNotification:
    """
    Attributes:
        to_be_notified (Union[Unset, bool]):
        value (Union[Unset, None, str]):
    """

    to_be_notified: Union[Unset, bool] = UNSET
    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        to_be_notified = self.to_be_notified
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if to_be_notified is not UNSET:
            field_dict["toBeNotified"] = to_be_notified
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        to_be_notified = d.pop("toBeNotified", UNSET)

        value = d.pop("value", UNSET)

        get_order_consignee_customer_notification = cls(
            to_be_notified=to_be_notified,
            value=value,
        )

        return get_order_consignee_customer_notification
