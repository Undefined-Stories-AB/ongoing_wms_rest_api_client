import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderTracking")


@attr.s(auto_attribs=True)
class GetOrderTracking:
    """
    Attributes:
        tracking_url (Union[Unset, None, str]):
        waybill (Union[Unset, None, str]):
        created (Union[Unset, datetime.datetime]):
    """

    tracking_url: Union[Unset, None, str] = UNSET
    waybill: Union[Unset, None, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tracking_url = self.tracking_url
        waybill = self.waybill
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tracking_url is not UNSET:
            field_dict["trackingUrl"] = tracking_url
        if waybill is not UNSET:
            field_dict["waybill"] = waybill
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tracking_url = d.pop("trackingUrl", UNSET)

        waybill = d.pop("waybill", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        get_order_tracking = cls(
            tracking_url=tracking_url,
            waybill=waybill,
            created=created,
        )

        return get_order_tracking
