from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetReturnOrderLineArticle")


@attr.s(auto_attribs=True)
class GetReturnOrderLineArticle:
    """
    Attributes:
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        article_name (Union[Unset, None, str]):
    """

    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    article_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_system_id = self.article_system_id
        article_number = self.article_number
        article_name = self.article_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if article_name is not UNSET:
            field_dict["articleName"] = article_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        article_name = d.pop("articleName", UNSET)

        get_return_order_line_article = cls(
            article_system_id=article_system_id,
            article_number=article_number,
            article_name=article_name,
        )

        return get_return_order_line_article
