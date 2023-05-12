import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_advanced_purchase_order_info import GetAdvancedPurchaseOrderInfo
    from ..models.get_purchase_order_free_values import GetPurchaseOrderFreeValues
    from ..models.get_purchase_order_status import GetPurchaseOrderStatus
    from ..models.get_purchase_order_warehouse import GetPurchaseOrderWarehouse


T = TypeVar("T", bound="GetPurchaseOrderInfo")


@attr.s(auto_attribs=True)
class GetPurchaseOrderInfo:
    """
    Attributes:
        purchase_order_id (Union[Unset, int]):
        purchase_order_number (Union[Unset, None, str]):
        supplier_order_number (Union[Unset, None, str]):
        goods_owner_reference (Union[Unset, None, str]):
        reference_number (Union[Unset, None, str]):
        purchase_order_status (Union[Unset, None, GetPurchaseOrderStatus]):
        purchase_order_type (Union[Unset, None, CodeNamePair]):
        in_date (Union[Unset, None, datetime.datetime]):
        purchase_order_remark (Union[Unset, None, str]):
        warehouse (Union[Unset, None, GetPurchaseOrderWarehouse]):
        created_date (Union[Unset, None, datetime.datetime]):
        advanced (Union[Unset, None, GetAdvancedPurchaseOrderInfo]):
        free_values (Union[Unset, None, GetPurchaseOrderFreeValues]):
    """

    purchase_order_id: Union[Unset, int] = UNSET
    purchase_order_number: Union[Unset, None, str] = UNSET
    supplier_order_number: Union[Unset, None, str] = UNSET
    goods_owner_reference: Union[Unset, None, str] = UNSET
    reference_number: Union[Unset, None, str] = UNSET
    purchase_order_status: Union[Unset, None, "GetPurchaseOrderStatus"] = UNSET
    purchase_order_type: Union[Unset, None, "CodeNamePair"] = UNSET
    in_date: Union[Unset, None, datetime.datetime] = UNSET
    purchase_order_remark: Union[Unset, None, str] = UNSET
    warehouse: Union[Unset, None, "GetPurchaseOrderWarehouse"] = UNSET
    created_date: Union[Unset, None, datetime.datetime] = UNSET
    advanced: Union[Unset, None, "GetAdvancedPurchaseOrderInfo"] = UNSET
    free_values: Union[Unset, None, "GetPurchaseOrderFreeValues"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_id = self.purchase_order_id
        purchase_order_number = self.purchase_order_number
        supplier_order_number = self.supplier_order_number
        goods_owner_reference = self.goods_owner_reference
        reference_number = self.reference_number
        purchase_order_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.purchase_order_status, Unset):
            purchase_order_status = self.purchase_order_status.to_dict() if self.purchase_order_status else None

        purchase_order_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.purchase_order_type, Unset):
            purchase_order_type = self.purchase_order_type.to_dict() if self.purchase_order_type else None

        in_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.in_date, Unset):
            in_date = self.in_date.isoformat() if self.in_date else None

        purchase_order_remark = self.purchase_order_remark
        warehouse: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.warehouse, Unset):
            warehouse = self.warehouse.to_dict() if self.warehouse else None

        created_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat() if self.created_date else None

        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        free_values: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.free_values, Unset):
            free_values = self.free_values.to_dict() if self.free_values else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if purchase_order_id is not UNSET:
            field_dict["purchaseOrderId"] = purchase_order_id
        if purchase_order_number is not UNSET:
            field_dict["purchaseOrderNumber"] = purchase_order_number
        if supplier_order_number is not UNSET:
            field_dict["supplierOrderNumber"] = supplier_order_number
        if goods_owner_reference is not UNSET:
            field_dict["goodsOwnerReference"] = goods_owner_reference
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if purchase_order_status is not UNSET:
            field_dict["purchaseOrderStatus"] = purchase_order_status
        if purchase_order_type is not UNSET:
            field_dict["purchaseOrderType"] = purchase_order_type
        if in_date is not UNSET:
            field_dict["inDate"] = in_date
        if purchase_order_remark is not UNSET:
            field_dict["purchaseOrderRemark"] = purchase_order_remark
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if free_values is not UNSET:
            field_dict["freeValues"] = free_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_advanced_purchase_order_info import GetAdvancedPurchaseOrderInfo
        from ..models.get_purchase_order_free_values import GetPurchaseOrderFreeValues
        from ..models.get_purchase_order_status import GetPurchaseOrderStatus
        from ..models.get_purchase_order_warehouse import GetPurchaseOrderWarehouse

        d = src_dict.copy()
        purchase_order_id = d.pop("purchaseOrderId", UNSET)

        purchase_order_number = d.pop("purchaseOrderNumber", UNSET)

        supplier_order_number = d.pop("supplierOrderNumber", UNSET)

        goods_owner_reference = d.pop("goodsOwnerReference", UNSET)

        reference_number = d.pop("referenceNumber", UNSET)

        _purchase_order_status = d.pop("purchaseOrderStatus", UNSET)
        purchase_order_status: Union[Unset, None, GetPurchaseOrderStatus]
        if _purchase_order_status is None:
            purchase_order_status = None
        elif isinstance(_purchase_order_status, Unset):
            purchase_order_status = UNSET
        else:
            purchase_order_status = GetPurchaseOrderStatus.from_dict(_purchase_order_status)

        _purchase_order_type = d.pop("purchaseOrderType", UNSET)
        purchase_order_type: Union[Unset, None, CodeNamePair]
        if _purchase_order_type is None:
            purchase_order_type = None
        elif isinstance(_purchase_order_type, Unset):
            purchase_order_type = UNSET
        else:
            purchase_order_type = CodeNamePair.from_dict(_purchase_order_type)

        _in_date = d.pop("inDate", UNSET)
        in_date: Union[Unset, None, datetime.datetime]
        if _in_date is None:
            in_date = None
        elif isinstance(_in_date, Unset):
            in_date = UNSET
        else:
            in_date = isoparse(_in_date)

        purchase_order_remark = d.pop("purchaseOrderRemark", UNSET)

        _warehouse = d.pop("warehouse", UNSET)
        warehouse: Union[Unset, None, GetPurchaseOrderWarehouse]
        if _warehouse is None:
            warehouse = None
        elif isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = GetPurchaseOrderWarehouse.from_dict(_warehouse)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, None, datetime.datetime]
        if _created_date is None:
            created_date = None
        elif isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, GetAdvancedPurchaseOrderInfo]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = GetAdvancedPurchaseOrderInfo.from_dict(_advanced)

        _free_values = d.pop("freeValues", UNSET)
        free_values: Union[Unset, None, GetPurchaseOrderFreeValues]
        if _free_values is None:
            free_values = None
        elif isinstance(_free_values, Unset):
            free_values = UNSET
        else:
            free_values = GetPurchaseOrderFreeValues.from_dict(_free_values)

        get_purchase_order_info = cls(
            purchase_order_id=purchase_order_id,
            purchase_order_number=purchase_order_number,
            supplier_order_number=supplier_order_number,
            goods_owner_reference=goods_owner_reference,
            reference_number=reference_number,
            purchase_order_status=purchase_order_status,
            purchase_order_type=purchase_order_type,
            in_date=in_date,
            purchase_order_remark=purchase_order_remark,
            warehouse=warehouse,
            created_date=created_date,
            advanced=advanced,
            free_values=free_values,
        )

        return get_purchase_order_info
