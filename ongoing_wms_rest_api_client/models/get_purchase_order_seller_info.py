from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPurchaseOrderSellerInfo")


@attr.s(auto_attribs=True)
class GetPurchaseOrderSellerInfo:
    """
    Attributes:
        seller_number (Union[Unset, None, str]):
        seller_name (Union[Unset, None, str]):
    """

    seller_number: Union[Unset, None, str] = UNSET
    seller_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        seller_number = self.seller_number
        seller_name = self.seller_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if seller_number is not UNSET:
            field_dict["sellerNumber"] = seller_number
        if seller_name is not UNSET:
            field_dict["sellerName"] = seller_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_number = d.pop("sellerNumber", UNSET)

        seller_name = d.pop("sellerName", UNSET)

        get_purchase_order_seller_info = cls(
            seller_number=seller_number,
            seller_name=seller_name,
        )

        return get_purchase_order_seller_info
