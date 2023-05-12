import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_inventory_adjustment_warehouse import GetInventoryAdjustmentWarehouse


T = TypeVar("T", bound="GetInventoryAdjustment")


@attr.s(auto_attribs=True)
class GetInventoryAdjustment:
    """
    Attributes:
        inventory_id (Union[Unset, int]):
        number_of_items (Union[Unset, float]):
        inventory_time (Union[Unset, datetime.datetime]):
        article_item_comment (Union[Unset, None, str]):
        inventory_item_comment (Union[Unset, None, str]):
        inventory_adjustment_cause (Union[Unset, None, CodeNamePair]):
        location (Union[Unset, None, str]):
        batch_number (Union[Unset, None, str]):
        serial (Union[Unset, None, str]):
        article_item_status (Union[Unset, None, CodeNamePair]):
        expiry_date (Union[Unset, None, datetime.datetime]):
        warehouse (Union[Unset, None, GetInventoryAdjustmentWarehouse]):
    """

    inventory_id: Union[Unset, int] = UNSET
    number_of_items: Union[Unset, float] = UNSET
    inventory_time: Union[Unset, datetime.datetime] = UNSET
    article_item_comment: Union[Unset, None, str] = UNSET
    inventory_item_comment: Union[Unset, None, str] = UNSET
    inventory_adjustment_cause: Union[Unset, None, "CodeNamePair"] = UNSET
    location: Union[Unset, None, str] = UNSET
    batch_number: Union[Unset, None, str] = UNSET
    serial: Union[Unset, None, str] = UNSET
    article_item_status: Union[Unset, None, "CodeNamePair"] = UNSET
    expiry_date: Union[Unset, None, datetime.datetime] = UNSET
    warehouse: Union[Unset, None, "GetInventoryAdjustmentWarehouse"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        inventory_id = self.inventory_id
        number_of_items = self.number_of_items
        inventory_time: Union[Unset, str] = UNSET
        if not isinstance(self.inventory_time, Unset):
            inventory_time = self.inventory_time.isoformat()

        article_item_comment = self.article_item_comment
        inventory_item_comment = self.inventory_item_comment
        inventory_adjustment_cause: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_adjustment_cause, Unset):
            inventory_adjustment_cause = (
                self.inventory_adjustment_cause.to_dict() if self.inventory_adjustment_cause else None
            )

        location = self.location
        batch_number = self.batch_number
        serial = self.serial
        article_item_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_item_status, Unset):
            article_item_status = self.article_item_status.to_dict() if self.article_item_status else None

        expiry_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat() if self.expiry_date else None

        warehouse: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.warehouse, Unset):
            warehouse = self.warehouse.to_dict() if self.warehouse else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if inventory_id is not UNSET:
            field_dict["inventoryId"] = inventory_id
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if inventory_time is not UNSET:
            field_dict["inventoryTime"] = inventory_time
        if article_item_comment is not UNSET:
            field_dict["articleItemComment"] = article_item_comment
        if inventory_item_comment is not UNSET:
            field_dict["inventoryItemComment"] = inventory_item_comment
        if inventory_adjustment_cause is not UNSET:
            field_dict["inventoryAdjustmentCause"] = inventory_adjustment_cause
        if location is not UNSET:
            field_dict["location"] = location
        if batch_number is not UNSET:
            field_dict["batchNumber"] = batch_number
        if serial is not UNSET:
            field_dict["serial"] = serial
        if article_item_status is not UNSET:
            field_dict["articleItemStatus"] = article_item_status
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_inventory_adjustment_warehouse import GetInventoryAdjustmentWarehouse

        d = src_dict.copy()
        inventory_id = d.pop("inventoryId", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        _inventory_time = d.pop("inventoryTime", UNSET)
        inventory_time: Union[Unset, datetime.datetime]
        if isinstance(_inventory_time, Unset):
            inventory_time = UNSET
        else:
            inventory_time = isoparse(_inventory_time)

        article_item_comment = d.pop("articleItemComment", UNSET)

        inventory_item_comment = d.pop("inventoryItemComment", UNSET)

        _inventory_adjustment_cause = d.pop("inventoryAdjustmentCause", UNSET)
        inventory_adjustment_cause: Union[Unset, None, CodeNamePair]
        if _inventory_adjustment_cause is None:
            inventory_adjustment_cause = None
        elif isinstance(_inventory_adjustment_cause, Unset):
            inventory_adjustment_cause = UNSET
        else:
            inventory_adjustment_cause = CodeNamePair.from_dict(_inventory_adjustment_cause)

        location = d.pop("location", UNSET)

        batch_number = d.pop("batchNumber", UNSET)

        serial = d.pop("serial", UNSET)

        _article_item_status = d.pop("articleItemStatus", UNSET)
        article_item_status: Union[Unset, None, CodeNamePair]
        if _article_item_status is None:
            article_item_status = None
        elif isinstance(_article_item_status, Unset):
            article_item_status = UNSET
        else:
            article_item_status = CodeNamePair.from_dict(_article_item_status)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, None, datetime.datetime]
        if _expiry_date is None:
            expiry_date = None
        elif isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        _warehouse = d.pop("warehouse", UNSET)
        warehouse: Union[Unset, None, GetInventoryAdjustmentWarehouse]
        if _warehouse is None:
            warehouse = None
        elif isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = GetInventoryAdjustmentWarehouse.from_dict(_warehouse)

        get_inventory_adjustment = cls(
            inventory_id=inventory_id,
            number_of_items=number_of_items,
            inventory_time=inventory_time,
            article_item_comment=article_item_comment,
            inventory_item_comment=inventory_item_comment,
            inventory_adjustment_cause=inventory_adjustment_cause,
            location=location,
            batch_number=batch_number,
            serial=serial,
            article_item_status=article_item_status,
            expiry_date=expiry_date,
            warehouse=warehouse,
        )

        return get_inventory_adjustment
