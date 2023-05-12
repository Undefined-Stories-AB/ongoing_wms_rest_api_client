from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostParcelResponse")


@attr.s(auto_attribs=True)
class PostParcelResponse:
    """
    Attributes:
        parcel_id (Union[Unset, int]):
        success (Union[Unset, bool]):
        message (Union[Unset, None, str]):
    """

    parcel_id: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        parcel_id = self.parcel_id
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if parcel_id is not UNSET:
            field_dict["parcelId"] = parcel_id
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parcel_id = d.pop("parcelId", UNSET)

        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        post_parcel_response = cls(
            parcel_id=parcel_id,
            success=success,
            message=message,
        )

        return post_parcel_response
