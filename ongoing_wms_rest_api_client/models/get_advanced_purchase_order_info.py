import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAdvancedPurchaseOrderInfo")


@attr.s(auto_attribs=True)
class GetAdvancedPurchaseOrderInfo:
    """
    Attributes:
        arrival_date (Union[Unset, None, datetime.datetime]):
        order_date (Union[Unset, None, datetime.datetime]):
        container (Union[Unset, None, str]):
        purchase_order_is_return_type (Union[Unset, bool]):
    """

    arrival_date: Union[Unset, None, datetime.datetime] = UNSET
    order_date: Union[Unset, None, datetime.datetime] = UNSET
    container: Union[Unset, None, str] = UNSET
    purchase_order_is_return_type: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        arrival_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.arrival_date, Unset):
            arrival_date = self.arrival_date.isoformat() if self.arrival_date else None

        order_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.order_date, Unset):
            order_date = self.order_date.isoformat() if self.order_date else None

        container = self.container
        purchase_order_is_return_type = self.purchase_order_is_return_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if arrival_date is not UNSET:
            field_dict["arrivalDate"] = arrival_date
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date
        if container is not UNSET:
            field_dict["container"] = container
        if purchase_order_is_return_type is not UNSET:
            field_dict["purchaseOrderIsReturnType"] = purchase_order_is_return_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _arrival_date = d.pop("arrivalDate", UNSET)
        arrival_date: Union[Unset, None, datetime.datetime]
        if _arrival_date is None:
            arrival_date = None
        elif isinstance(_arrival_date, Unset):
            arrival_date = UNSET
        else:
            arrival_date = isoparse(_arrival_date)

        _order_date = d.pop("orderDate", UNSET)
        order_date: Union[Unset, None, datetime.datetime]
        if _order_date is None:
            order_date = None
        elif isinstance(_order_date, Unset):
            order_date = UNSET
        else:
            order_date = isoparse(_order_date)

        container = d.pop("container", UNSET)

        purchase_order_is_return_type = d.pop("purchaseOrderIsReturnType", UNSET)

        get_advanced_purchase_order_info = cls(
            arrival_date=arrival_date,
            order_date=order_date,
            container=container,
            purchase_order_is_return_type=purchase_order_is_return_type,
        )

        return get_advanced_purchase_order_info
