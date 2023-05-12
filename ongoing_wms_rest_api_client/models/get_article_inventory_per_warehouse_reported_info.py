from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticleInventoryPerWarehouseReportedInfo")


@attr.s(auto_attribs=True)
class GetArticleInventoryPerWarehouseReportedInfo:
    """
    Attributes:
        picked_to_be_reported_number_of_items (Union[Unset, float]):
        returned_to_be_reported_number_of_items (Union[Unset, float]):
        received_to_be_reported_number_of_items (Union[Unset, float]):
    """

    picked_to_be_reported_number_of_items: Union[Unset, float] = UNSET
    returned_to_be_reported_number_of_items: Union[Unset, float] = UNSET
    received_to_be_reported_number_of_items: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        picked_to_be_reported_number_of_items = self.picked_to_be_reported_number_of_items
        returned_to_be_reported_number_of_items = self.returned_to_be_reported_number_of_items
        received_to_be_reported_number_of_items = self.received_to_be_reported_number_of_items

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if picked_to_be_reported_number_of_items is not UNSET:
            field_dict["pickedToBeReportedNumberOfItems"] = picked_to_be_reported_number_of_items
        if returned_to_be_reported_number_of_items is not UNSET:
            field_dict["returnedToBeReportedNumberOfItems"] = returned_to_be_reported_number_of_items
        if received_to_be_reported_number_of_items is not UNSET:
            field_dict["receivedToBeReportedNumberOfItems"] = received_to_be_reported_number_of_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        picked_to_be_reported_number_of_items = d.pop("pickedToBeReportedNumberOfItems", UNSET)

        returned_to_be_reported_number_of_items = d.pop("returnedToBeReportedNumberOfItems", UNSET)

        received_to_be_reported_number_of_items = d.pop("receivedToBeReportedNumberOfItems", UNSET)

        get_article_inventory_per_warehouse_reported_info = cls(
            picked_to_be_reported_number_of_items=picked_to_be_reported_number_of_items,
            returned_to_be_reported_number_of_items=returned_to_be_reported_number_of_items,
            received_to_be_reported_number_of_items=received_to_be_reported_number_of_items,
        )

        return get_article_inventory_per_warehouse_reported_info
