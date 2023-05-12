from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_inventory_adjustment import GetInventoryAdjustment
    from ..models.get_inventory_adjustment_article import GetInventoryAdjustmentArticle


T = TypeVar("T", bound="GetInventoryAdjustmentsLine")


@attr.s(auto_attribs=True)
class GetInventoryAdjustmentsLine:
    """
    Attributes:
        article (Union[Unset, None, GetInventoryAdjustmentArticle]):
        inventory_adjustments (Union[Unset, None, List['GetInventoryAdjustment']]):
    """

    article: Union[Unset, None, "GetInventoryAdjustmentArticle"] = UNSET
    inventory_adjustments: Union[Unset, None, List["GetInventoryAdjustment"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict() if self.article else None

        inventory_adjustments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inventory_adjustments, Unset):
            if self.inventory_adjustments is None:
                inventory_adjustments = None
            else:
                inventory_adjustments = []
                for inventory_adjustments_item_data in self.inventory_adjustments:
                    inventory_adjustments_item = inventory_adjustments_item_data.to_dict()

                    inventory_adjustments.append(inventory_adjustments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article is not UNSET:
            field_dict["article"] = article
        if inventory_adjustments is not UNSET:
            field_dict["inventoryAdjustments"] = inventory_adjustments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_inventory_adjustment import GetInventoryAdjustment
        from ..models.get_inventory_adjustment_article import GetInventoryAdjustmentArticle

        d = src_dict.copy()
        _article = d.pop("article", UNSET)
        article: Union[Unset, None, GetInventoryAdjustmentArticle]
        if _article is None:
            article = None
        elif isinstance(_article, Unset):
            article = UNSET
        else:
            article = GetInventoryAdjustmentArticle.from_dict(_article)

        inventory_adjustments = []
        _inventory_adjustments = d.pop("inventoryAdjustments", UNSET)
        for inventory_adjustments_item_data in _inventory_adjustments or []:
            inventory_adjustments_item = GetInventoryAdjustment.from_dict(inventory_adjustments_item_data)

            inventory_adjustments.append(inventory_adjustments_item)

        get_inventory_adjustments_line = cls(
            article=article,
            inventory_adjustments=inventory_adjustments,
        )

        return get_inventory_adjustments_line
