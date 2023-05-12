import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair


T = TypeVar("T", bound="GetReturnedArticleItem")


@attr.s(auto_attribs=True)
class GetReturnedArticleItem:
    """
    Attributes:
        number_of_items (Union[Unset, float]):
        batch (Union[Unset, None, str]):
        serial (Union[Unset, None, str]):
        expiry_date (Union[Unset, None, datetime.datetime]):
        container (Union[Unset, None, str]):
        weight (Union[Unset, None, float]):
        volume (Union[Unset, None, float]):
        comment (Union[Unset, None, str]):
        return_time (Union[Unset, None, datetime.datetime]):
        return_comment (Union[Unset, None, str]):
        is_return_removed_by_inventory (Union[Unset, bool]):
        return_cause (Union[Unset, None, CodeNamePair]):
        article_item_status (Union[Unset, None, CodeNamePair]):
        article_item_category (Union[Unset, None, CodeNamePair]):
    """

    number_of_items: Union[Unset, float] = UNSET
    batch: Union[Unset, None, str] = UNSET
    serial: Union[Unset, None, str] = UNSET
    expiry_date: Union[Unset, None, datetime.datetime] = UNSET
    container: Union[Unset, None, str] = UNSET
    weight: Union[Unset, None, float] = UNSET
    volume: Union[Unset, None, float] = UNSET
    comment: Union[Unset, None, str] = UNSET
    return_time: Union[Unset, None, datetime.datetime] = UNSET
    return_comment: Union[Unset, None, str] = UNSET
    is_return_removed_by_inventory: Union[Unset, bool] = UNSET
    return_cause: Union[Unset, None, "CodeNamePair"] = UNSET
    article_item_status: Union[Unset, None, "CodeNamePair"] = UNSET
    article_item_category: Union[Unset, None, "CodeNamePair"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number_of_items = self.number_of_items
        batch = self.batch
        serial = self.serial
        expiry_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat() if self.expiry_date else None

        container = self.container
        weight = self.weight
        volume = self.volume
        comment = self.comment
        return_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.return_time, Unset):
            return_time = self.return_time.isoformat() if self.return_time else None

        return_comment = self.return_comment
        is_return_removed_by_inventory = self.is_return_removed_by_inventory
        return_cause: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.return_cause, Unset):
            return_cause = self.return_cause.to_dict() if self.return_cause else None

        article_item_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_item_status, Unset):
            article_item_status = self.article_item_status.to_dict() if self.article_item_status else None

        article_item_category: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_item_category, Unset):
            article_item_category = self.article_item_category.to_dict() if self.article_item_category else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if batch is not UNSET:
            field_dict["batch"] = batch
        if serial is not UNSET:
            field_dict["serial"] = serial
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if container is not UNSET:
            field_dict["container"] = container
        if weight is not UNSET:
            field_dict["weight"] = weight
        if volume is not UNSET:
            field_dict["volume"] = volume
        if comment is not UNSET:
            field_dict["comment"] = comment
        if return_time is not UNSET:
            field_dict["returnTime"] = return_time
        if return_comment is not UNSET:
            field_dict["returnComment"] = return_comment
        if is_return_removed_by_inventory is not UNSET:
            field_dict["isReturnRemovedByInventory"] = is_return_removed_by_inventory
        if return_cause is not UNSET:
            field_dict["returnCause"] = return_cause
        if article_item_status is not UNSET:
            field_dict["articleItemStatus"] = article_item_status
        if article_item_category is not UNSET:
            field_dict["articleItemCategory"] = article_item_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair

        d = src_dict.copy()
        number_of_items = d.pop("numberOfItems", UNSET)

        batch = d.pop("batch", UNSET)

        serial = d.pop("serial", UNSET)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, None, datetime.datetime]
        if _expiry_date is None:
            expiry_date = None
        elif isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        container = d.pop("container", UNSET)

        weight = d.pop("weight", UNSET)

        volume = d.pop("volume", UNSET)

        comment = d.pop("comment", UNSET)

        _return_time = d.pop("returnTime", UNSET)
        return_time: Union[Unset, None, datetime.datetime]
        if _return_time is None:
            return_time = None
        elif isinstance(_return_time, Unset):
            return_time = UNSET
        else:
            return_time = isoparse(_return_time)

        return_comment = d.pop("returnComment", UNSET)

        is_return_removed_by_inventory = d.pop("isReturnRemovedByInventory", UNSET)

        _return_cause = d.pop("returnCause", UNSET)
        return_cause: Union[Unset, None, CodeNamePair]
        if _return_cause is None:
            return_cause = None
        elif isinstance(_return_cause, Unset):
            return_cause = UNSET
        else:
            return_cause = CodeNamePair.from_dict(_return_cause)

        _article_item_status = d.pop("articleItemStatus", UNSET)
        article_item_status: Union[Unset, None, CodeNamePair]
        if _article_item_status is None:
            article_item_status = None
        elif isinstance(_article_item_status, Unset):
            article_item_status = UNSET
        else:
            article_item_status = CodeNamePair.from_dict(_article_item_status)

        _article_item_category = d.pop("articleItemCategory", UNSET)
        article_item_category: Union[Unset, None, CodeNamePair]
        if _article_item_category is None:
            article_item_category = None
        elif isinstance(_article_item_category, Unset):
            article_item_category = UNSET
        else:
            article_item_category = CodeNamePair.from_dict(_article_item_category)

        get_returned_article_item = cls(
            number_of_items=number_of_items,
            batch=batch,
            serial=serial,
            expiry_date=expiry_date,
            container=container,
            weight=weight,
            volume=volume,
            comment=comment,
            return_time=return_time,
            return_comment=return_comment,
            is_return_removed_by_inventory=is_return_removed_by_inventory,
            return_cause=return_cause,
            article_item_status=article_item_status,
            article_item_category=article_item_category,
        )

        return get_returned_article_item
