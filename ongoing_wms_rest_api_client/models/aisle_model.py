from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_model import LocationModel
    from ..models.position_model import PositionModel


T = TypeVar("T", bound="AisleModel")


@attr.s(auto_attribs=True)
class AisleModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        position (Union[Unset, None, PositionModel]):
        locations (Union[Unset, None, List['LocationModel']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, "PositionModel"] = UNSET
    locations: Union[Unset, None, List["LocationModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        position: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict() if self.position else None

        locations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            if self.locations is None:
                locations = None
            else:
                locations = []
                for locations_item_data in self.locations:
                    locations_item = locations_item_data.to_dict()

                    locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_model import LocationModel
        from ..models.position_model import PositionModel

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, None, PositionModel]
        if _position is None:
            position = None
        elif isinstance(_position, Unset):
            position = UNSET
        else:
            position = PositionModel.from_dict(_position)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = LocationModel.from_dict(locations_item_data)

            locations.append(locations_item)

        aisle_model = cls(
            id=id,
            name=name,
            position=position,
            locations=locations,
        )

        return aisle_model
