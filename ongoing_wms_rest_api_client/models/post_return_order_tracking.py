from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostReturnOrderTracking")


@attr.s(auto_attribs=True)
class PostReturnOrderTracking:
    """
    Attributes:
        waybill (Union[Unset, None, str]):
        tracking_url (Union[Unset, None, str]):
    """

    waybill: Union[Unset, None, str] = UNSET
    tracking_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        waybill = self.waybill
        tracking_url = self.tracking_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if waybill is not UNSET:
            field_dict["waybill"] = waybill
        if tracking_url is not UNSET:
            field_dict["trackingUrl"] = tracking_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        waybill = d.pop("waybill", UNSET)

        tracking_url = d.pop("trackingUrl", UNSET)

        post_return_order_tracking = cls(
            waybill=waybill,
            tracking_url=tracking_url,
        )

        return post_return_order_tracking
