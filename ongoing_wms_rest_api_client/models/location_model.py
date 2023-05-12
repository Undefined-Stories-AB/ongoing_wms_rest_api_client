from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_position_model import LocationPositionModel


T = TypeVar("T", bound="LocationModel")


@attr.s(auto_attribs=True)
class LocationModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        barcode (Union[Unset, None, str]):
        position (Union[Unset, None, LocationPositionModel]):
        location_type_id (Union[Unset, None, int]):
        picking_priority (Union[Unset, int]):
        is_picking_location (Union[Unset, bool]):
        is_locked (Union[Unset, bool]):
        is_locked_for_sale (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    barcode: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, "LocationPositionModel"] = UNSET
    location_type_id: Union[Unset, None, int] = UNSET
    picking_priority: Union[Unset, int] = UNSET
    is_picking_location: Union[Unset, bool] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    is_locked_for_sale: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        barcode = self.barcode
        position: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict() if self.position else None

        location_type_id = self.location_type_id
        picking_priority = self.picking_priority
        is_picking_location = self.is_picking_location
        is_locked = self.is_locked
        is_locked_for_sale = self.is_locked_for_sale

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if position is not UNSET:
            field_dict["position"] = position
        if location_type_id is not UNSET:
            field_dict["locationTypeId"] = location_type_id
        if picking_priority is not UNSET:
            field_dict["pickingPriority"] = picking_priority
        if is_picking_location is not UNSET:
            field_dict["isPickingLocation"] = is_picking_location
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if is_locked_for_sale is not UNSET:
            field_dict["isLockedForSale"] = is_locked_for_sale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_position_model import LocationPositionModel

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        barcode = d.pop("barcode", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, None, LocationPositionModel]
        if _position is None:
            position = None
        elif isinstance(_position, Unset):
            position = UNSET
        else:
            position = LocationPositionModel.from_dict(_position)

        location_type_id = d.pop("locationTypeId", UNSET)

        picking_priority = d.pop("pickingPriority", UNSET)

        is_picking_location = d.pop("isPickingLocation", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        is_locked_for_sale = d.pop("isLockedForSale", UNSET)

        location_model = cls(
            id=id,
            name=name,
            barcode=barcode,
            position=position,
            location_type_id=location_type_id,
            picking_priority=picking_priority,
            is_picking_location=is_picking_location,
            is_locked=is_locked,
            is_locked_for_sale=is_locked_for_sale,
        )

        return location_model
