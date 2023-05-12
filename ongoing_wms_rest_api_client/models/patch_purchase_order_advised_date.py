import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchPurchaseOrderAdvisedDate")


@attr.s(auto_attribs=True)
class PatchPurchaseOrderAdvisedDate:
    """
    Attributes:
        advised_date (Union[Unset, None, datetime.datetime]):
    """

    advised_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        advised_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.advised_date, Unset):
            advised_date = self.advised_date.isoformat() if self.advised_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if advised_date is not UNSET:
            field_dict["advisedDate"] = advised_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _advised_date = d.pop("advisedDate", UNSET)
        advised_date: Union[Unset, None, datetime.datetime]
        if _advised_date is None:
            advised_date = None
        elif isinstance(_advised_date, Unset):
            advised_date = UNSET
        else:
            advised_date = isoparse(_advised_date)

        patch_purchase_order_advised_date = cls(
            advised_date=advised_date,
        )

        return patch_purchase_order_advised_date
