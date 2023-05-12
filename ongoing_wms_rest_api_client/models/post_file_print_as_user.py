from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFilePrintAsUser")


@attr.s(auto_attribs=True)
class PostFilePrintAsUser:
    """
    Attributes:
        user_id (Union[Unset, None, int]):
    """

    user_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId", UNSET)

        post_file_print_as_user = cls(
            user_id=user_id,
        )

        return post_file_print_as_user
