from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchPurchaseOrderFreeBool1")


@attr.s(auto_attribs=True)
class PatchPurchaseOrderFreeBool1:
    """
    Attributes:
        free_bool_1 (bool):
    """

    free_bool_1: bool

    def to_dict(self) -> Dict[str, Any]:
        free_bool_1 = self.free_bool_1

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "freeBool1": free_bool_1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        free_bool_1 = d.pop("freeBool1")

        patch_purchase_order_free_bool_1 = cls(
            free_bool_1=free_bool_1,
        )

        return patch_purchase_order_free_bool_1
