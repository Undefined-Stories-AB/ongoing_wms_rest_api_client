import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPurchaseOrderAdvanced")


@attr.s(auto_attribs=True)
class PostPurchaseOrderAdvanced:
    """
    Attributes:
        container (Union[Unset, None, str]):
        order_date (Union[Unset, None, datetime.datetime]):
        advised_date (Union[Unset, None, datetime.datetime]):
        purchase_order_status_created (Union[Unset, None, int]):
        purchase_order_is_return_type (Union[Unset, None, bool]):
    """

    container: Union[Unset, None, str] = UNSET
    order_date: Union[Unset, None, datetime.datetime] = UNSET
    advised_date: Union[Unset, None, datetime.datetime] = UNSET
    purchase_order_status_created: Union[Unset, None, int] = UNSET
    purchase_order_is_return_type: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        container = self.container
        order_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.order_date, Unset):
            order_date = self.order_date.isoformat() if self.order_date else None

        advised_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.advised_date, Unset):
            advised_date = self.advised_date.isoformat() if self.advised_date else None

        purchase_order_status_created = self.purchase_order_status_created
        purchase_order_is_return_type = self.purchase_order_is_return_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if container is not UNSET:
            field_dict["container"] = container
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date
        if advised_date is not UNSET:
            field_dict["advisedDate"] = advised_date
        if purchase_order_status_created is not UNSET:
            field_dict["purchaseOrderStatusCreated"] = purchase_order_status_created
        if purchase_order_is_return_type is not UNSET:
            field_dict["purchaseOrderIsReturnType"] = purchase_order_is_return_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        container = d.pop("container", UNSET)

        _order_date = d.pop("orderDate", UNSET)
        order_date: Union[Unset, None, datetime.datetime]
        if _order_date is None:
            order_date = None
        elif isinstance(_order_date, Unset):
            order_date = UNSET
        else:
            order_date = isoparse(_order_date)

        _advised_date = d.pop("advisedDate", UNSET)
        advised_date: Union[Unset, None, datetime.datetime]
        if _advised_date is None:
            advised_date = None
        elif isinstance(_advised_date, Unset):
            advised_date = UNSET
        else:
            advised_date = isoparse(_advised_date)

        purchase_order_status_created = d.pop("purchaseOrderStatusCreated", UNSET)

        purchase_order_is_return_type = d.pop("purchaseOrderIsReturnType", UNSET)

        post_purchase_order_advanced = cls(
            container=container,
            order_date=order_date,
            advised_date=advised_date,
            purchase_order_status_created=purchase_order_status_created,
            purchase_order_is_return_type=purchase_order_is_return_type,
        )

        return post_purchase_order_advanced
