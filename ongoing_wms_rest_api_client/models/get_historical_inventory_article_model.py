from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_historical_inventory_article_item_model import GetHistoricalInventoryArticleItemModel


T = TypeVar("T", bound="GetHistoricalInventoryArticleModel")


@attr.s(auto_attribs=True)
class GetHistoricalInventoryArticleModel:
    """
    Attributes:
        article_items (Union[Unset, None, List['GetHistoricalInventoryArticleItemModel']]):
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        article_name (Union[Unset, None, str]):
        product_code (Union[Unset, None, str]):
        number_of_items (Union[Unset, float]):
    """

    article_items: Union[Unset, None, List["GetHistoricalInventoryArticleItemModel"]] = UNSET
    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    article_name: Union[Unset, None, str] = UNSET
    product_code: Union[Unset, None, str] = UNSET
    number_of_items: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.article_items, Unset):
            if self.article_items is None:
                article_items = None
            else:
                article_items = []
                for article_items_item_data in self.article_items:
                    article_items_item = article_items_item_data.to_dict()

                    article_items.append(article_items_item)

        article_system_id = self.article_system_id
        article_number = self.article_number
        article_name = self.article_name
        product_code = self.product_code
        number_of_items = self.number_of_items

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_items is not UNSET:
            field_dict["articleItems"] = article_items
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if article_name is not UNSET:
            field_dict["articleName"] = article_name
        if product_code is not UNSET:
            field_dict["productCode"] = product_code
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_historical_inventory_article_item_model import GetHistoricalInventoryArticleItemModel

        d = src_dict.copy()
        article_items = []
        _article_items = d.pop("articleItems", UNSET)
        for article_items_item_data in _article_items or []:
            article_items_item = GetHistoricalInventoryArticleItemModel.from_dict(article_items_item_data)

            article_items.append(article_items_item)

        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        article_name = d.pop("articleName", UNSET)

        product_code = d.pop("productCode", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        get_historical_inventory_article_model = cls(
            article_items=article_items,
            article_system_id=article_system_id,
            article_number=article_number,
            article_name=article_name,
            product_code=product_code,
            number_of_items=number_of_items,
        )

        return get_historical_inventory_article_model
