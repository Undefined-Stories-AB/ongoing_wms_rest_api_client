from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFileResponse")


@attr.s(auto_attribs=True)
class PostFileResponse:
    """
    Attributes:
        file_id (Union[Unset, None, int]):
        success (Union[Unset, bool]):
        message (Union[Unset, None, str]):
    """

    file_id: Union[Unset, None, int] = UNSET
    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file_id = self.file_id
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_id = d.pop("fileId", UNSET)

        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        post_file_response = cls(
            file_id=file_id,
            success=success,
            message=message,
        )

        return post_file_response
