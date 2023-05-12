from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchInventoryAdjustmentArticlesReportedItems")


@attr.s(auto_attribs=True)
class PatchInventoryAdjustmentArticlesReportedItems:
    """
    Attributes:
        inventory_article_item_id (Union[Unset, int]):
        article_item_id (Union[Unset, int]):
    """

    inventory_article_item_id: Union[Unset, int] = UNSET
    article_item_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        inventory_article_item_id = self.inventory_article_item_id
        article_item_id = self.article_item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if inventory_article_item_id is not UNSET:
            field_dict["inventoryArticleItemId"] = inventory_article_item_id
        if article_item_id is not UNSET:
            field_dict["articleItemId"] = article_item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        inventory_article_item_id = d.pop("inventoryArticleItemId", UNSET)

        article_item_id = d.pop("articleItemId", UNSET)

        patch_inventory_adjustment_articles_reported_items = cls(
            inventory_article_item_id=inventory_article_item_id,
            article_item_id=article_item_id,
        )

        return patch_inventory_adjustment_articles_reported_items
