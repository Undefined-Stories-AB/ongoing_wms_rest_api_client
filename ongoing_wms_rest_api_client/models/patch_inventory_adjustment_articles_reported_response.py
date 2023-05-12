from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_inventory_adjustment_articles_reported_items import (
        PatchInventoryAdjustmentArticlesReportedItems,
    )


T = TypeVar("T", bound="PatchInventoryAdjustmentArticlesReportedResponse")


@attr.s(auto_attribs=True)
class PatchInventoryAdjustmentArticlesReportedResponse:
    """
    Attributes:
        message (Union[Unset, None, str]):
        items (Union[Unset, None, List['PatchInventoryAdjustmentArticlesReportedItems']]):
    """

    message: Union[Unset, None, str] = UNSET
    items: Union[Unset, None, List["PatchInventoryAdjustmentArticlesReportedItems"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
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
        if message is not UNSET:
            field_dict["message"] = message
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_inventory_adjustment_articles_reported_items import (
            PatchInventoryAdjustmentArticlesReportedItems,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = PatchInventoryAdjustmentArticlesReportedItems.from_dict(items_item_data)

            items.append(items_item)

        patch_inventory_adjustment_articles_reported_response = cls(
            message=message,
            items=items,
        )

        return patch_inventory_adjustment_articles_reported_response
