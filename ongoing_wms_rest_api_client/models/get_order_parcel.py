from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_parcel_advanced import GetOrderParcelAdvanced
    from ..models.get_order_parcel_tracking import GetOrderParcelTracking


T = TypeVar("T", bound="GetOrderParcel")


@attr.s(auto_attribs=True)
class GetOrderParcel:
    """
    Attributes:
        id (Union[Unset, int]):
        parcel_number (Union[Unset, None, str]):
        is_return_parcel (Union[Unset, bool]):
        tracking (Union[Unset, None, GetOrderParcelTracking]):
        advanced (Union[Unset, None, GetOrderParcelAdvanced]):
    """

    id: Union[Unset, int] = UNSET
    parcel_number: Union[Unset, None, str] = UNSET
    is_return_parcel: Union[Unset, bool] = UNSET
    tracking: Union[Unset, None, "GetOrderParcelTracking"] = UNSET
    advanced: Union[Unset, None, "GetOrderParcelAdvanced"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parcel_number = self.parcel_number
        is_return_parcel = self.is_return_parcel
        tracking: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict() if self.tracking else None

        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parcel_number is not UNSET:
            field_dict["parcelNumber"] = parcel_number
        if is_return_parcel is not UNSET:
            field_dict["isReturnParcel"] = is_return_parcel
        if tracking is not UNSET:
            field_dict["tracking"] = tracking
        if advanced is not UNSET:
            field_dict["advanced"] = advanced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_order_parcel_advanced import GetOrderParcelAdvanced
        from ..models.get_order_parcel_tracking import GetOrderParcelTracking

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parcel_number = d.pop("parcelNumber", UNSET)

        is_return_parcel = d.pop("isReturnParcel", UNSET)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, None, GetOrderParcelTracking]
        if _tracking is None:
            tracking = None
        elif isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = GetOrderParcelTracking.from_dict(_tracking)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, GetOrderParcelAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = GetOrderParcelAdvanced.from_dict(_advanced)

        get_order_parcel = cls(
            id=id,
            parcel_number=parcel_number,
            is_return_parcel=is_return_parcel,
            tracking=tracking,
            advanced=advanced,
        )

        return get_order_parcel
