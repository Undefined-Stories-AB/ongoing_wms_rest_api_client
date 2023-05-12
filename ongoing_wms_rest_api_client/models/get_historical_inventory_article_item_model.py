from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetHistoricalInventoryArticleItemModel")


@attr.s(auto_attribs=True)
class GetHistoricalInventoryArticleItemModel:
    """
    Attributes:
        number_of_items (Union[Unset, float]):
        batch (Union[Unset, None, str]):
        serial (Union[Unset, None, str]):
    """

    number_of_items: Union[Unset, float] = UNSET
    batch: Union[Unset, None, str] = UNSET
    serial: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number_of_items = self.number_of_items
        batch = self.batch
        serial = self.serial

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if batch is not UNSET:
            field_dict["batch"] = batch
        if serial is not UNSET:
            field_dict["serial"] = serial

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_items = d.pop("numberOfItems", UNSET)

        batch = d.pop("batch", UNSET)

        serial = d.pop("serial", UNSET)

        get_historical_inventory_article_item_model = cls(
            number_of_items=number_of_items,
            batch=batch,
            serial=serial,
        )

        return get_historical_inventory_article_item_model
