from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchOrderStatus")


@attr.s(auto_attribs=True)
class PatchOrderStatus:
    """
    Attributes:
        order_status_number (int):
    """

    order_status_number: int

    def to_dict(self) -> Dict[str, Any]:
        order_status_number = self.order_status_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "orderStatusNumber": order_status_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_status_number = d.pop("orderStatusNumber")

        patch_order_status = cls(
            order_status_number=order_status_number,
        )

        return patch_order_status
