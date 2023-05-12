import datetime
from typing import Any, Dict, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="PatchOrderDeliveryDate")


@attr.s(auto_attribs=True)
class PatchOrderDeliveryDate:
    """
    Attributes:
        delivery_date (datetime.datetime):
    """

    delivery_date: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        delivery_date = self.delivery_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "deliveryDate": delivery_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delivery_date = isoparse(d.pop("deliveryDate"))

        patch_order_delivery_date = cls(
            delivery_date=delivery_date,
        )

        return patch_order_delivery_date
