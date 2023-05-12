from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderParcelTracking")


@attr.s(auto_attribs=True)
class GetOrderParcelTracking:
    """
    Attributes:
        tracking_url (Union[Unset, None, str]):
    """

    tracking_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tracking_url = self.tracking_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tracking_url is not UNSET:
            field_dict["trackingUrl"] = tracking_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tracking_url = d.pop("trackingUrl", UNSET)

        get_order_parcel_tracking = cls(
            tracking_url=tracking_url,
        )

        return get_order_parcel_tracking
