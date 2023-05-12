import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_return_order_customer_order import PostReturnOrderCustomerOrder
    from ..models.post_return_order_line import PostReturnOrderLine
    from ..models.post_return_order_tracking import PostReturnOrderTracking


T = TypeVar("T", bound="PostReturnOrderModel")


@attr.s(auto_attribs=True)
class PostReturnOrderModel:
    """
    Attributes:
        goods_owner_id (int):
        return_order_number (str):
        customer_order (PostReturnOrderCustomerOrder):
        return_order_lines (List['PostReturnOrderLine']):
        comment (Union[Unset, None, str]):
        in_date (Union[Unset, None, datetime.datetime]):
        warehouse_id (Union[Unset, None, int]):
        tracking (Union[Unset, None, List['PostReturnOrderTracking']]):
        return_order_handling_comment (Union[Unset, None, str]):
    """

    goods_owner_id: int
    return_order_number: str
    customer_order: "PostReturnOrderCustomerOrder"
    return_order_lines: List["PostReturnOrderLine"]
    comment: Union[Unset, None, str] = UNSET
    in_date: Union[Unset, None, datetime.datetime] = UNSET
    warehouse_id: Union[Unset, None, int] = UNSET
    tracking: Union[Unset, None, List["PostReturnOrderTracking"]] = UNSET
    return_order_handling_comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner_id = self.goods_owner_id
        return_order_number = self.return_order_number
        customer_order = self.customer_order.to_dict()

        return_order_lines = []
        for return_order_lines_item_data in self.return_order_lines:
            return_order_lines_item = return_order_lines_item_data.to_dict()

            return_order_lines.append(return_order_lines_item)

        comment = self.comment
        in_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.in_date, Unset):
            in_date = self.in_date.isoformat() if self.in_date else None

        warehouse_id = self.warehouse_id
        tracking: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking, Unset):
            if self.tracking is None:
                tracking = None
            else:
                tracking = []
                for tracking_item_data in self.tracking:
                    tracking_item = tracking_item_data.to_dict()

                    tracking.append(tracking_item)

        return_order_handling_comment = self.return_order_handling_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "goodsOwnerId": goods_owner_id,
                "returnOrderNumber": return_order_number,
                "customerOrder": customer_order,
                "returnOrderLines": return_order_lines,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if in_date is not UNSET:
            field_dict["inDate"] = in_date
        if warehouse_id is not UNSET:
            field_dict["warehouseId"] = warehouse_id
        if tracking is not UNSET:
            field_dict["tracking"] = tracking
        if return_order_handling_comment is not UNSET:
            field_dict["returnOrderHandlingComment"] = return_order_handling_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_return_order_customer_order import PostReturnOrderCustomerOrder
        from ..models.post_return_order_line import PostReturnOrderLine
        from ..models.post_return_order_tracking import PostReturnOrderTracking

        d = src_dict.copy()
        goods_owner_id = d.pop("goodsOwnerId")

        return_order_number = d.pop("returnOrderNumber")

        customer_order = PostReturnOrderCustomerOrder.from_dict(d.pop("customerOrder"))

        return_order_lines = []
        _return_order_lines = d.pop("returnOrderLines")
        for return_order_lines_item_data in _return_order_lines:
            return_order_lines_item = PostReturnOrderLine.from_dict(return_order_lines_item_data)

            return_order_lines.append(return_order_lines_item)

        comment = d.pop("comment", UNSET)

        _in_date = d.pop("inDate", UNSET)
        in_date: Union[Unset, None, datetime.datetime]
        if _in_date is None:
            in_date = None
        elif isinstance(_in_date, Unset):
            in_date = UNSET
        else:
            in_date = isoparse(_in_date)

        warehouse_id = d.pop("warehouseId", UNSET)

        tracking = []
        _tracking = d.pop("tracking", UNSET)
        for tracking_item_data in _tracking or []:
            tracking_item = PostReturnOrderTracking.from_dict(tracking_item_data)

            tracking.append(tracking_item)

        return_order_handling_comment = d.pop("returnOrderHandlingComment", UNSET)

        post_return_order_model = cls(
            goods_owner_id=goods_owner_id,
            return_order_number=return_order_number,
            customer_order=customer_order,
            return_order_lines=return_order_lines,
            comment=comment,
            in_date=in_date,
            warehouse_id=warehouse_id,
            tracking=tracking,
            return_order_handling_comment=return_order_handling_comment,
        )

        return post_return_order_model
