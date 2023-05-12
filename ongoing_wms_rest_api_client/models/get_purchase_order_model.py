from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_purchase_order_goods_owner import GetPurchaseOrderGoodsOwner
    from ..models.get_purchase_order_info import GetPurchaseOrderInfo
    from ..models.get_purchase_order_line import GetPurchaseOrderLine
    from ..models.get_purchase_order_seller_info import GetPurchaseOrderSellerInfo
    from ..models.get_purchase_order_supplier_info import GetPurchaseOrderSupplierInfo


T = TypeVar("T", bound="GetPurchaseOrderModel")


@attr.s(auto_attribs=True)
class GetPurchaseOrderModel:
    """
    Attributes:
        goods_owner (Union[Unset, None, GetPurchaseOrderGoodsOwner]):
        supplier_info (Union[Unset, None, GetPurchaseOrderSupplierInfo]):
        purchase_order_info (Union[Unset, None, GetPurchaseOrderInfo]):
        purchase_order_lines (Union[Unset, None, List['GetPurchaseOrderLine']]):
        seller_info (Union[Unset, None, GetPurchaseOrderSellerInfo]):
    """

    goods_owner: Union[Unset, None, "GetPurchaseOrderGoodsOwner"] = UNSET
    supplier_info: Union[Unset, None, "GetPurchaseOrderSupplierInfo"] = UNSET
    purchase_order_info: Union[Unset, None, "GetPurchaseOrderInfo"] = UNSET
    purchase_order_lines: Union[Unset, None, List["GetPurchaseOrderLine"]] = UNSET
    seller_info: Union[Unset, None, "GetPurchaseOrderSellerInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.goods_owner, Unset):
            goods_owner = self.goods_owner.to_dict() if self.goods_owner else None

        supplier_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_info, Unset):
            supplier_info = self.supplier_info.to_dict() if self.supplier_info else None

        purchase_order_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.purchase_order_info, Unset):
            purchase_order_info = self.purchase_order_info.to_dict() if self.purchase_order_info else None

        purchase_order_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_order_lines, Unset):
            if self.purchase_order_lines is None:
                purchase_order_lines = None
            else:
                purchase_order_lines = []
                for purchase_order_lines_item_data in self.purchase_order_lines:
                    purchase_order_lines_item = purchase_order_lines_item_data.to_dict()

                    purchase_order_lines.append(purchase_order_lines_item)

        seller_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_info, Unset):
            seller_info = self.seller_info.to_dict() if self.seller_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if goods_owner is not UNSET:
            field_dict["goodsOwner"] = goods_owner
        if supplier_info is not UNSET:
            field_dict["supplierInfo"] = supplier_info
        if purchase_order_info is not UNSET:
            field_dict["purchaseOrderInfo"] = purchase_order_info
        if purchase_order_lines is not UNSET:
            field_dict["purchaseOrderLines"] = purchase_order_lines
        if seller_info is not UNSET:
            field_dict["sellerInfo"] = seller_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_purchase_order_goods_owner import GetPurchaseOrderGoodsOwner
        from ..models.get_purchase_order_info import GetPurchaseOrderInfo
        from ..models.get_purchase_order_line import GetPurchaseOrderLine
        from ..models.get_purchase_order_seller_info import GetPurchaseOrderSellerInfo
        from ..models.get_purchase_order_supplier_info import GetPurchaseOrderSupplierInfo

        d = src_dict.copy()
        _goods_owner = d.pop("goodsOwner", UNSET)
        goods_owner: Union[Unset, None, GetPurchaseOrderGoodsOwner]
        if _goods_owner is None:
            goods_owner = None
        elif isinstance(_goods_owner, Unset):
            goods_owner = UNSET
        else:
            goods_owner = GetPurchaseOrderGoodsOwner.from_dict(_goods_owner)

        _supplier_info = d.pop("supplierInfo", UNSET)
        supplier_info: Union[Unset, None, GetPurchaseOrderSupplierInfo]
        if _supplier_info is None:
            supplier_info = None
        elif isinstance(_supplier_info, Unset):
            supplier_info = UNSET
        else:
            supplier_info = GetPurchaseOrderSupplierInfo.from_dict(_supplier_info)

        _purchase_order_info = d.pop("purchaseOrderInfo", UNSET)
        purchase_order_info: Union[Unset, None, GetPurchaseOrderInfo]
        if _purchase_order_info is None:
            purchase_order_info = None
        elif isinstance(_purchase_order_info, Unset):
            purchase_order_info = UNSET
        else:
            purchase_order_info = GetPurchaseOrderInfo.from_dict(_purchase_order_info)

        purchase_order_lines = []
        _purchase_order_lines = d.pop("purchaseOrderLines", UNSET)
        for purchase_order_lines_item_data in _purchase_order_lines or []:
            purchase_order_lines_item = GetPurchaseOrderLine.from_dict(purchase_order_lines_item_data)

            purchase_order_lines.append(purchase_order_lines_item)

        _seller_info = d.pop("sellerInfo", UNSET)
        seller_info: Union[Unset, None, GetPurchaseOrderSellerInfo]
        if _seller_info is None:
            seller_info = None
        elif isinstance(_seller_info, Unset):
            seller_info = UNSET
        else:
            seller_info = GetPurchaseOrderSellerInfo.from_dict(_seller_info)

        get_purchase_order_model = cls(
            goods_owner=goods_owner,
            supplier_info=supplier_info,
            purchase_order_info=purchase_order_info,
            purchase_order_lines=purchase_order_lines,
            seller_info=seller_info,
        )

        return get_purchase_order_model
