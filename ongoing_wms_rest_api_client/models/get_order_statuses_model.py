from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_status_model import GetOrderStatusModel


T = TypeVar("T", bound="GetOrderStatusesModel")


@attr.s(auto_attribs=True)
class GetOrderStatusesModel:
    """
    Attributes:
        order_statuses (Union[Unset, None, List['GetOrderStatusModel']]):
    """

    order_statuses: Union[Unset, None, List["GetOrderStatusModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_statuses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_statuses, Unset):
            if self.order_statuses is None:
                order_statuses = None
            else:
                order_statuses = []
                for order_statuses_item_data in self.order_statuses:
                    order_statuses_item = order_statuses_item_data.to_dict()

                    order_statuses.append(order_statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_statuses is not UNSET:
            field_dict["orderStatuses"] = order_statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_order_status_model import GetOrderStatusModel

        d = src_dict.copy()
        order_statuses = []
        _order_statuses = d.pop("orderStatuses", UNSET)
        for order_statuses_item_data in _order_statuses or []:
            order_statuses_item = GetOrderStatusModel.from_dict(order_statuses_item_data)

            order_statuses.append(order_statuses_item)

        get_order_statuses_model = cls(
            order_statuses=order_statuses,
        )

        return get_order_statuses_model
