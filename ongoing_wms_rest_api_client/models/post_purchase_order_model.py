import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.post_purchase_order_advanced import PostPurchaseOrderAdvanced
    from ..models.post_purchase_order_customs import PostPurchaseOrderCustoms
    from ..models.post_purchase_order_free_values import PostPurchaseOrderFreeValues
    from ..models.post_purchase_order_line import PostPurchaseOrderLine
    from ..models.post_purchase_order_seller_info import PostPurchaseOrderSellerInfo
    from ..models.post_purchase_order_supplier_info import PostPurchaseOrderSupplierInfo


T = TypeVar("T", bound="PostPurchaseOrderModel")


@attr.s(auto_attribs=True)
class PostPurchaseOrderModel:
    """
    Attributes:
        goods_owner_id (int):
        purchase_order_number (str):
        supplier_order_number (Union[Unset, None, str]):
        goods_owner_reference (Union[Unset, None, str]):
        reference_number (Union[Unset, None, str]):
        in_date (Union[Unset, None, datetime.datetime]):
        supplier_info (Union[Unset, None, PostPurchaseOrderSupplierInfo]):
        purchase_order_type (Union[Unset, None, CodeNamePair]):
        purchase_order_lines (Union[Unset, None, List['PostPurchaseOrderLine']]):
        purchase_order_remark (Union[Unset, None, str]):
        warehouse_id (Union[Unset, None, int]):
        free_values (Union[Unset, None, PostPurchaseOrderFreeValues]):
        advanced (Union[Unset, None, PostPurchaseOrderAdvanced]):
        customs_info (Union[Unset, None, PostPurchaseOrderCustoms]):
        seller_info (Union[Unset, None, PostPurchaseOrderSellerInfo]):
    """

    goods_owner_id: int
    purchase_order_number: str
    supplier_order_number: Union[Unset, None, str] = UNSET
    goods_owner_reference: Union[Unset, None, str] = UNSET
    reference_number: Union[Unset, None, str] = UNSET
    in_date: Union[Unset, None, datetime.datetime] = UNSET
    supplier_info: Union[Unset, None, "PostPurchaseOrderSupplierInfo"] = UNSET
    purchase_order_type: Union[Unset, None, "CodeNamePair"] = UNSET
    purchase_order_lines: Union[Unset, None, List["PostPurchaseOrderLine"]] = UNSET
    purchase_order_remark: Union[Unset, None, str] = UNSET
    warehouse_id: Union[Unset, None, int] = UNSET
    free_values: Union[Unset, None, "PostPurchaseOrderFreeValues"] = UNSET
    advanced: Union[Unset, None, "PostPurchaseOrderAdvanced"] = UNSET
    customs_info: Union[Unset, None, "PostPurchaseOrderCustoms"] = UNSET
    seller_info: Union[Unset, None, "PostPurchaseOrderSellerInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner_id = self.goods_owner_id
        purchase_order_number = self.purchase_order_number
        supplier_order_number = self.supplier_order_number
        goods_owner_reference = self.goods_owner_reference
        reference_number = self.reference_number
        in_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.in_date, Unset):
            in_date = self.in_date.isoformat() if self.in_date else None

        supplier_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_info, Unset):
            supplier_info = self.supplier_info.to_dict() if self.supplier_info else None

        purchase_order_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.purchase_order_type, Unset):
            purchase_order_type = self.purchase_order_type.to_dict() if self.purchase_order_type else None

        purchase_order_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_order_lines, Unset):
            if self.purchase_order_lines is None:
                purchase_order_lines = None
            else:
                purchase_order_lines = []
                for purchase_order_lines_item_data in self.purchase_order_lines:
                    purchase_order_lines_item = purchase_order_lines_item_data.to_dict()

                    purchase_order_lines.append(purchase_order_lines_item)

        purchase_order_remark = self.purchase_order_remark
        warehouse_id = self.warehouse_id
        free_values: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.free_values, Unset):
            free_values = self.free_values.to_dict() if self.free_values else None

        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        customs_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customs_info, Unset):
            customs_info = self.customs_info.to_dict() if self.customs_info else None

        seller_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_info, Unset):
            seller_info = self.seller_info.to_dict() if self.seller_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "goodsOwnerId": goods_owner_id,
                "purchaseOrderNumber": purchase_order_number,
            }
        )
        if supplier_order_number is not UNSET:
            field_dict["supplierOrderNumber"] = supplier_order_number
        if goods_owner_reference is not UNSET:
            field_dict["goodsOwnerReference"] = goods_owner_reference
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if in_date is not UNSET:
            field_dict["inDate"] = in_date
        if supplier_info is not UNSET:
            field_dict["supplierInfo"] = supplier_info
        if purchase_order_type is not UNSET:
            field_dict["purchaseOrderType"] = purchase_order_type
        if purchase_order_lines is not UNSET:
            field_dict["purchaseOrderLines"] = purchase_order_lines
        if purchase_order_remark is not UNSET:
            field_dict["purchaseOrderRemark"] = purchase_order_remark
        if warehouse_id is not UNSET:
            field_dict["warehouseId"] = warehouse_id
        if free_values is not UNSET:
            field_dict["freeValues"] = free_values
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if customs_info is not UNSET:
            field_dict["customsInfo"] = customs_info
        if seller_info is not UNSET:
            field_dict["sellerInfo"] = seller_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.post_purchase_order_advanced import PostPurchaseOrderAdvanced
        from ..models.post_purchase_order_customs import PostPurchaseOrderCustoms
        from ..models.post_purchase_order_free_values import PostPurchaseOrderFreeValues
        from ..models.post_purchase_order_line import PostPurchaseOrderLine
        from ..models.post_purchase_order_seller_info import PostPurchaseOrderSellerInfo
        from ..models.post_purchase_order_supplier_info import PostPurchaseOrderSupplierInfo

        d = src_dict.copy()
        goods_owner_id = d.pop("goodsOwnerId")

        purchase_order_number = d.pop("purchaseOrderNumber")

        supplier_order_number = d.pop("supplierOrderNumber", UNSET)

        goods_owner_reference = d.pop("goodsOwnerReference", UNSET)

        reference_number = d.pop("referenceNumber", UNSET)

        _in_date = d.pop("inDate", UNSET)
        in_date: Union[Unset, None, datetime.datetime]
        if _in_date is None:
            in_date = None
        elif isinstance(_in_date, Unset):
            in_date = UNSET
        else:
            in_date = isoparse(_in_date)

        _supplier_info = d.pop("supplierInfo", UNSET)
        supplier_info: Union[Unset, None, PostPurchaseOrderSupplierInfo]
        if _supplier_info is None:
            supplier_info = None
        elif isinstance(_supplier_info, Unset):
            supplier_info = UNSET
        else:
            supplier_info = PostPurchaseOrderSupplierInfo.from_dict(_supplier_info)

        _purchase_order_type = d.pop("purchaseOrderType", UNSET)
        purchase_order_type: Union[Unset, None, CodeNamePair]
        if _purchase_order_type is None:
            purchase_order_type = None
        elif isinstance(_purchase_order_type, Unset):
            purchase_order_type = UNSET
        else:
            purchase_order_type = CodeNamePair.from_dict(_purchase_order_type)

        purchase_order_lines = []
        _purchase_order_lines = d.pop("purchaseOrderLines", UNSET)
        for purchase_order_lines_item_data in _purchase_order_lines or []:
            purchase_order_lines_item = PostPurchaseOrderLine.from_dict(purchase_order_lines_item_data)

            purchase_order_lines.append(purchase_order_lines_item)

        purchase_order_remark = d.pop("purchaseOrderRemark", UNSET)

        warehouse_id = d.pop("warehouseId", UNSET)

        _free_values = d.pop("freeValues", UNSET)
        free_values: Union[Unset, None, PostPurchaseOrderFreeValues]
        if _free_values is None:
            free_values = None
        elif isinstance(_free_values, Unset):
            free_values = UNSET
        else:
            free_values = PostPurchaseOrderFreeValues.from_dict(_free_values)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, PostPurchaseOrderAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = PostPurchaseOrderAdvanced.from_dict(_advanced)

        _customs_info = d.pop("customsInfo", UNSET)
        customs_info: Union[Unset, None, PostPurchaseOrderCustoms]
        if _customs_info is None:
            customs_info = None
        elif isinstance(_customs_info, Unset):
            customs_info = UNSET
        else:
            customs_info = PostPurchaseOrderCustoms.from_dict(_customs_info)

        _seller_info = d.pop("sellerInfo", UNSET)
        seller_info: Union[Unset, None, PostPurchaseOrderSellerInfo]
        if _seller_info is None:
            seller_info = None
        elif isinstance(_seller_info, Unset):
            seller_info = UNSET
        else:
            seller_info = PostPurchaseOrderSellerInfo.from_dict(_seller_info)

        post_purchase_order_model = cls(
            goods_owner_id=goods_owner_id,
            purchase_order_number=purchase_order_number,
            supplier_order_number=supplier_order_number,
            goods_owner_reference=goods_owner_reference,
            reference_number=reference_number,
            in_date=in_date,
            supplier_info=supplier_info,
            purchase_order_type=purchase_order_type,
            purchase_order_lines=purchase_order_lines,
            purchase_order_remark=purchase_order_remark,
            warehouse_id=warehouse_id,
            free_values=free_values,
            advanced=advanced,
            customs_info=customs_info,
            seller_info=seller_info,
        )

        return post_purchase_order_model
