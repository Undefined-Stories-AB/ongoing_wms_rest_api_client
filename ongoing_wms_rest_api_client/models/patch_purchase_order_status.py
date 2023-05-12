from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchPurchaseOrderStatus")


@attr.s(auto_attribs=True)
class PatchPurchaseOrderStatus:
    """
    Attributes:
        purchase_order_status_number (int):
    """

    purchase_order_status_number: int

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_status_number = self.purchase_order_status_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "purchaseOrderStatusNumber": purchase_order_status_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        purchase_order_status_number = d.pop("purchaseOrderStatusNumber")

        patch_purchase_order_status = cls(
            purchase_order_status_number=purchase_order_status_number,
        )

        return patch_purchase_order_status
