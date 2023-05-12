from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_type_model import GetOrderTypeModel


T = TypeVar("T", bound="GetOrderTypesModel")


@attr.s(auto_attribs=True)
class GetOrderTypesModel:
    """
    Attributes:
        order_types (Union[Unset, None, List['GetOrderTypeModel']]):
    """

    order_types: Union[Unset, None, List["GetOrderTypeModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_types: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_types, Unset):
            if self.order_types is None:
                order_types = None
            else:
                order_types = []
                for order_types_item_data in self.order_types:
                    order_types_item = order_types_item_data.to_dict()

                    order_types.append(order_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_types is not UNSET:
            field_dict["orderTypes"] = order_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_order_type_model import GetOrderTypeModel

        d = src_dict.copy()
        order_types = []
        _order_types = d.pop("orderTypes", UNSET)
        for order_types_item_data in _order_types or []:
            order_types_item = GetOrderTypeModel.from_dict(order_types_item_data)

            order_types.append(order_types_item)

        get_order_types_model = cls(
            order_types=order_types,
        )

        return get_order_types_model
