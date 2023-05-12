from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostReturnCauseResponse")


@attr.s(auto_attribs=True)
class PostReturnCauseResponse:
    """
    Attributes:
        return_cause_id (Union[Unset, None, int]):
        success (Union[Unset, bool]):
        message (Union[Unset, None, str]):
    """

    return_cause_id: Union[Unset, None, int] = UNSET
    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        return_cause_id = self.return_cause_id
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if return_cause_id is not UNSET:
            field_dict["returnCauseId"] = return_cause_id
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_cause_id = d.pop("returnCauseId", UNSET)

        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        post_return_cause_response = cls(
            return_cause_id=return_cause_id,
            success=success,
            message=message,
        )

        return post_return_cause_response
