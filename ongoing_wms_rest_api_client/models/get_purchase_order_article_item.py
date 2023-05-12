import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair


T = TypeVar("T", bound="GetPurchaseOrderArticleItem")


@attr.s(auto_attribs=True)
class GetPurchaseOrderArticleItem:
    """
    Attributes:
        original_article_item_id (Union[Unset, int]):
        number_of_items (Union[Unset, float]):
        in_date (Union[Unset, datetime.datetime]):
        serial (Union[Unset, None, str]):
        case_number (Union[Unset, None, str]):
        batch_number (Union[Unset, None, str]):
        container (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
        weight (Union[Unset, None, float]):
        expiry_date (Union[Unset, None, datetime.datetime]):
        location (Union[Unset, None, str]):
        article_item_status (Union[Unset, None, CodeNamePair]):
    """

    original_article_item_id: Union[Unset, int] = UNSET
    number_of_items: Union[Unset, float] = UNSET
    in_date: Union[Unset, datetime.datetime] = UNSET
    serial: Union[Unset, None, str] = UNSET
    case_number: Union[Unset, None, str] = UNSET
    batch_number: Union[Unset, None, str] = UNSET
    container: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    weight: Union[Unset, None, float] = UNSET
    expiry_date: Union[Unset, None, datetime.datetime] = UNSET
    location: Union[Unset, None, str] = UNSET
    article_item_status: Union[Unset, None, "CodeNamePair"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        original_article_item_id = self.original_article_item_id
        number_of_items = self.number_of_items
        in_date: Union[Unset, str] = UNSET
        if not isinstance(self.in_date, Unset):
            in_date = self.in_date.isoformat()

        serial = self.serial
        case_number = self.case_number
        batch_number = self.batch_number
        container = self.container
        comment = self.comment
        weight = self.weight
        expiry_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat() if self.expiry_date else None

        location = self.location
        article_item_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_item_status, Unset):
            article_item_status = self.article_item_status.to_dict() if self.article_item_status else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if original_article_item_id is not UNSET:
            field_dict["originalArticleItemId"] = original_article_item_id
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if in_date is not UNSET:
            field_dict["inDate"] = in_date
        if serial is not UNSET:
            field_dict["serial"] = serial
        if case_number is not UNSET:
            field_dict["caseNumber"] = case_number
        if batch_number is not UNSET:
            field_dict["batchNumber"] = batch_number
        if container is not UNSET:
            field_dict["container"] = container
        if comment is not UNSET:
            field_dict["comment"] = comment
        if weight is not UNSET:
            field_dict["weight"] = weight
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if location is not UNSET:
            field_dict["location"] = location
        if article_item_status is not UNSET:
            field_dict["articleItemStatus"] = article_item_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair

        d = src_dict.copy()
        original_article_item_id = d.pop("originalArticleItemId", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        _in_date = d.pop("inDate", UNSET)
        in_date: Union[Unset, datetime.datetime]
        if isinstance(_in_date, Unset):
            in_date = UNSET
        else:
            in_date = isoparse(_in_date)

        serial = d.pop("serial", UNSET)

        case_number = d.pop("caseNumber", UNSET)

        batch_number = d.pop("batchNumber", UNSET)

        container = d.pop("container", UNSET)

        comment = d.pop("comment", UNSET)

        weight = d.pop("weight", UNSET)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, None, datetime.datetime]
        if _expiry_date is None:
            expiry_date = None
        elif isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        location = d.pop("location", UNSET)

        _article_item_status = d.pop("articleItemStatus", UNSET)
        article_item_status: Union[Unset, None, CodeNamePair]
        if _article_item_status is None:
            article_item_status = None
        elif isinstance(_article_item_status, Unset):
            article_item_status = UNSET
        else:
            article_item_status = CodeNamePair.from_dict(_article_item_status)

        get_purchase_order_article_item = cls(
            original_article_item_id=original_article_item_id,
            number_of_items=number_of_items,
            in_date=in_date,
            serial=serial,
            case_number=case_number,
            batch_number=batch_number,
            container=container,
            comment=comment,
            weight=weight,
            expiry_date=expiry_date,
            location=location,
            article_item_status=article_item_status,
        )

        return get_purchase_order_article_item
