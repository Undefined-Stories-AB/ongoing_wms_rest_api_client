from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchOrderNumberModel")


@attr.s(auto_attribs=True)
class PatchOrderNumberModel:
    """
    Attributes:
        order_number (str):
    """

    order_number: str

    def to_dict(self) -> Dict[str, Any]:
        order_number = self.order_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "orderNumber": order_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_number = d.pop("orderNumber")

        patch_order_number_model = cls(
            order_number=order_number,
        )

        return patch_order_number_model
