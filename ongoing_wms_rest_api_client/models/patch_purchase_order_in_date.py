import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchPurchaseOrderInDate")


@attr.s(auto_attribs=True)
class PatchPurchaseOrderInDate:
    """
    Attributes:
        in_date (Union[Unset, datetime.datetime]):
    """

    in_date: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        in_date: Union[Unset, str] = UNSET
        if not isinstance(self.in_date, Unset):
            in_date = self.in_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if in_date is not UNSET:
            field_dict["inDate"] = in_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _in_date = d.pop("inDate", UNSET)
        in_date: Union[Unset, datetime.datetime]
        if isinstance(_in_date, Unset):
            in_date = UNSET
        else:
            in_date = isoparse(_in_date)

        patch_purchase_order_in_date = cls(
            in_date=in_date,
        )

        return patch_purchase_order_in_date
