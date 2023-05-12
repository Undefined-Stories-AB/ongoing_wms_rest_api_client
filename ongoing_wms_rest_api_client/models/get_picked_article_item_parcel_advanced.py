from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPickedArticleItemParcelAdvanced")


@attr.s(auto_attribs=True)
class GetPickedArticleItemParcelAdvanced:
    """
    Attributes:
        parcel_serial_number (Union[Unset, None, str]):
    """

    parcel_serial_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        parcel_serial_number = self.parcel_serial_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if parcel_serial_number is not UNSET:
            field_dict["parcelSerialNumber"] = parcel_serial_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parcel_serial_number = d.pop("parcelSerialNumber", UNSET)

        get_picked_article_item_parcel_advanced = cls(
            parcel_serial_number=parcel_serial_number,
        )

        return get_picked_article_item_parcel_advanced
