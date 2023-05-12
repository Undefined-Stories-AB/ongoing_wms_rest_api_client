import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.post_purchase_order_line_free_values import PostPurchaseOrderLineFreeValues


T = TypeVar("T", bound="PostPurchaseOrderLine")


@attr.s(auto_attribs=True)
class PostPurchaseOrderLine:
    """
    Attributes:
        row_number (str):
        article_number (str):
        number_of_items (Union[Unset, float]):
        comment (Union[Unset, None, str]):
        row_price (Union[Unset, None, float]):
        currency_code (Union[Unset, None, str]):
        article_item_status_id (Union[Unset, None, int]):
        batch_number (Union[Unset, None, str]):
        external_order_line_id (Union[Unset, None, str]):
        in_date (Union[Unset, None, datetime.datetime]):
        serial_number (Union[Unset, None, str]):
        expiry_date (Union[Unset, None, datetime.datetime]):
        production_date (Union[Unset, None, datetime.datetime]):
        line_free_values (Union[Unset, None, PostPurchaseOrderLineFreeValues]):
        line_type (Union[Unset, None, CodeNamePair]):
    """

    row_number: str
    article_number: str
    number_of_items: Union[Unset, float] = UNSET
    comment: Union[Unset, None, str] = UNSET
    row_price: Union[Unset, None, float] = UNSET
    currency_code: Union[Unset, None, str] = UNSET
    article_item_status_id: Union[Unset, None, int] = UNSET
    batch_number: Union[Unset, None, str] = UNSET
    external_order_line_id: Union[Unset, None, str] = UNSET
    in_date: Union[Unset, None, datetime.datetime] = UNSET
    serial_number: Union[Unset, None, str] = UNSET
    expiry_date: Union[Unset, None, datetime.datetime] = UNSET
    production_date: Union[Unset, None, datetime.datetime] = UNSET
    line_free_values: Union[Unset, None, "PostPurchaseOrderLineFreeValues"] = UNSET
    line_type: Union[Unset, None, "CodeNamePair"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        row_number = self.row_number
        article_number = self.article_number
        number_of_items = self.number_of_items
        comment = self.comment
        row_price = self.row_price
        currency_code = self.currency_code
        article_item_status_id = self.article_item_status_id
        batch_number = self.batch_number
        external_order_line_id = self.external_order_line_id
        in_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.in_date, Unset):
            in_date = self.in_date.isoformat() if self.in_date else None

        serial_number = self.serial_number
        expiry_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat() if self.expiry_date else None

        production_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.production_date, Unset):
            production_date = self.production_date.isoformat() if self.production_date else None

        line_free_values: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.line_free_values, Unset):
            line_free_values = self.line_free_values.to_dict() if self.line_free_values else None

        line_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.line_type, Unset):
            line_type = self.line_type.to_dict() if self.line_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "rowNumber": row_number,
                "articleNumber": article_number,
            }
        )
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if comment is not UNSET:
            field_dict["comment"] = comment
        if row_price is not UNSET:
            field_dict["rowPrice"] = row_price
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if article_item_status_id is not UNSET:
            field_dict["articleItemStatusId"] = article_item_status_id
        if batch_number is not UNSET:
            field_dict["batchNumber"] = batch_number
        if external_order_line_id is not UNSET:
            field_dict["externalOrderLineId"] = external_order_line_id
        if in_date is not UNSET:
            field_dict["inDate"] = in_date
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if production_date is not UNSET:
            field_dict["productionDate"] = production_date
        if line_free_values is not UNSET:
            field_dict["lineFreeValues"] = line_free_values
        if line_type is not UNSET:
            field_dict["lineType"] = line_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.post_purchase_order_line_free_values import PostPurchaseOrderLineFreeValues

        d = src_dict.copy()
        row_number = d.pop("rowNumber")

        article_number = d.pop("articleNumber")

        number_of_items = d.pop("numberOfItems", UNSET)

        comment = d.pop("comment", UNSET)

        row_price = d.pop("rowPrice", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        article_item_status_id = d.pop("articleItemStatusId", UNSET)

        batch_number = d.pop("batchNumber", UNSET)

        external_order_line_id = d.pop("externalOrderLineId", UNSET)

        _in_date = d.pop("inDate", UNSET)
        in_date: Union[Unset, None, datetime.datetime]
        if _in_date is None:
            in_date = None
        elif isinstance(_in_date, Unset):
            in_date = UNSET
        else:
            in_date = isoparse(_in_date)

        serial_number = d.pop("serialNumber", UNSET)

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

        _line_free_values = d.pop("lineFreeValues", UNSET)
        line_free_values: Union[Unset, None, PostPurchaseOrderLineFreeValues]
        if _line_free_values is None:
            line_free_values = None
        elif isinstance(_line_free_values, Unset):
            line_free_values = UNSET
        else:
            line_free_values = PostPurchaseOrderLineFreeValues.from_dict(_line_free_values)

        _line_type = d.pop("lineType", UNSET)
        line_type: Union[Unset, None, CodeNamePair]
        if _line_type is None:
            line_type = None
        elif isinstance(_line_type, Unset):
            line_type = UNSET
        else:
            line_type = CodeNamePair.from_dict(_line_type)

        post_purchase_order_line = cls(
            row_number=row_number,
            article_number=article_number,
            number_of_items=number_of_items,
            comment=comment,
            row_price=row_price,
            currency_code=currency_code,
            article_item_status_id=article_item_status_id,
            batch_number=batch_number,
            external_order_line_id=external_order_line_id,
            in_date=in_date,
            serial_number=serial_number,
            expiry_date=expiry_date,
            production_date=production_date,
            line_free_values=line_free_values,
            line_type=line_type,
        )

        return post_purchase_order_line
