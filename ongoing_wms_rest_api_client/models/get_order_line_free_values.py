from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderLineFreeValues")


@attr.s(auto_attribs=True)
class GetOrderLineFreeValues:
    """
    Attributes:
        free_text_1 (Union[Unset, None, str]):
    """

    free_text_1: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        free_text_1 = self.free_text_1

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if free_text_1 is not UNSET:
            field_dict["freeText1"] = free_text_1

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        free_text_1 = d.pop("freeText1", UNSET)

        get_order_line_free_values = cls(
            free_text_1=free_text_1,
        )

        return get_order_line_free_values
