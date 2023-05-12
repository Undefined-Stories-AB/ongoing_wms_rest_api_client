from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticleStructureRowInfoModel")


@attr.s(auto_attribs=True)
class GetArticleStructureRowInfoModel:
    """
    Attributes:
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        number_of_items (Union[Unset, None, float]):
    """

    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    number_of_items: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_system_id = self.article_system_id
        article_number = self.article_number
        number_of_items = self.number_of_items

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        get_article_structure_row_info_model = cls(
            article_system_id=article_system_id,
            article_number=article_number,
            number_of_items=number_of_items,
        )

        return get_article_structure_row_info_model
