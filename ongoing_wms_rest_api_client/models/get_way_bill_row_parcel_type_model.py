from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWayBillRowParcelTypeModel")


@attr.s(auto_attribs=True)
class GetWayBillRowParcelTypeModel:
    """
    Attributes:
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        weight (Union[Unset, None, float]):
        length (Union[Unset, None, float]):
        width (Union[Unset, None, float]):
        height (Union[Unset, None, float]):
        load_meters (Union[Unset, None, float]):
        bar_code (Union[Unset, None, str]):
    """

    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    weight: Union[Unset, None, float] = UNSET
    length: Union[Unset, None, float] = UNSET
    width: Union[Unset, None, float] = UNSET
    height: Union[Unset, None, float] = UNSET
    load_meters: Union[Unset, None, float] = UNSET
    bar_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        weight = self.weight
        length = self.length
        width = self.width
        height = self.height
        load_meters = self.load_meters
        bar_code = self.bar_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
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
        if bar_code is not UNSET:
            field_dict["barCode"] = bar_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        weight = d.pop("weight", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        load_meters = d.pop("loadMeters", UNSET)

        bar_code = d.pop("barCode", UNSET)

        get_way_bill_row_parcel_type_model = cls(
            code=code,
            name=name,
            weight=weight,
            length=length,
            width=width,
            height=height,
            load_meters=load_meters,
            bar_code=bar_code,
        )

        return get_way_bill_row_parcel_type_model
