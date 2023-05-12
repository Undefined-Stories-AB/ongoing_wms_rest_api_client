from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_way_of_delivery_type_model import GetWayOfDeliveryTypeModel


T = TypeVar("T", bound="GetWayOfDeliveryTypesModel")


@attr.s(auto_attribs=True)
class GetWayOfDeliveryTypesModel:
    """
    Attributes:
        way_of_delivery_types (Union[Unset, None, List['GetWayOfDeliveryTypeModel']]):
    """

    way_of_delivery_types: Union[Unset, None, List["GetWayOfDeliveryTypeModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        way_of_delivery_types: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.way_of_delivery_types, Unset):
            if self.way_of_delivery_types is None:
                way_of_delivery_types = None
            else:
                way_of_delivery_types = []
                for way_of_delivery_types_item_data in self.way_of_delivery_types:
                    way_of_delivery_types_item = way_of_delivery_types_item_data.to_dict()

                    way_of_delivery_types.append(way_of_delivery_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if way_of_delivery_types is not UNSET:
            field_dict["wayOfDeliveryTypes"] = way_of_delivery_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_way_of_delivery_type_model import GetWayOfDeliveryTypeModel

        d = src_dict.copy()
        way_of_delivery_types = []
        _way_of_delivery_types = d.pop("wayOfDeliveryTypes", UNSET)
        for way_of_delivery_types_item_data in _way_of_delivery_types or []:
            way_of_delivery_types_item = GetWayOfDeliveryTypeModel.from_dict(way_of_delivery_types_item_data)

            way_of_delivery_types.append(way_of_delivery_types_item)

        get_way_of_delivery_types_model = cls(
            way_of_delivery_types=way_of_delivery_types,
        )

        return get_way_of_delivery_types_model
