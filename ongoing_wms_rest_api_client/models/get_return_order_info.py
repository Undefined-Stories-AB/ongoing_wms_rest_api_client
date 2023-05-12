import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_return_order_status import GetReturnOrderStatus
    from ..models.get_return_order_warehouse import GetReturnOrderWarehouse


T = TypeVar("T", bound="GetReturnOrderInfo")


@attr.s(auto_attribs=True)
class GetReturnOrderInfo:
    """
    Attributes:
        return_order_id (Union[Unset, int]):
        return_order_number (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
        in_date (Union[Unset, None, datetime.datetime]):
        return_order_status (Union[Unset, None, GetReturnOrderStatus]):
        warehouse (Union[Unset, None, GetReturnOrderWarehouse]):
        return_order_handling_comment (Union[Unset, None, str]):
    """

    return_order_id: Union[Unset, int] = UNSET
    return_order_number: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    in_date: Union[Unset, None, datetime.datetime] = UNSET
    return_order_status: Union[Unset, None, "GetReturnOrderStatus"] = UNSET
    warehouse: Union[Unset, None, "GetReturnOrderWarehouse"] = UNSET
    return_order_handling_comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        return_order_id = self.return_order_id
        return_order_number = self.return_order_number
        comment = self.comment
        in_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.in_date, Unset):
            in_date = self.in_date.isoformat() if self.in_date else None

        return_order_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.return_order_status, Unset):
            return_order_status = self.return_order_status.to_dict() if self.return_order_status else None

        warehouse: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.warehouse, Unset):
            warehouse = self.warehouse.to_dict() if self.warehouse else None

        return_order_handling_comment = self.return_order_handling_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if return_order_id is not UNSET:
            field_dict["returnOrderId"] = return_order_id
        if return_order_number is not UNSET:
            field_dict["returnOrderNumber"] = return_order_number
        if comment is not UNSET:
            field_dict["comment"] = comment
        if in_date is not UNSET:
            field_dict["inDate"] = in_date
        if return_order_status is not UNSET:
            field_dict["returnOrderStatus"] = return_order_status
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse
        if return_order_handling_comment is not UNSET:
            field_dict["returnOrderHandlingComment"] = return_order_handling_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_return_order_status import GetReturnOrderStatus
        from ..models.get_return_order_warehouse import GetReturnOrderWarehouse

        d = src_dict.copy()
        return_order_id = d.pop("returnOrderId", UNSET)

        return_order_number = d.pop("returnOrderNumber", UNSET)

        comment = d.pop("comment", UNSET)

        _in_date = d.pop("inDate", UNSET)
        in_date: Union[Unset, None, datetime.datetime]
        if _in_date is None:
            in_date = None
        elif isinstance(_in_date, Unset):
            in_date = UNSET
        else:
            in_date = isoparse(_in_date)

        _return_order_status = d.pop("returnOrderStatus", UNSET)
        return_order_status: Union[Unset, None, GetReturnOrderStatus]
        if _return_order_status is None:
            return_order_status = None
        elif isinstance(_return_order_status, Unset):
            return_order_status = UNSET
        else:
            return_order_status = GetReturnOrderStatus.from_dict(_return_order_status)

        _warehouse = d.pop("warehouse", UNSET)
        warehouse: Union[Unset, None, GetReturnOrderWarehouse]
        if _warehouse is None:
            warehouse = None
        elif isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = GetReturnOrderWarehouse.from_dict(_warehouse)

        return_order_handling_comment = d.pop("returnOrderHandlingComment", UNSET)

        get_return_order_info = cls(
            return_order_id=return_order_id,
            return_order_number=return_order_number,
            comment=comment,
            in_date=in_date,
            return_order_status=return_order_status,
            warehouse=warehouse,
            return_order_handling_comment=return_order_handling_comment,
        )

        return get_return_order_info
