from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_purchase_order_seller_address import PostPurchaseOrderSellerAddress


T = TypeVar("T", bound="PostPurchaseOrderSellerInfo")


@attr.s(auto_attribs=True)
class PostPurchaseOrderSellerInfo:
    """
    Attributes:
        seller_number (Union[Unset, None, str]):
        seller_name (Union[Unset, None, str]):
        seller_address (Union[Unset, None, PostPurchaseOrderSellerAddress]):
    """

    seller_number: Union[Unset, None, str] = UNSET
    seller_name: Union[Unset, None, str] = UNSET
    seller_address: Union[Unset, None, "PostPurchaseOrderSellerAddress"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        seller_number = self.seller_number
        seller_name = self.seller_name
        seller_address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_address, Unset):
            seller_address = self.seller_address.to_dict() if self.seller_address else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if seller_number is not UNSET:
            field_dict["sellerNumber"] = seller_number
        if seller_name is not UNSET:
            field_dict["sellerName"] = seller_name
        if seller_address is not UNSET:
            field_dict["sellerAddress"] = seller_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_purchase_order_seller_address import PostPurchaseOrderSellerAddress

        d = src_dict.copy()
        seller_number = d.pop("sellerNumber", UNSET)

        seller_name = d.pop("sellerName", UNSET)

        _seller_address = d.pop("sellerAddress", UNSET)
        seller_address: Union[Unset, None, PostPurchaseOrderSellerAddress]
        if _seller_address is None:
            seller_address = None
        elif isinstance(_seller_address, Unset):
            seller_address = UNSET
        else:
            seller_address = PostPurchaseOrderSellerAddress.from_dict(_seller_address)

        post_purchase_order_seller_info = cls(
            seller_number=seller_number,
            seller_name=seller_name,
            seller_address=seller_address,
        )

        return post_purchase_order_seller_info
