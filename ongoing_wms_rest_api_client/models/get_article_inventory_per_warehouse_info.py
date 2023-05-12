from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_inventory_per_warehouse_reported_info import GetArticleInventoryPerWarehouseReportedInfo


T = TypeVar("T", bound="GetArticleInventoryPerWarehouseInfo")


@attr.s(auto_attribs=True)
class GetArticleInventoryPerWarehouseInfo:
    """
    Attributes:
        warehouse_id (Union[Unset, int]):
        number_of_items (Union[Unset, float]):
        number_of_locked_items (Union[Unset, float]):
        sellable_number_of_items (Union[Unset, float]):
        available_for_sale_number_of_items (Union[Unset, float]):
        reported (Union[Unset, None, GetArticleInventoryPerWarehouseReportedInfo]):
    """

    warehouse_id: Union[Unset, int] = UNSET
    number_of_items: Union[Unset, float] = UNSET
    number_of_locked_items: Union[Unset, float] = UNSET
    sellable_number_of_items: Union[Unset, float] = UNSET
    available_for_sale_number_of_items: Union[Unset, float] = UNSET
    reported: Union[Unset, None, "GetArticleInventoryPerWarehouseReportedInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        warehouse_id = self.warehouse_id
        number_of_items = self.number_of_items
        number_of_locked_items = self.number_of_locked_items
        sellable_number_of_items = self.sellable_number_of_items
        available_for_sale_number_of_items = self.available_for_sale_number_of_items
        reported: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.reported, Unset):
            reported = self.reported.to_dict() if self.reported else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if warehouse_id is not UNSET:
            field_dict["warehouseId"] = warehouse_id
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if number_of_locked_items is not UNSET:
            field_dict["numberOfLockedItems"] = number_of_locked_items
        if sellable_number_of_items is not UNSET:
            field_dict["sellableNumberOfItems"] = sellable_number_of_items
        if available_for_sale_number_of_items is not UNSET:
            field_dict["availableForSaleNumberOfItems"] = available_for_sale_number_of_items
        if reported is not UNSET:
            field_dict["reported"] = reported

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_inventory_per_warehouse_reported_info import (
            GetArticleInventoryPerWarehouseReportedInfo,
        )

        d = src_dict.copy()
        warehouse_id = d.pop("warehouseId", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        number_of_locked_items = d.pop("numberOfLockedItems", UNSET)

        sellable_number_of_items = d.pop("sellableNumberOfItems", UNSET)

        available_for_sale_number_of_items = d.pop("availableForSaleNumberOfItems", UNSET)

        _reported = d.pop("reported", UNSET)
        reported: Union[Unset, None, GetArticleInventoryPerWarehouseReportedInfo]
        if _reported is None:
            reported = None
        elif isinstance(_reported, Unset):
            reported = UNSET
        else:
            reported = GetArticleInventoryPerWarehouseReportedInfo.from_dict(_reported)

        get_article_inventory_per_warehouse_info = cls(
            warehouse_id=warehouse_id,
            number_of_items=number_of_items,
            number_of_locked_items=number_of_locked_items,
            sellable_number_of_items=sellable_number_of_items,
            available_for_sale_number_of_items=available_for_sale_number_of_items,
            reported=reported,
        )

        return get_article_inventory_per_warehouse_info
