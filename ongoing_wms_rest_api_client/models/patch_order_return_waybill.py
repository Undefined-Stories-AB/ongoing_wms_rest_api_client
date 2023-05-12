from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchOrderReturnWaybill")


@attr.s(auto_attribs=True)
class PatchOrderReturnWaybill:
    """
    Attributes:
        return_waybill (str):
    """

    return_waybill: str

    def to_dict(self) -> Dict[str, Any]:
        return_waybill = self.return_waybill

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "returnWaybill": return_waybill,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_waybill = d.pop("returnWaybill")

        patch_order_return_waybill = cls(
            return_waybill=return_waybill,
        )

        return patch_order_return_waybill
