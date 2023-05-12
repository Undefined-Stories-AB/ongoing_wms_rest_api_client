import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_article_item_warehouse import GetArticleItemWarehouse


T = TypeVar("T", bound="GetArticleItemInfo")


@attr.s(auto_attribs=True)
class GetArticleItemInfo:
    """
    Attributes:
        batch (Union[Unset, None, str]):
        container (Union[Unset, None, str]):
        expiry_date (Union[Unset, None, datetime.datetime]):
        is_locked (Union[Unset, bool]):
        is_locked_for_sale (Union[Unset, bool]):
        location (Union[Unset, None, str]):
        number_of_items (Union[Unset, float]):
        serial (Union[Unset, None, str]):
        status (Union[Unset, None, CodeNamePair]):
        comment (Union[Unset, None, str]):
        warehouse (Union[Unset, None, GetArticleItemWarehouse]):
        in_date (Union[Unset, datetime.datetime]):
    """

    batch: Union[Unset, None, str] = UNSET
    container: Union[Unset, None, str] = UNSET
    expiry_date: Union[Unset, None, datetime.datetime] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    is_locked_for_sale: Union[Unset, bool] = UNSET
    location: Union[Unset, None, str] = UNSET
    number_of_items: Union[Unset, float] = UNSET
    serial: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, "CodeNamePair"] = UNSET
    comment: Union[Unset, None, str] = UNSET
    warehouse: Union[Unset, None, "GetArticleItemWarehouse"] = UNSET
    in_date: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        batch = self.batch
        container = self.container
        expiry_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat() if self.expiry_date else None

        is_locked = self.is_locked
        is_locked_for_sale = self.is_locked_for_sale
        location = self.location
        number_of_items = self.number_of_items
        serial = self.serial
        status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict() if self.status else None

        comment = self.comment
        warehouse: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.warehouse, Unset):
            warehouse = self.warehouse.to_dict() if self.warehouse else None

        in_date: Union[Unset, str] = UNSET
        if not isinstance(self.in_date, Unset):
            in_date = self.in_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if batch is not UNSET:
            field_dict["batch"] = batch
        if container is not UNSET:
            field_dict["container"] = container
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if is_locked_for_sale is not UNSET:
            field_dict["isLockedForSale"] = is_locked_for_sale
        if location is not UNSET:
            field_dict["location"] = location
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if serial is not UNSET:
            field_dict["serial"] = serial
        if status is not UNSET:
            field_dict["status"] = status
        if comment is not UNSET:
            field_dict["comment"] = comment
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse
        if in_date is not UNSET:
            field_dict["inDate"] = in_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_article_item_warehouse import GetArticleItemWarehouse

        d = src_dict.copy()
        batch = d.pop("batch", UNSET)

        container = d.pop("container", UNSET)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, None, datetime.datetime]
        if _expiry_date is None:
            expiry_date = None
        elif isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        is_locked = d.pop("isLocked", UNSET)

        is_locked_for_sale = d.pop("isLockedForSale", UNSET)

        location = d.pop("location", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        serial = d.pop("serial", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, CodeNamePair]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodeNamePair.from_dict(_status)

        comment = d.pop("comment", UNSET)

        _warehouse = d.pop("warehouse", UNSET)
        warehouse: Union[Unset, None, GetArticleItemWarehouse]
        if _warehouse is None:
            warehouse = None
        elif isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = GetArticleItemWarehouse.from_dict(_warehouse)

        _in_date = d.pop("inDate", UNSET)
        in_date: Union[Unset, datetime.datetime]
        if isinstance(_in_date, Unset):
            in_date = UNSET
        else:
            in_date = isoparse(_in_date)

        get_article_item_info = cls(
            batch=batch,
            container=container,
            expiry_date=expiry_date,
            is_locked=is_locked,
            is_locked_for_sale=is_locked_for_sale,
            location=location,
            number_of_items=number_of_items,
            serial=serial,
            status=status,
            comment=comment,
            warehouse=warehouse,
            in_date=in_date,
        )

        return get_article_item_info
