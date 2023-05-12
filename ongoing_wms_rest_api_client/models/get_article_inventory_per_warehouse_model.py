from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_inventory_per_warehouse_info import GetArticleInventoryPerWarehouseInfo


T = TypeVar("T", bound="GetArticleInventoryPerWarehouseModel")


@attr.s(auto_attribs=True)
class GetArticleInventoryPerWarehouseModel:
    """
    Attributes:
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        inventory_per_warehouse (Union[Unset, None, List['GetArticleInventoryPerWarehouseInfo']]):
    """

    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    inventory_per_warehouse: Union[Unset, None, List["GetArticleInventoryPerWarehouseInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_system_id = self.article_system_id
        article_number = self.article_number
        inventory_per_warehouse: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inventory_per_warehouse, Unset):
            if self.inventory_per_warehouse is None:
                inventory_per_warehouse = None
            else:
                inventory_per_warehouse = []
                for inventory_per_warehouse_item_data in self.inventory_per_warehouse:
                    inventory_per_warehouse_item = inventory_per_warehouse_item_data.to_dict()

                    inventory_per_warehouse.append(inventory_per_warehouse_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if inventory_per_warehouse is not UNSET:
            field_dict["inventoryPerWarehouse"] = inventory_per_warehouse

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_inventory_per_warehouse_info import GetArticleInventoryPerWarehouseInfo

        d = src_dict.copy()
        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        inventory_per_warehouse = []
        _inventory_per_warehouse = d.pop("inventoryPerWarehouse", UNSET)
        for inventory_per_warehouse_item_data in _inventory_per_warehouse or []:
            inventory_per_warehouse_item = GetArticleInventoryPerWarehouseInfo.from_dict(
                inventory_per_warehouse_item_data
            )

            inventory_per_warehouse.append(inventory_per_warehouse_item)

        get_article_inventory_per_warehouse_model = cls(
            article_system_id=article_system_id,
            article_number=article_number,
            inventory_per_warehouse=inventory_per_warehouse,
        )

        return get_article_inventory_per_warehouse_model
