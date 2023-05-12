from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostArticleClassModel")


@attr.s(auto_attribs=True)
class PostArticleClassModel:
    """
    Attributes:
        goods_owner_id (int):
        code (str):
        name (str):
        comment (Union[Unset, None, str]):
    """

    goods_owner_id: int
    code: str
    name: str
    comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner_id = self.goods_owner_id
        code = self.code
        name = self.name
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "goodsOwnerId": goods_owner_id,
                "code": code,
                "name": name,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        goods_owner_id = d.pop("goodsOwnerId")

        code = d.pop("code")

        name = d.pop("name")

        comment = d.pop("comment", UNSET)

        post_article_class_model = cls(
            goods_owner_id=goods_owner_id,
            code=code,
            name=name,
            comment=comment,
        )

        return post_article_class_model
