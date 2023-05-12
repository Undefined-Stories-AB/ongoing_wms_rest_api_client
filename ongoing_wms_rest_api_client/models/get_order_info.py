import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_order_customs_info import GetOrderCustomsInfo
    from ..models.get_order_info_advanced import GetOrderInfoAdvanced
    from ..models.get_order_market_place import GetOrderMarketPlace
    from ..models.get_order_notification import GetOrderNotification
    from ..models.get_order_status import GetOrderStatus
    from ..models.get_order_warehouse import GetOrderWarehouse


T = TypeVar("T", bound="GetOrderInfo")


@attr.s(auto_attribs=True)
class GetOrderInfo:
    """
    Attributes:
        order_id (Union[Unset, int]):
        order_number (Union[Unset, None, str]):
        goods_owner_order_id (Union[Unset, None, str]):
        reference_number (Union[Unset, None, str]):
        sales_code (Union[Unset, None, str]):
        order_remark (Union[Unset, None, str]):
        delivery_instruction (Union[Unset, None, str]):
        service_point_code (Union[Unset, None, str]):
        free_text_1 (Union[Unset, None, str]):
        free_text_2 (Union[Unset, None, str]):
        free_text_3 (Union[Unset, None, str]):
        order_type (Union[Unset, None, CodeNamePair]):
        way_of_delivery (Union[Unset, None, CodeNamePair]):
        delivery_date (Union[Unset, datetime.datetime]):
        created_date (Union[Unset, datetime.datetime]):
        shipped_time (Union[Unset, None, datetime.datetime]):
        way_bill (Union[Unset, None, str]):
        return_way_bill (Union[Unset, None, str]):
        order_status (Union[Unset, None, GetOrderStatus]):
        email_notification (Union[Unset, None, GetOrderNotification]):
        sms_notification (Union[Unset, None, GetOrderNotification]):
        telephone_notification (Union[Unset, None, GetOrderNotification]):
        ordered_number_of_items (Union[Unset, float]):
        allocated_number_of_items (Union[Unset, float]):
        picked_number_of_items (Union[Unset, float]):
        customs_info (Union[Unset, None, GetOrderCustomsInfo]):
        prepared_transport_document_id (Union[Unset, None, str]):
        warehouse (Union[Unset, None, GetOrderWarehouse]):
        terms_of_delivery_type (Union[Unset, None, CodeNamePair]):
        customer_price (Union[Unset, None, float]):
        consignee_order_number (Union[Unset, None, str]):
        warehouse_instruction (Union[Unset, None, str]):
        market_place (Union[Unset, None, GetOrderMarketPlace]):
        picking_priority (Union[Unset, None, int]):
        production_code (Union[Unset, None, str]):
        advanced (Union[Unset, None, GetOrderInfoAdvanced]):
    """

    order_id: Union[Unset, int] = UNSET
    order_number: Union[Unset, None, str] = UNSET
    goods_owner_order_id: Union[Unset, None, str] = UNSET
    reference_number: Union[Unset, None, str] = UNSET
    sales_code: Union[Unset, None, str] = UNSET
    order_remark: Union[Unset, None, str] = UNSET
    delivery_instruction: Union[Unset, None, str] = UNSET
    service_point_code: Union[Unset, None, str] = UNSET
    free_text_1: Union[Unset, None, str] = UNSET
    free_text_2: Union[Unset, None, str] = UNSET
    free_text_3: Union[Unset, None, str] = UNSET
    order_type: Union[Unset, None, "CodeNamePair"] = UNSET
    way_of_delivery: Union[Unset, None, "CodeNamePair"] = UNSET
    delivery_date: Union[Unset, datetime.datetime] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    shipped_time: Union[Unset, None, datetime.datetime] = UNSET
    way_bill: Union[Unset, None, str] = UNSET
    return_way_bill: Union[Unset, None, str] = UNSET
    order_status: Union[Unset, None, "GetOrderStatus"] = UNSET
    email_notification: Union[Unset, None, "GetOrderNotification"] = UNSET
    sms_notification: Union[Unset, None, "GetOrderNotification"] = UNSET
    telephone_notification: Union[Unset, None, "GetOrderNotification"] = UNSET
    ordered_number_of_items: Union[Unset, float] = UNSET
    allocated_number_of_items: Union[Unset, float] = UNSET
    picked_number_of_items: Union[Unset, float] = UNSET
    customs_info: Union[Unset, None, "GetOrderCustomsInfo"] = UNSET
    prepared_transport_document_id: Union[Unset, None, str] = UNSET
    warehouse: Union[Unset, None, "GetOrderWarehouse"] = UNSET
    terms_of_delivery_type: Union[Unset, None, "CodeNamePair"] = UNSET
    customer_price: Union[Unset, None, float] = UNSET
    consignee_order_number: Union[Unset, None, str] = UNSET
    warehouse_instruction: Union[Unset, None, str] = UNSET
    market_place: Union[Unset, None, "GetOrderMarketPlace"] = UNSET
    picking_priority: Union[Unset, None, int] = UNSET
    production_code: Union[Unset, None, str] = UNSET
    advanced: Union[Unset, None, "GetOrderInfoAdvanced"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        order_number = self.order_number
        goods_owner_order_id = self.goods_owner_order_id
        reference_number = self.reference_number
        sales_code = self.sales_code
        order_remark = self.order_remark
        delivery_instruction = self.delivery_instruction
        service_point_code = self.service_point_code
        free_text_1 = self.free_text_1
        free_text_2 = self.free_text_2
        free_text_3 = self.free_text_3
        order_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.order_type, Unset):
            order_type = self.order_type.to_dict() if self.order_type else None

        way_of_delivery: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.way_of_delivery, Unset):
            way_of_delivery = self.way_of_delivery.to_dict() if self.way_of_delivery else None

        delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        shipped_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.shipped_time, Unset):
            shipped_time = self.shipped_time.isoformat() if self.shipped_time else None

        way_bill = self.way_bill
        return_way_bill = self.return_way_bill
        order_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.order_status, Unset):
            order_status = self.order_status.to_dict() if self.order_status else None

        email_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.email_notification, Unset):
            email_notification = self.email_notification.to_dict() if self.email_notification else None

        sms_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sms_notification, Unset):
            sms_notification = self.sms_notification.to_dict() if self.sms_notification else None

        telephone_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.telephone_notification, Unset):
            telephone_notification = self.telephone_notification.to_dict() if self.telephone_notification else None

        ordered_number_of_items = self.ordered_number_of_items
        allocated_number_of_items = self.allocated_number_of_items
        picked_number_of_items = self.picked_number_of_items
        customs_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customs_info, Unset):
            customs_info = self.customs_info.to_dict() if self.customs_info else None

        prepared_transport_document_id = self.prepared_transport_document_id
        warehouse: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.warehouse, Unset):
            warehouse = self.warehouse.to_dict() if self.warehouse else None

        terms_of_delivery_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.terms_of_delivery_type, Unset):
            terms_of_delivery_type = self.terms_of_delivery_type.to_dict() if self.terms_of_delivery_type else None

        customer_price = self.customer_price
        consignee_order_number = self.consignee_order_number
        warehouse_instruction = self.warehouse_instruction
        market_place: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.market_place, Unset):
            market_place = self.market_place.to_dict() if self.market_place else None

        picking_priority = self.picking_priority
        production_code = self.production_code
        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if order_number is not UNSET:
            field_dict["orderNumber"] = order_number
        if goods_owner_order_id is not UNSET:
            field_dict["goodsOwnerOrderId"] = goods_owner_order_id
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if sales_code is not UNSET:
            field_dict["salesCode"] = sales_code
        if order_remark is not UNSET:
            field_dict["orderRemark"] = order_remark
        if delivery_instruction is not UNSET:
            field_dict["deliveryInstruction"] = delivery_instruction
        if service_point_code is not UNSET:
            field_dict["servicePointCode"] = service_point_code
        if free_text_1 is not UNSET:
            field_dict["freeText1"] = free_text_1
        if free_text_2 is not UNSET:
            field_dict["freeText2"] = free_text_2
        if free_text_3 is not UNSET:
            field_dict["freeText3"] = free_text_3
        if order_type is not UNSET:
            field_dict["orderType"] = order_type
        if way_of_delivery is not UNSET:
            field_dict["wayOfDelivery"] = way_of_delivery
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if shipped_time is not UNSET:
            field_dict["shippedTime"] = shipped_time
        if way_bill is not UNSET:
            field_dict["wayBill"] = way_bill
        if return_way_bill is not UNSET:
            field_dict["returnWayBill"] = return_way_bill
        if order_status is not UNSET:
            field_dict["orderStatus"] = order_status
        if email_notification is not UNSET:
            field_dict["emailNotification"] = email_notification
        if sms_notification is not UNSET:
            field_dict["smsNotification"] = sms_notification
        if telephone_notification is not UNSET:
            field_dict["telephoneNotification"] = telephone_notification
        if ordered_number_of_items is not UNSET:
            field_dict["orderedNumberOfItems"] = ordered_number_of_items
        if allocated_number_of_items is not UNSET:
            field_dict["allocatedNumberOfItems"] = allocated_number_of_items
        if picked_number_of_items is not UNSET:
            field_dict["pickedNumberOfItems"] = picked_number_of_items
        if customs_info is not UNSET:
            field_dict["customsInfo"] = customs_info
        if prepared_transport_document_id is not UNSET:
            field_dict["preparedTransportDocumentId"] = prepared_transport_document_id
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse
        if terms_of_delivery_type is not UNSET:
            field_dict["termsOfDeliveryType"] = terms_of_delivery_type
        if customer_price is not UNSET:
            field_dict["customerPrice"] = customer_price
        if consignee_order_number is not UNSET:
            field_dict["consigneeOrderNumber"] = consignee_order_number
        if warehouse_instruction is not UNSET:
            field_dict["warehouseInstruction"] = warehouse_instruction
        if market_place is not UNSET:
            field_dict["marketPlace"] = market_place
        if picking_priority is not UNSET:
            field_dict["pickingPriority"] = picking_priority
        if production_code is not UNSET:
            field_dict["productionCode"] = production_code
        if advanced is not UNSET:
            field_dict["advanced"] = advanced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_order_customs_info import GetOrderCustomsInfo
        from ..models.get_order_info_advanced import GetOrderInfoAdvanced
        from ..models.get_order_market_place import GetOrderMarketPlace
        from ..models.get_order_notification import GetOrderNotification
        from ..models.get_order_status import GetOrderStatus
        from ..models.get_order_warehouse import GetOrderWarehouse

        d = src_dict.copy()
        order_id = d.pop("orderId", UNSET)

        order_number = d.pop("orderNumber", UNSET)

        goods_owner_order_id = d.pop("goodsOwnerOrderId", UNSET)

        reference_number = d.pop("referenceNumber", UNSET)

        sales_code = d.pop("salesCode", UNSET)

        order_remark = d.pop("orderRemark", UNSET)

        delivery_instruction = d.pop("deliveryInstruction", UNSET)

        service_point_code = d.pop("servicePointCode", UNSET)

        free_text_1 = d.pop("freeText1", UNSET)

        free_text_2 = d.pop("freeText2", UNSET)

        free_text_3 = d.pop("freeText3", UNSET)

        _order_type = d.pop("orderType", UNSET)
        order_type: Union[Unset, None, CodeNamePair]
        if _order_type is None:
            order_type = None
        elif isinstance(_order_type, Unset):
            order_type = UNSET
        else:
            order_type = CodeNamePair.from_dict(_order_type)

        _way_of_delivery = d.pop("wayOfDelivery", UNSET)
        way_of_delivery: Union[Unset, None, CodeNamePair]
        if _way_of_delivery is None:
            way_of_delivery = None
        elif isinstance(_way_of_delivery, Unset):
            way_of_delivery = UNSET
        else:
            way_of_delivery = CodeNamePair.from_dict(_way_of_delivery)

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _shipped_time = d.pop("shippedTime", UNSET)
        shipped_time: Union[Unset, None, datetime.datetime]
        if _shipped_time is None:
            shipped_time = None
        elif isinstance(_shipped_time, Unset):
            shipped_time = UNSET
        else:
            shipped_time = isoparse(_shipped_time)

        way_bill = d.pop("wayBill", UNSET)

        return_way_bill = d.pop("returnWayBill", UNSET)

        _order_status = d.pop("orderStatus", UNSET)
        order_status: Union[Unset, None, GetOrderStatus]
        if _order_status is None:
            order_status = None
        elif isinstance(_order_status, Unset):
            order_status = UNSET
        else:
            order_status = GetOrderStatus.from_dict(_order_status)

        _email_notification = d.pop("emailNotification", UNSET)
        email_notification: Union[Unset, None, GetOrderNotification]
        if _email_notification is None:
            email_notification = None
        elif isinstance(_email_notification, Unset):
            email_notification = UNSET
        else:
            email_notification = GetOrderNotification.from_dict(_email_notification)

        _sms_notification = d.pop("smsNotification", UNSET)
        sms_notification: Union[Unset, None, GetOrderNotification]
        if _sms_notification is None:
            sms_notification = None
        elif isinstance(_sms_notification, Unset):
            sms_notification = UNSET
        else:
            sms_notification = GetOrderNotification.from_dict(_sms_notification)

        _telephone_notification = d.pop("telephoneNotification", UNSET)
        telephone_notification: Union[Unset, None, GetOrderNotification]
        if _telephone_notification is None:
            telephone_notification = None
        elif isinstance(_telephone_notification, Unset):
            telephone_notification = UNSET
        else:
            telephone_notification = GetOrderNotification.from_dict(_telephone_notification)

        ordered_number_of_items = d.pop("orderedNumberOfItems", UNSET)

        allocated_number_of_items = d.pop("allocatedNumberOfItems", UNSET)

        picked_number_of_items = d.pop("pickedNumberOfItems", UNSET)

        _customs_info = d.pop("customsInfo", UNSET)
        customs_info: Union[Unset, None, GetOrderCustomsInfo]
        if _customs_info is None:
            customs_info = None
        elif isinstance(_customs_info, Unset):
            customs_info = UNSET
        else:
            customs_info = GetOrderCustomsInfo.from_dict(_customs_info)

        prepared_transport_document_id = d.pop("preparedTransportDocumentId", UNSET)

        _warehouse = d.pop("warehouse", UNSET)
        warehouse: Union[Unset, None, GetOrderWarehouse]
        if _warehouse is None:
            warehouse = None
        elif isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = GetOrderWarehouse.from_dict(_warehouse)

        _terms_of_delivery_type = d.pop("termsOfDeliveryType", UNSET)
        terms_of_delivery_type: Union[Unset, None, CodeNamePair]
        if _terms_of_delivery_type is None:
            terms_of_delivery_type = None
        elif isinstance(_terms_of_delivery_type, Unset):
            terms_of_delivery_type = UNSET
        else:
            terms_of_delivery_type = CodeNamePair.from_dict(_terms_of_delivery_type)

        customer_price = d.pop("customerPrice", UNSET)

        consignee_order_number = d.pop("consigneeOrderNumber", UNSET)

        warehouse_instruction = d.pop("warehouseInstruction", UNSET)

        _market_place = d.pop("marketPlace", UNSET)
        market_place: Union[Unset, None, GetOrderMarketPlace]
        if _market_place is None:
            market_place = None
        elif isinstance(_market_place, Unset):
            market_place = UNSET
        else:
            market_place = GetOrderMarketPlace.from_dict(_market_place)

        picking_priority = d.pop("pickingPriority", UNSET)

        production_code = d.pop("productionCode", UNSET)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, GetOrderInfoAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = GetOrderInfoAdvanced.from_dict(_advanced)

        get_order_info = cls(
            order_id=order_id,
            order_number=order_number,
            goods_owner_order_id=goods_owner_order_id,
            reference_number=reference_number,
            sales_code=sales_code,
            order_remark=order_remark,
            delivery_instruction=delivery_instruction,
            service_point_code=service_point_code,
            free_text_1=free_text_1,
            free_text_2=free_text_2,
            free_text_3=free_text_3,
            order_type=order_type,
            way_of_delivery=way_of_delivery,
            delivery_date=delivery_date,
            created_date=created_date,
            shipped_time=shipped_time,
            way_bill=way_bill,
            return_way_bill=return_way_bill,
            order_status=order_status,
            email_notification=email_notification,
            sms_notification=sms_notification,
            telephone_notification=telephone_notification,
            ordered_number_of_items=ordered_number_of_items,
            allocated_number_of_items=allocated_number_of_items,
            picked_number_of_items=picked_number_of_items,
            customs_info=customs_info,
            prepared_transport_document_id=prepared_transport_document_id,
            warehouse=warehouse,
            terms_of_delivery_type=terms_of_delivery_type,
            customer_price=customer_price,
            consignee_order_number=consignee_order_number,
            warehouse_instruction=warehouse_instruction,
            market_place=market_place,
            picking_priority=picking_priority,
            production_code=production_code,
            advanced=advanced,
        )

        return get_order_info
