from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostArticleStructureRow")


@attr.s(auto_attribs=True)
class PostArticleStructureRow:
    """
    Attributes:
        article_number (str):
        number_of_items (Union[Unset, float]):
    """

    article_number: str
    number_of_items: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_number = self.article_number
        number_of_items = self.number_of_items

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "articleNumber": article_number,
            }
        )
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        article_number = d.pop("articleNumber")

        number_of_items = d.pop("numberOfItems", UNSET)

        post_article_structure_row = cls(
            article_number=article_number,
            number_of_items=number_of_items,
        )

        return post_article_structure_row
