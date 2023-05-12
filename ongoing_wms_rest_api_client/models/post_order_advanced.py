import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_order_text_line import PostOrderTextLine


T = TypeVar("T", bound="PostOrderAdvanced")


@attr.s(auto_attribs=True)
class PostOrderAdvanced:
    """
    Attributes:
        order_text_lines (Union[Unset, None, List['PostOrderTextLine']]):
        arrival_date (Union[Unset, None, datetime.datetime]):
        way_of_delivery_string (Union[Unset, None, str]):
        transporter_order_number (Union[Unset, None, str]):
        invoice_number (Union[Unset, None, str]):
        arrival_date_from (Union[Unset, None, datetime.datetime]):
        terms_of_payment_string (Union[Unset, None, str]):
        terms_of_delivery_string (Union[Unset, None, str]):
        communication (Union[Unset, None, str]):
    """

    order_text_lines: Union[Unset, None, List["PostOrderTextLine"]] = UNSET
    arrival_date: Union[Unset, None, datetime.datetime] = UNSET
    way_of_delivery_string: Union[Unset, None, str] = UNSET
    transporter_order_number: Union[Unset, None, str] = UNSET
    invoice_number: Union[Unset, None, str] = UNSET
    arrival_date_from: Union[Unset, None, datetime.datetime] = UNSET
    terms_of_payment_string: Union[Unset, None, str] = UNSET
    terms_of_delivery_string: Union[Unset, None, str] = UNSET
    communication: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_text_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_text_lines, Unset):
            if self.order_text_lines is None:
                order_text_lines = None
            else:
                order_text_lines = []
                for order_text_lines_item_data in self.order_text_lines:
                    order_text_lines_item = order_text_lines_item_data.to_dict()

                    order_text_lines.append(order_text_lines_item)

        arrival_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.arrival_date, Unset):
            arrival_date = self.arrival_date.isoformat() if self.arrival_date else None

        way_of_delivery_string = self.way_of_delivery_string
        transporter_order_number = self.transporter_order_number
        invoice_number = self.invoice_number
        arrival_date_from: Union[Unset, None, str] = UNSET
        if not isinstance(self.arrival_date_from, Unset):
            arrival_date_from = self.arrival_date_from.isoformat() if self.arrival_date_from else None

        terms_of_payment_string = self.terms_of_payment_string
        terms_of_delivery_string = self.terms_of_delivery_string
        communication = self.communication

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_text_lines is not UNSET:
            field_dict["orderTextLines"] = order_text_lines
        if arrival_date is not UNSET:
            field_dict["arrivalDate"] = arrival_date
        if way_of_delivery_string is not UNSET:
            field_dict["wayOfDeliveryString"] = way_of_delivery_string
        if transporter_order_number is not UNSET:
            field_dict["transporterOrderNumber"] = transporter_order_number
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if arrival_date_from is not UNSET:
            field_dict["arrivalDateFrom"] = arrival_date_from
        if terms_of_payment_string is not UNSET:
            field_dict["termsOfPaymentString"] = terms_of_payment_string
        if terms_of_delivery_string is not UNSET:
            field_dict["termsOfDeliveryString"] = terms_of_delivery_string
        if communication is not UNSET:
            field_dict["communication"] = communication

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_order_text_line import PostOrderTextLine

        d = src_dict.copy()
        order_text_lines = []
        _order_text_lines = d.pop("orderTextLines", UNSET)
        for order_text_lines_item_data in _order_text_lines or []:
            order_text_lines_item = PostOrderTextLine.from_dict(order_text_lines_item_data)

            order_text_lines.append(order_text_lines_item)

        _arrival_date = d.pop("arrivalDate", UNSET)
        arrival_date: Union[Unset, None, datetime.datetime]
        if _arrival_date is None:
            arrival_date = None
        elif isinstance(_arrival_date, Unset):
            arrival_date = UNSET
        else:
            arrival_date = isoparse(_arrival_date)

        way_of_delivery_string = d.pop("wayOfDeliveryString", UNSET)

        transporter_order_number = d.pop("transporterOrderNumber", UNSET)

        invoice_number = d.pop("invoiceNumber", UNSET)

        _arrival_date_from = d.pop("arrivalDateFrom", UNSET)
        arrival_date_from: Union[Unset, None, datetime.datetime]
        if _arrival_date_from is None:
            arrival_date_from = None
        elif isinstance(_arrival_date_from, Unset):
            arrival_date_from = UNSET
        else:
            arrival_date_from = isoparse(_arrival_date_from)

        terms_of_payment_string = d.pop("termsOfPaymentString", UNSET)

        terms_of_delivery_string = d.pop("termsOfDeliveryString", UNSET)

        communication = d.pop("communication", UNSET)

        post_order_advanced = cls(
            order_text_lines=order_text_lines,
            arrival_date=arrival_date,
            way_of_delivery_string=way_of_delivery_string,
            transporter_order_number=transporter_order_number,
            invoice_number=invoice_number,
            arrival_date_from=arrival_date_from,
            terms_of_payment_string=terms_of_payment_string,
            terms_of_delivery_string=terms_of_delivery_string,
            communication=communication,
        )

        return post_order_advanced
