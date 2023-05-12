from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderStatusModel")


@attr.s(auto_attribs=True)
class GetOrderStatusModel:
    """
    Attributes:
        number (Union[Unset, int]):
        text (Union[Unset, None, str]):
    """

    number: Union[Unset, int] = UNSET
    text: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        text = d.pop("text", UNSET)

        get_order_status_model = cls(
            number=number,
            text=text,
        )

        return get_order_status_model
