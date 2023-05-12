import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_picked_article_item_handling import GetPickedArticleItemHandling
    from ..models.get_picked_article_item_parcel import GetPickedArticleItemParcel


T = TypeVar("T", bound="GetOrderPickedArticleItem")


@attr.s(auto_attribs=True)
class GetOrderPickedArticleItem:
    """
    Attributes:
        article_item_id (Union[Unset, int]):
        number_of_items (Union[Unset, float]):
        in_date (Union[Unset, datetime.datetime]):
        serial (Union[Unset, None, str]):
        case_number (Union[Unset, None, str]):
        batch_number (Union[Unset, None, str]):
        container (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
        weight (Union[Unset, None, float]):
        volume (Union[Unset, None, float]):
        is_picked (Union[Unset, bool]):
        is_returned (Union[Unset, bool]):
        expiry_date (Union[Unset, None, datetime.datetime]):
        return_date (Union[Unset, None, datetime.datetime]):
        picked_time (Union[Unset, None, datetime.datetime]):
        return_cause (Union[Unset, None, CodeNamePair]):
        location (Union[Unset, None, str]):
        location_type_code (Union[Unset, None, str]):
        article_item_status (Union[Unset, None, CodeNamePair]):
        free_text_1 (Union[Unset, None, str]):
        packed_time (Union[Unset, None, datetime.datetime]):
        handling (Union[Unset, None, GetPickedArticleItemHandling]):
        parcel (Union[Unset, None, GetPickedArticleItemParcel]):
        zone_name (Union[Unset, None, str]):
    """

    article_item_id: Union[Unset, int] = UNSET
    number_of_items: Union[Unset, float] = UNSET
    in_date: Union[Unset, datetime.datetime] = UNSET
    serial: Union[Unset, None, str] = UNSET
    case_number: Union[Unset, None, str] = UNSET
    batch_number: Union[Unset, None, str] = UNSET
    container: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    weight: Union[Unset, None, float] = UNSET
    volume: Union[Unset, None, float] = UNSET
    is_picked: Union[Unset, bool] = UNSET
    is_returned: Union[Unset, bool] = UNSET
    expiry_date: Union[Unset, None, datetime.datetime] = UNSET
    return_date: Union[Unset, None, datetime.datetime] = UNSET
    picked_time: Union[Unset, None, datetime.datetime] = UNSET
    return_cause: Union[Unset, None, "CodeNamePair"] = UNSET
    location: Union[Unset, None, str] = UNSET
    location_type_code: Union[Unset, None, str] = UNSET
    article_item_status: Union[Unset, None, "CodeNamePair"] = UNSET
    free_text_1: Union[Unset, None, str] = UNSET
    packed_time: Union[Unset, None, datetime.datetime] = UNSET
    handling: Union[Unset, None, "GetPickedArticleItemHandling"] = UNSET
    parcel: Union[Unset, None, "GetPickedArticleItemParcel"] = UNSET
    zone_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_item_id = self.article_item_id
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
        volume = self.volume
        is_picked = self.is_picked
        is_returned = self.is_returned
        expiry_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat() if self.expiry_date else None

        return_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.return_date, Unset):
            return_date = self.return_date.isoformat() if self.return_date else None

        picked_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.picked_time, Unset):
            picked_time = self.picked_time.isoformat() if self.picked_time else None

        return_cause: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.return_cause, Unset):
            return_cause = self.return_cause.to_dict() if self.return_cause else None

        location = self.location
        location_type_code = self.location_type_code
        article_item_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_item_status, Unset):
            article_item_status = self.article_item_status.to_dict() if self.article_item_status else None

        free_text_1 = self.free_text_1
        packed_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.packed_time, Unset):
            packed_time = self.packed_time.isoformat() if self.packed_time else None

        handling: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.handling, Unset):
            handling = self.handling.to_dict() if self.handling else None

        parcel: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parcel, Unset):
            parcel = self.parcel.to_dict() if self.parcel else None

        zone_name = self.zone_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_item_id is not UNSET:
            field_dict["articleItemId"] = article_item_id
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
        if volume is not UNSET:
            field_dict["volume"] = volume
        if is_picked is not UNSET:
            field_dict["isPicked"] = is_picked
        if is_returned is not UNSET:
            field_dict["isReturned"] = is_returned
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if return_date is not UNSET:
            field_dict["returnDate"] = return_date
        if picked_time is not UNSET:
            field_dict["pickedTime"] = picked_time
        if return_cause is not UNSET:
            field_dict["returnCause"] = return_cause
        if location is not UNSET:
            field_dict["location"] = location
        if location_type_code is not UNSET:
            field_dict["locationTypeCode"] = location_type_code
        if article_item_status is not UNSET:
            field_dict["articleItemStatus"] = article_item_status
        if free_text_1 is not UNSET:
            field_dict["freeText1"] = free_text_1
        if packed_time is not UNSET:
            field_dict["packedTime"] = packed_time
        if handling is not UNSET:
            field_dict["handling"] = handling
        if parcel is not UNSET:
            field_dict["parcel"] = parcel
        if zone_name is not UNSET:
            field_dict["zoneName"] = zone_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_picked_article_item_handling import GetPickedArticleItemHandling
        from ..models.get_picked_article_item_parcel import GetPickedArticleItemParcel

        d = src_dict.copy()
        article_item_id = d.pop("articleItemId", UNSET)

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

        volume = d.pop("volume", UNSET)

        is_picked = d.pop("isPicked", UNSET)

        is_returned = d.pop("isReturned", UNSET)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, None, datetime.datetime]
        if _expiry_date is None:
            expiry_date = None
        elif isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        _return_date = d.pop("returnDate", UNSET)
        return_date: Union[Unset, None, datetime.datetime]
        if _return_date is None:
            return_date = None
        elif isinstance(_return_date, Unset):
            return_date = UNSET
        else:
            return_date = isoparse(_return_date)

        _picked_time = d.pop("pickedTime", UNSET)
        picked_time: Union[Unset, None, datetime.datetime]
        if _picked_time is None:
            picked_time = None
        elif isinstance(_picked_time, Unset):
            picked_time = UNSET
        else:
            picked_time = isoparse(_picked_time)

        _return_cause = d.pop("returnCause", UNSET)
        return_cause: Union[Unset, None, CodeNamePair]
        if _return_cause is None:
            return_cause = None
        elif isinstance(_return_cause, Unset):
            return_cause = UNSET
        else:
            return_cause = CodeNamePair.from_dict(_return_cause)

        location = d.pop("location", UNSET)

        location_type_code = d.pop("locationTypeCode", UNSET)

        _article_item_status = d.pop("articleItemStatus", UNSET)
        article_item_status: Union[Unset, None, CodeNamePair]
        if _article_item_status is None:
            article_item_status = None
        elif isinstance(_article_item_status, Unset):
            article_item_status = UNSET
        else:
            article_item_status = CodeNamePair.from_dict(_article_item_status)

        free_text_1 = d.pop("freeText1", UNSET)

        _packed_time = d.pop("packedTime", UNSET)
        packed_time: Union[Unset, None, datetime.datetime]
        if _packed_time is None:
            packed_time = None
        elif isinstance(_packed_time, Unset):
            packed_time = UNSET
        else:
            packed_time = isoparse(_packed_time)

        _handling = d.pop("handling", UNSET)
        handling: Union[Unset, None, GetPickedArticleItemHandling]
        if _handling is None:
            handling = None
        elif isinstance(_handling, Unset):
            handling = UNSET
        else:
            handling = GetPickedArticleItemHandling.from_dict(_handling)

        _parcel = d.pop("parcel", UNSET)
        parcel: Union[Unset, None, GetPickedArticleItemParcel]
        if _parcel is None:
            parcel = None
        elif isinstance(_parcel, Unset):
            parcel = UNSET
        else:
            parcel = GetPickedArticleItemParcel.from_dict(_parcel)

        zone_name = d.pop("zoneName", UNSET)

        get_order_picked_article_item = cls(
            article_item_id=article_item_id,
            number_of_items=number_of_items,
            in_date=in_date,
            serial=serial,
            case_number=case_number,
            batch_number=batch_number,
            container=container,
            comment=comment,
            weight=weight,
            volume=volume,
            is_picked=is_picked,
            is_returned=is_returned,
            expiry_date=expiry_date,
            return_date=return_date,
            picked_time=picked_time,
            return_cause=return_cause,
            location=location,
            location_type_code=location_type_code,
            article_item_status=article_item_status,
            free_text_1=free_text_1,
            packed_time=packed_time,
            handling=handling,
            parcel=parcel,
            zone_name=zone_name,
        )

        return get_order_picked_article_item
