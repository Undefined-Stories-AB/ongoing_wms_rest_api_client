from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOrderTrackingResponse")


@attr.s(auto_attribs=True)
class PostOrderTrackingResponse:
    """
    Attributes:
        success (Union[Unset, bool]):
        message (Union[Unset, None, str]):
    """

    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        post_order_tracking_response = cls(
            success=success,
            message=message,
        )

        return post_order_tracking_response
