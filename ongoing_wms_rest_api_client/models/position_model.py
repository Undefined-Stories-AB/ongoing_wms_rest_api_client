from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionModel")


@attr.s(auto_attribs=True)
class PositionModel:
    """
    Attributes:
        x (Union[Unset, None, int]):
        y (Union[Unset, None, int]):
    """

    x: Union[Unset, None, int] = UNSET
    y: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        x = self.x
        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        position_model = cls(
            x=x,
            y=y,
        )

        return position_model
