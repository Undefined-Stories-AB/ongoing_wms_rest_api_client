from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostDangerousGoodsRepsonse")


@attr.s(auto_attribs=True)
class PostDangerousGoodsRepsonse:
    """
    Attributes:
        article_system_id (Union[Unset, None, int]):
        message (Union[Unset, None, str]):
    """

    article_system_id: Union[Unset, None, int] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_system_id = self.article_system_id
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        article_system_id = d.pop("articleSystemId", UNSET)

        message = d.pop("message", UNSET)

        post_dangerous_goods_repsonse = cls(
            article_system_id=article_system_id,
            message=message,
        )

        return post_dangerous_goods_repsonse
