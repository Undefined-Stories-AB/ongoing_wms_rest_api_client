import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticleInventoryInfo")


@attr.s(auto_attribs=True)
class GetArticleInventoryInfo:
    """
    Attributes:
        number_of_items (Union[Unset, float]):
        number_of_booked_items (Union[Unset, float]):
        number_of_locked_items (Union[Unset, float]):
        to_receive_number_of_items (Union[Unset, float]):
        allocated_number_of_items (Union[Unset, float]):
        locked_for_sale_number_of_items (Union[Unset, float]):
        picked_to_be_collected_number_of_items (Union[Unset, float]):
        received_to_be_finished_number_of_items (Union[Unset, float]):
        last_in_date (Union[Unset, None, datetime.datetime]):
        sellable_number_of_items (Union[Unset, float]):
        total_stock_value (Union[Unset, float]):
    """

    number_of_items: Union[Unset, float] = UNSET
    number_of_booked_items: Union[Unset, float] = UNSET
    number_of_locked_items: Union[Unset, float] = UNSET
    to_receive_number_of_items: Union[Unset, float] = UNSET
    allocated_number_of_items: Union[Unset, float] = UNSET
    locked_for_sale_number_of_items: Union[Unset, float] = UNSET
    picked_to_be_collected_number_of_items: Union[Unset, float] = UNSET
    received_to_be_finished_number_of_items: Union[Unset, float] = UNSET
    last_in_date: Union[Unset, None, datetime.datetime] = UNSET
    sellable_number_of_items: Union[Unset, float] = UNSET
    total_stock_value: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number_of_items = self.number_of_items
        number_of_booked_items = self.number_of_booked_items
        number_of_locked_items = self.number_of_locked_items
        to_receive_number_of_items = self.to_receive_number_of_items
        allocated_number_of_items = self.allocated_number_of_items
        locked_for_sale_number_of_items = self.locked_for_sale_number_of_items
        picked_to_be_collected_number_of_items = self.picked_to_be_collected_number_of_items
        received_to_be_finished_number_of_items = self.received_to_be_finished_number_of_items
        last_in_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_in_date, Unset):
            last_in_date = self.last_in_date.isoformat() if self.last_in_date else None

        sellable_number_of_items = self.sellable_number_of_items
        total_stock_value = self.total_stock_value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if number_of_booked_items is not UNSET:
            field_dict["numberOfBookedItems"] = number_of_booked_items
        if number_of_locked_items is not UNSET:
            field_dict["numberOfLockedItems"] = number_of_locked_items
        if to_receive_number_of_items is not UNSET:
            field_dict["toReceiveNumberOfItems"] = to_receive_number_of_items
        if allocated_number_of_items is not UNSET:
            field_dict["allocatedNumberOfItems"] = allocated_number_of_items
        if locked_for_sale_number_of_items is not UNSET:
            field_dict["lockedForSaleNumberOfItems"] = locked_for_sale_number_of_items
        if picked_to_be_collected_number_of_items is not UNSET:
            field_dict["pickedToBeCollectedNumberOfItems"] = picked_to_be_collected_number_of_items
        if received_to_be_finished_number_of_items is not UNSET:
            field_dict["receivedToBeFinishedNumberOfItems"] = received_to_be_finished_number_of_items
        if last_in_date is not UNSET:
            field_dict["lastInDate"] = last_in_date
        if sellable_number_of_items is not UNSET:
            field_dict["sellableNumberOfItems"] = sellable_number_of_items
        if total_stock_value is not UNSET:
            field_dict["totalStockValue"] = total_stock_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_items = d.pop("numberOfItems", UNSET)

        number_of_booked_items = d.pop("numberOfBookedItems", UNSET)

        number_of_locked_items = d.pop("numberOfLockedItems", UNSET)

        to_receive_number_of_items = d.pop("toReceiveNumberOfItems", UNSET)

        allocated_number_of_items = d.pop("allocatedNumberOfItems", UNSET)

        locked_for_sale_number_of_items = d.pop("lockedForSaleNumberOfItems", UNSET)

        picked_to_be_collected_number_of_items = d.pop("pickedToBeCollectedNumberOfItems", UNSET)

        received_to_be_finished_number_of_items = d.pop("receivedToBeFinishedNumberOfItems", UNSET)

        _last_in_date = d.pop("lastInDate", UNSET)
        last_in_date: Union[Unset, None, datetime.datetime]
        if _last_in_date is None:
            last_in_date = None
        elif isinstance(_last_in_date, Unset):
            last_in_date = UNSET
        else:
            last_in_date = isoparse(_last_in_date)

        sellable_number_of_items = d.pop("sellableNumberOfItems", UNSET)

        total_stock_value = d.pop("totalStockValue", UNSET)

        get_article_inventory_info = cls(
            number_of_items=number_of_items,
            number_of_booked_items=number_of_booked_items,
            number_of_locked_items=number_of_locked_items,
            to_receive_number_of_items=to_receive_number_of_items,
            allocated_number_of_items=allocated_number_of_items,
            locked_for_sale_number_of_items=locked_for_sale_number_of_items,
            picked_to_be_collected_number_of_items=picked_to_be_collected_number_of_items,
            received_to_be_finished_number_of_items=received_to_be_finished_number_of_items,
            last_in_date=last_in_date,
            sellable_number_of_items=sellable_number_of_items,
            total_stock_value=total_stock_value,
        )

        return get_article_inventory_info
