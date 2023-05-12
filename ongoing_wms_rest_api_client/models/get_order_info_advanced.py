import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_back_order_info import GetOrderBackOrderInfo


T = TypeVar("T", bound="GetOrderInfoAdvanced")


@attr.s(auto_attribs=True)
class GetOrderInfoAdvanced:
    """
    Attributes:
        invoice_number (Union[Unset, None, str]):
        arrival_date (Union[Unset, None, datetime.datetime]):
        delivery_date_with_time (Union[Unset, datetime.datetime]):
        back_order_info (Union[Unset, None, GetOrderBackOrderInfo]):
    """

    invoice_number: Union[Unset, None, str] = UNSET
    arrival_date: Union[Unset, None, datetime.datetime] = UNSET
    delivery_date_with_time: Union[Unset, datetime.datetime] = UNSET
    back_order_info: Union[Unset, None, "GetOrderBackOrderInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        invoice_number = self.invoice_number
        arrival_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.arrival_date, Unset):
            arrival_date = self.arrival_date.isoformat() if self.arrival_date else None

        delivery_date_with_time: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date_with_time, Unset):
            delivery_date_with_time = self.delivery_date_with_time.isoformat()

        back_order_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.back_order_info, Unset):
            back_order_info = self.back_order_info.to_dict() if self.back_order_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if arrival_date is not UNSET:
            field_dict["arrivalDate"] = arrival_date
        if delivery_date_with_time is not UNSET:
            field_dict["deliveryDateWithTime"] = delivery_date_with_time
        if back_order_info is not UNSET:
            field_dict["backOrderInfo"] = back_order_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_order_back_order_info import GetOrderBackOrderInfo

        d = src_dict.copy()
        invoice_number = d.pop("invoiceNumber", UNSET)

        _arrival_date = d.pop("arrivalDate", UNSET)
        arrival_date: Union[Unset, None, datetime.datetime]
        if _arrival_date is None:
            arrival_date = None
        elif isinstance(_arrival_date, Unset):
            arrival_date = UNSET
        else:
            arrival_date = isoparse(_arrival_date)

        _delivery_date_with_time = d.pop("deliveryDateWithTime", UNSET)
        delivery_date_with_time: Union[Unset, datetime.datetime]
        if isinstance(_delivery_date_with_time, Unset):
            delivery_date_with_time = UNSET
        else:
            delivery_date_with_time = isoparse(_delivery_date_with_time)

        _back_order_info = d.pop("backOrderInfo", UNSET)
        back_order_info: Union[Unset, None, GetOrderBackOrderInfo]
        if _back_order_info is None:
            back_order_info = None
        elif isinstance(_back_order_info, Unset):
            back_order_info = UNSET
        else:
            back_order_info = GetOrderBackOrderInfo.from_dict(_back_order_info)

        get_order_info_advanced = cls(
            invoice_number=invoice_number,
            arrival_date=arrival_date,
            delivery_date_with_time=delivery_date_with_time,
            back_order_info=back_order_info,
        )

        return get_order_info_advanced
