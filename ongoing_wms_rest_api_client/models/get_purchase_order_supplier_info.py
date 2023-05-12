from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPurchaseOrderSupplierInfo")


@attr.s(auto_attribs=True)
class GetPurchaseOrderSupplierInfo:
    """
    Attributes:
        supplier_number (Union[Unset, None, str]):
        supplier_name (Union[Unset, None, str]):
    """

    supplier_number: Union[Unset, None, str] = UNSET
    supplier_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        supplier_number = self.supplier_number
        supplier_name = self.supplier_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if supplier_number is not UNSET:
            field_dict["supplierNumber"] = supplier_number
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_number = d.pop("supplierNumber", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        get_purchase_order_supplier_info = cls(
            supplier_number=supplier_number,
            supplier_name=supplier_name,
        )

        return get_purchase_order_supplier_info
