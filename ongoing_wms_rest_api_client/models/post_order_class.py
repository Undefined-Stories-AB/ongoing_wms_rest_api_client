from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOrderClass")


@attr.s(auto_attribs=True)
class PostOrderClass:
    """
    Attributes:
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
    """

    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        comment = d.pop("comment", UNSET)

        post_order_class = cls(
            code=code,
            name=name,
            comment=comment,
        )

        return post_order_class
