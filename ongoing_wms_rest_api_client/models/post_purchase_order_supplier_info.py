from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_purchase_order_supplier_address import PostPurchaseOrderSupplierAddress


T = TypeVar("T", bound="PostPurchaseOrderSupplierInfo")


@attr.s(auto_attribs=True)
class PostPurchaseOrderSupplierInfo:
    """
    Attributes:
        supplier_number (Union[Unset, None, str]):
        supplier_name (Union[Unset, None, str]):
        supplier_address (Union[Unset, None, PostPurchaseOrderSupplierAddress]):
    """

    supplier_number: Union[Unset, None, str] = UNSET
    supplier_name: Union[Unset, None, str] = UNSET
    supplier_address: Union[Unset, None, "PostPurchaseOrderSupplierAddress"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        supplier_number = self.supplier_number
        supplier_name = self.supplier_name
        supplier_address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_address, Unset):
            supplier_address = self.supplier_address.to_dict() if self.supplier_address else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if supplier_number is not UNSET:
            field_dict["supplierNumber"] = supplier_number
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if supplier_address is not UNSET:
            field_dict["supplierAddress"] = supplier_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_purchase_order_supplier_address import PostPurchaseOrderSupplierAddress

        d = src_dict.copy()
        supplier_number = d.pop("supplierNumber", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        _supplier_address = d.pop("supplierAddress", UNSET)
        supplier_address: Union[Unset, None, PostPurchaseOrderSupplierAddress]
        if _supplier_address is None:
            supplier_address = None
        elif isinstance(_supplier_address, Unset):
            supplier_address = UNSET
        else:
            supplier_address = PostPurchaseOrderSupplierAddress.from_dict(_supplier_address)

        post_purchase_order_supplier_info = cls(
            supplier_number=supplier_number,
            supplier_name=supplier_name,
            supplier_address=supplier_address,
        )

        return post_purchase_order_supplier_info
