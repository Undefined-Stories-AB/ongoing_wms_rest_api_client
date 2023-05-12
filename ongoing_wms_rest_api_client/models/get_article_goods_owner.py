from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticleGoodsOwner")


@attr.s(auto_attribs=True)
class GetArticleGoodsOwner:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        get_article_goods_owner = cls(
            id=id,
            name=name,
        )

        return get_article_goods_owner
