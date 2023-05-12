from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParcelTypeModel")


@attr.s(auto_attribs=True)
class ParcelTypeModel:
    """
    Attributes:
        id (Union[Unset, int]):
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        weight (Union[Unset, None, float]):
        length (Union[Unset, None, float]):
        width (Union[Unset, None, float]):
        height (Union[Unset, None, float]):
        load_meters (Union[Unset, None, float]):
        area (Union[Unset, None, float]):
        bar_code (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    weight: Union[Unset, None, float] = UNSET
    length: Union[Unset, None, float] = UNSET
    width: Union[Unset, None, float] = UNSET
    height: Union[Unset, None, float] = UNSET
    load_meters: Union[Unset, None, float] = UNSET
    area: Union[Unset, None, float] = UNSET
    bar_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        code = self.code
        name = self.name
        weight = self.weight
        length = self.length
        width = self.width
        height = self.height
        load_meters = self.load_meters
        area = self.area
        bar_code = self.bar_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if load_meters is not UNSET:
            field_dict["loadMeters"] = load_meters
        if area is not UNSET:
            field_dict["area"] = area
        if bar_code is not UNSET:
            field_dict["barCode"] = bar_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        weight = d.pop("weight", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        load_meters = d.pop("loadMeters", UNSET)

        area = d.pop("area", UNSET)

        bar_code = d.pop("barCode", UNSET)

        parcel_type_model = cls(
            id=id,
            code=code,
            name=name,
            weight=weight,
            length=length,
            width=width,
            height=height,
            load_meters=load_meters,
            area=area,
            bar_code=bar_code,
        )

        return parcel_type_model
