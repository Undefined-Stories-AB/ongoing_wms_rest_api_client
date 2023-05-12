from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWayOfDeliveryTypeModel")


@attr.s(auto_attribs=True)
class GetWayOfDeliveryTypeModel:
    """
    Attributes:
        id (Union[Unset, int]):
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        code = self.code
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        get_way_of_delivery_type_model = cls(
            id=id,
            code=code,
            name=name,
        )

        return get_way_of_delivery_type_model
