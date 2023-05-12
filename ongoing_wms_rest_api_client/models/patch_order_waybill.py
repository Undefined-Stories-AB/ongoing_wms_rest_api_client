from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchOrderWaybill")


@attr.s(auto_attribs=True)
class PatchOrderWaybill:
    """
    Attributes:
        waybill (str):
    """

    waybill: str

    def to_dict(self) -> Dict[str, Any]:
        waybill = self.waybill

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "waybill": waybill,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        waybill = d.pop("waybill")

        patch_order_waybill = cls(
            waybill=waybill,
        )

        return patch_order_waybill
