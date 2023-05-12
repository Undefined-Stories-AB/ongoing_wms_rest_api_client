from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostWayOfDeliveryTypeResponse")


@attr.s(auto_attribs=True)
class PostWayOfDeliveryTypeResponse:
    """
    Attributes:
        way_of_delivery_type_id (Union[Unset, None, int]):
        success (Union[Unset, bool]):
        message (Union[Unset, None, str]):
    """

    way_of_delivery_type_id: Union[Unset, None, int] = UNSET
    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        way_of_delivery_type_id = self.way_of_delivery_type_id
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if way_of_delivery_type_id is not UNSET:
            field_dict["wayOfDeliveryTypeId"] = way_of_delivery_type_id
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        way_of_delivery_type_id = d.pop("wayOfDeliveryTypeId", UNSET)

        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        post_way_of_delivery_type_response = cls(
            way_of_delivery_type_id=way_of_delivery_type_id,
            success=success,
            message=message,
        )

        return post_way_of_delivery_type_response
