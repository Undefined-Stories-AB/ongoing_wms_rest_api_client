from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPickedArticleItemParcelType")


@attr.s(auto_attribs=True)
class GetPickedArticleItemParcelType:
    """
    Attributes:
        code (Union[Unset, None, str]):
    """

    code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        get_picked_article_item_parcel_type = cls(
            code=code,
        )

        return get_picked_article_item_parcel_type
