from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_return_order_status_model import GetReturnOrderStatusModel


T = TypeVar("T", bound="GetReturnOrderStatusesModel")


@attr.s(auto_attribs=True)
class GetReturnOrderStatusesModel:
    """
    Attributes:
        return_order_statuses (Union[Unset, None, List['GetReturnOrderStatusModel']]):
    """

    return_order_statuses: Union[Unset, None, List["GetReturnOrderStatusModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        return_order_statuses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.return_order_statuses, Unset):
            if self.return_order_statuses is None:
                return_order_statuses = None
            else:
                return_order_statuses = []
                for return_order_statuses_item_data in self.return_order_statuses:
                    return_order_statuses_item = return_order_statuses_item_data.to_dict()

                    return_order_statuses.append(return_order_statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if return_order_statuses is not UNSET:
            field_dict["returnOrderStatuses"] = return_order_statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_return_order_status_model import GetReturnOrderStatusModel

        d = src_dict.copy()
        return_order_statuses = []
        _return_order_statuses = d.pop("returnOrderStatuses", UNSET)
        for return_order_statuses_item_data in _return_order_statuses or []:
            return_order_statuses_item = GetReturnOrderStatusModel.from_dict(return_order_statuses_item_data)

            return_order_statuses.append(return_order_statuses_item)

        get_return_order_statuses_model = cls(
            return_order_statuses=return_order_statuses,
        )

        return get_return_order_statuses_model
