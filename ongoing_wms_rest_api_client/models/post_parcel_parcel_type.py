from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostParcelParcelType")


@attr.s(auto_attribs=True)
class PostParcelParcelType:
    """
    Attributes:
        id (Union[Unset, None, int]):
        code (Union[Unset, None, str]):
    """

    id: Union[Unset, None, int] = UNSET
    code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        code = self.code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        code = d.pop("code", UNSET)

        post_parcel_parcel_type = cls(
            id=id,
            code=code,
        )

        return post_parcel_parcel_type
