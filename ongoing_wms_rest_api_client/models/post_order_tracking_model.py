from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PostOrderTrackingModel")


@attr.s(auto_attribs=True)
class PostOrderTrackingModel:
    """
    Attributes:
        waybill (str):
        tracking_url (str):
        is_return_tracking (bool):
    """

    waybill: str
    tracking_url: str
    is_return_tracking: bool

    def to_dict(self) -> Dict[str, Any]:
        waybill = self.waybill
        tracking_url = self.tracking_url
        is_return_tracking = self.is_return_tracking

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "waybill": waybill,
                "trackingUrl": tracking_url,
                "isReturnTracking": is_return_tracking,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        waybill = d.pop("waybill")

        tracking_url = d.pop("trackingUrl")

        is_return_tracking = d.pop("isReturnTracking")

        post_order_tracking_model = cls(
            waybill=waybill,
            tracking_url=tracking_url,
            is_return_tracking=is_return_tracking,
        )

        return post_order_tracking_model
