from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_item_info import GetArticleItemInfo


T = TypeVar("T", bound="GetArticleItemsModel")


@attr.s(auto_attribs=True)
class GetArticleItemsModel:
    """
    Attributes:
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        items (Union[Unset, None, List['GetArticleItemInfo']]):
    """

    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    items: Union[Unset, None, List["GetArticleItemInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_system_id = self.article_system_id
        article_number = self.article_number
        items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = []
                for items_item_data in self.items:
                    items_item = items_item_data.to_dict()

                    items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_item_info import GetArticleItemInfo

        d = src_dict.copy()
        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = GetArticleItemInfo.from_dict(items_item_data)

            items.append(items_item)

        get_article_items_model = cls(
            article_system_id=article_system_id,
            article_number=article_number,
            items=items,
        )

        return get_article_items_model
