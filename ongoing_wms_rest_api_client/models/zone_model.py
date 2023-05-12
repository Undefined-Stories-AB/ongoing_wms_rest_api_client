from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aisle_model import AisleModel
    from ..models.position_model import PositionModel


T = TypeVar("T", bound="ZoneModel")


@attr.s(auto_attribs=True)
class ZoneModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        position (Union[Unset, None, PositionModel]):
        aisles (Union[Unset, None, List['AisleModel']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, "PositionModel"] = UNSET
    aisles: Union[Unset, None, List["AisleModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        position: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict() if self.position else None

        aisles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aisles, Unset):
            if self.aisles is None:
                aisles = None
            else:
                aisles = []
                for aisles_item_data in self.aisles:
                    aisles_item = aisles_item_data.to_dict()

                    aisles.append(aisles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if aisles is not UNSET:
            field_dict["aisles"] = aisles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aisle_model import AisleModel
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

        aisles = []
        _aisles = d.pop("aisles", UNSET)
        for aisles_item_data in _aisles or []:
            aisles_item = AisleModel.from_dict(aisles_item_data)

            aisles.append(aisles_item)

        zone_model = cls(
            id=id,
            name=name,
            position=position,
            aisles=aisles,
        )

        return zone_model
