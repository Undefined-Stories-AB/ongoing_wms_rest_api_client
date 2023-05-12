from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_return_order_customer_order_info import GetReturnOrderCustomerOrderInfo
    from ..models.get_return_order_info import GetReturnOrderInfo
    from ..models.get_return_order_line import GetReturnOrderLine


T = TypeVar("T", bound="GetReturnOrderModel")


@attr.s(auto_attribs=True)
class GetReturnOrderModel:
    """
    Attributes:
        return_order_info (Union[Unset, None, GetReturnOrderInfo]):
        customer_order_info (Union[Unset, None, GetReturnOrderCustomerOrderInfo]):
        return_order_lines (Union[Unset, None, List['GetReturnOrderLine']]):
    """

    return_order_info: Union[Unset, None, "GetReturnOrderInfo"] = UNSET
    customer_order_info: Union[Unset, None, "GetReturnOrderCustomerOrderInfo"] = UNSET
    return_order_lines: Union[Unset, None, List["GetReturnOrderLine"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        return_order_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.return_order_info, Unset):
            return_order_info = self.return_order_info.to_dict() if self.return_order_info else None

        customer_order_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_order_info, Unset):
            customer_order_info = self.customer_order_info.to_dict() if self.customer_order_info else None

        return_order_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.return_order_lines, Unset):
            if self.return_order_lines is None:
                return_order_lines = None
            else:
                return_order_lines = []
                for return_order_lines_item_data in self.return_order_lines:
                    return_order_lines_item = return_order_lines_item_data.to_dict()

                    return_order_lines.append(return_order_lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if return_order_info is not UNSET:
            field_dict["returnOrderInfo"] = return_order_info
        if customer_order_info is not UNSET:
            field_dict["customerOrderInfo"] = customer_order_info
        if return_order_lines is not UNSET:
            field_dict["returnOrderLines"] = return_order_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_return_order_customer_order_info import GetReturnOrderCustomerOrderInfo
        from ..models.get_return_order_info import GetReturnOrderInfo
        from ..models.get_return_order_line import GetReturnOrderLine

        d = src_dict.copy()
        _return_order_info = d.pop("returnOrderInfo", UNSET)
        return_order_info: Union[Unset, None, GetReturnOrderInfo]
        if _return_order_info is None:
            return_order_info = None
        elif isinstance(_return_order_info, Unset):
            return_order_info = UNSET
        else:
            return_order_info = GetReturnOrderInfo.from_dict(_return_order_info)

        _customer_order_info = d.pop("customerOrderInfo", UNSET)
        customer_order_info: Union[Unset, None, GetReturnOrderCustomerOrderInfo]
        if _customer_order_info is None:
            customer_order_info = None
        elif isinstance(_customer_order_info, Unset):
            customer_order_info = UNSET
        else:
            customer_order_info = GetReturnOrderCustomerOrderInfo.from_dict(_customer_order_info)

        return_order_lines = []
        _return_order_lines = d.pop("returnOrderLines", UNSET)
        for return_order_lines_item_data in _return_order_lines or []:
            return_order_lines_item = GetReturnOrderLine.from_dict(return_order_lines_item_data)

            return_order_lines.append(return_order_lines_item)

        get_return_order_model = cls(
            return_order_info=return_order_info,
            customer_order_info=customer_order_info,
            return_order_lines=return_order_lines,
        )

        return get_return_order_model
