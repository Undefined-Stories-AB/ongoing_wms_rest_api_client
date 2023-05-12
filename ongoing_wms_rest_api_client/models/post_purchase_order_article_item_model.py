import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPurchaseOrderArticleItemModel")


@attr.s(auto_attribs=True)
class PostPurchaseOrderArticleItemModel:
    """
    Attributes:
        purchase_order_line_id (int):
        serial (Union[Unset, None, str]):
        batch (Union[Unset, None, str]):
        number_of_items (Union[Unset, None, float]):
        weight (Union[Unset, None, float]):
        length (Union[Unset, None, float]):
        width (Union[Unset, None, float]):
        height (Union[Unset, None, float]):
        volume (Union[Unset, None, float]):
        price (Union[Unset, None, float]):
        comment (Union[Unset, None, str]):
        container (Union[Unset, None, str]):
        case_number (Union[Unset, None, str]):
        status_id (Union[Unset, None, int]):
        expiry_date (Union[Unset, None, datetime.datetime]):
        production_date (Union[Unset, None, datetime.datetime]):
    """

    purchase_order_line_id: int
    serial: Union[Unset, None, str] = UNSET
    batch: Union[Unset, None, str] = UNSET
    number_of_items: Union[Unset, None, float] = UNSET
    weight: Union[Unset, None, float] = UNSET
    length: Union[Unset, None, float] = UNSET
    width: Union[Unset, None, float] = UNSET
    height: Union[Unset, None, float] = UNSET
    volume: Union[Unset, None, float] = UNSET
    price: Union[Unset, None, float] = UNSET
    comment: Union[Unset, None, str] = UNSET
    container: Union[Unset, None, str] = UNSET
    case_number: Union[Unset, None, str] = UNSET
    status_id: Union[Unset, None, int] = UNSET
    expiry_date: Union[Unset, None, datetime.datetime] = UNSET
    production_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_line_id = self.purchase_order_line_id
        serial = self.serial
        batch = self.batch
        number_of_items = self.number_of_items
        weight = self.weight
        length = self.length
        width = self.width
        height = self.height
        volume = self.volume
        price = self.price
        comment = self.comment
        container = self.container
        case_number = self.case_number
        status_id = self.status_id
        expiry_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat() if self.expiry_date else None

        production_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.production_date, Unset):
            production_date = self.production_date.isoformat() if self.production_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "purchaseOrderLineId": purchase_order_line_id,
            }
        )
        if serial is not UNSET:
            field_dict["serial"] = serial
        if batch is not UNSET:
            field_dict["batch"] = batch
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if weight is not UNSET:
            field_dict["weight"] = weight
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if volume is not UNSET:
            field_dict["volume"] = volume
        if price is not UNSET:
            field_dict["price"] = price
        if comment is not UNSET:
            field_dict["comment"] = comment
        if container is not UNSET:
            field_dict["container"] = container
        if case_number is not UNSET:
            field_dict["caseNumber"] = case_number
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if production_date is not UNSET:
            field_dict["productionDate"] = production_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        purchase_order_line_id = d.pop("purchaseOrderLineId")

        serial = d.pop("serial", UNSET)

        batch = d.pop("batch", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        weight = d.pop("weight", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        volume = d.pop("volume", UNSET)

        price = d.pop("price", UNSET)

        comment = d.pop("comment", UNSET)

        container = d.pop("container", UNSET)

        case_number = d.pop("caseNumber", UNSET)

        status_id = d.pop("statusId", UNSET)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, None, datetime.datetime]
        if _expiry_date is None:
            expiry_date = None
        elif isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        _production_date = d.pop("productionDate", UNSET)
        production_date: Union[Unset, None, datetime.datetime]
        if _production_date is None:
            production_date = None
        elif isinstance(_production_date, Unset):
            production_date = UNSET
        else:
            production_date = isoparse(_production_date)

        post_purchase_order_article_item_model = cls(
            purchase_order_line_id=purchase_order_line_id,
            serial=serial,
            batch=batch,
            number_of_items=number_of_items,
            weight=weight,
            length=length,
            width=width,
            height=height,
            volume=volume,
            price=price,
            comment=comment,
            container=container,
            case_number=case_number,
            status_id=status_id,
            expiry_date=expiry_date,
            production_date=production_date,
        )

        return post_purchase_order_article_item_model
