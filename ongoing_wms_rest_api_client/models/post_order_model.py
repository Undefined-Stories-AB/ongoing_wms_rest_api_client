import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.post_order_advanced import PostOrderAdvanced
    from ..models.post_order_class import PostOrderClass
    from ..models.post_order_consignee import PostOrderConsignee
    from ..models.post_order_customs_info import PostOrderCustomsInfo
    from ..models.post_order_line import PostOrderLine
    from ..models.post_order_market_place import PostOrderMarketPlace
    from ..models.post_order_notification import PostOrderNotification
    from ..models.post_order_return_transporter import PostOrderReturnTransporter
    from ..models.post_order_transporter import PostOrderTransporter


T = TypeVar("T", bound="PostOrderModel")


@attr.s(auto_attribs=True)
class PostOrderModel:
    """
    Attributes:
        goods_owner_id (int):
        order_number (str):
        delivery_date (datetime.datetime):
        consignee (PostOrderConsignee):
        reference_number (Union[Unset, None, str]):
        goods_owner_order_id (Union[Unset, None, str]):
        sales_code (Union[Unset, None, str]):
        order_remark (Union[Unset, None, str]):
        delivery_instruction (Union[Unset, None, str]):
        service_point_code (Union[Unset, None, str]):
        free_text_1 (Union[Unset, None, str]):
        free_text_2 (Union[Unset, None, str]):
        free_text_3 (Union[Unset, None, str]):
        order_free_date_time_1 (Union[Unset, None, datetime.datetime]):
        order_type (Union[Unset, None, CodeNamePair]):
        way_of_delivery (Union[Unset, None, CodeNamePair]):
        email_notification (Union[Unset, None, PostOrderNotification]):
        sms_notification (Union[Unset, None, PostOrderNotification]):
        telephone_notification (Union[Unset, None, PostOrderNotification]):
        transporter (Union[Unset, None, PostOrderTransporter]):
        return_transporter (Union[Unset, None, PostOrderReturnTransporter]):
        order_lines (Union[Unset, None, List['PostOrderLine']]):
        customs_info (Union[Unset, None, PostOrderCustomsInfo]):
        prepared_transport_document_id (Union[Unset, None, str]):
        freight_price (Union[Unset, None, float]):
        warehouse_id (Union[Unset, None, int]):
        classes (Union[Unset, None, List['PostOrderClass']]):
        terms_of_delivery_type (Union[Unset, None, CodeNamePair]):
        customer_price (Union[Unset, None, float]):
        advanced (Union[Unset, None, PostOrderAdvanced]):
        consignee_order_number (Union[Unset, None, str]):
        warehouse_instruction (Union[Unset, None, str]):
        market_place (Union[Unset, None, PostOrderMarketPlace]):
        picking_priority (Union[Unset, None, int]):
        production_code (Union[Unset, None, str]):
        transporter_bulk_id (Union[Unset, None, str]):
    """

    goods_owner_id: int
    order_number: str
    delivery_date: datetime.datetime
    consignee: "PostOrderConsignee"
    reference_number: Union[Unset, None, str] = UNSET
    goods_owner_order_id: Union[Unset, None, str] = UNSET
    sales_code: Union[Unset, None, str] = UNSET
    order_remark: Union[Unset, None, str] = UNSET
    delivery_instruction: Union[Unset, None, str] = UNSET
    service_point_code: Union[Unset, None, str] = UNSET
    free_text_1: Union[Unset, None, str] = UNSET
    free_text_2: Union[Unset, None, str] = UNSET
    free_text_3: Union[Unset, None, str] = UNSET
    order_free_date_time_1: Union[Unset, None, datetime.datetime] = UNSET
    order_type: Union[Unset, None, "CodeNamePair"] = UNSET
    way_of_delivery: Union[Unset, None, "CodeNamePair"] = UNSET
    email_notification: Union[Unset, None, "PostOrderNotification"] = UNSET
    sms_notification: Union[Unset, None, "PostOrderNotification"] = UNSET
    telephone_notification: Union[Unset, None, "PostOrderNotification"] = UNSET
    transporter: Union[Unset, None, "PostOrderTransporter"] = UNSET
    return_transporter: Union[Unset, None, "PostOrderReturnTransporter"] = UNSET
    order_lines: Union[Unset, None, List["PostOrderLine"]] = UNSET
    customs_info: Union[Unset, None, "PostOrderCustomsInfo"] = UNSET
    prepared_transport_document_id: Union[Unset, None, str] = UNSET
    freight_price: Union[Unset, None, float] = UNSET
    warehouse_id: Union[Unset, None, int] = UNSET
    classes: Union[Unset, None, List["PostOrderClass"]] = UNSET
    terms_of_delivery_type: Union[Unset, None, "CodeNamePair"] = UNSET
    customer_price: Union[Unset, None, float] = UNSET
    advanced: Union[Unset, None, "PostOrderAdvanced"] = UNSET
    consignee_order_number: Union[Unset, None, str] = UNSET
    warehouse_instruction: Union[Unset, None, str] = UNSET
    market_place: Union[Unset, None, "PostOrderMarketPlace"] = UNSET
    picking_priority: Union[Unset, None, int] = UNSET
    production_code: Union[Unset, None, str] = UNSET
    transporter_bulk_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner_id = self.goods_owner_id
        order_number = self.order_number
        delivery_date = self.delivery_date.isoformat()

        consignee = self.consignee.to_dict()

        reference_number = self.reference_number
        goods_owner_order_id = self.goods_owner_order_id
        sales_code = self.sales_code
        order_remark = self.order_remark
        delivery_instruction = self.delivery_instruction
        service_point_code = self.service_point_code
        free_text_1 = self.free_text_1
        free_text_2 = self.free_text_2
        free_text_3 = self.free_text_3
        order_free_date_time_1: Union[Unset, None, str] = UNSET
        if not isinstance(self.order_free_date_time_1, Unset):
            order_free_date_time_1 = self.order_free_date_time_1.isoformat() if self.order_free_date_time_1 else None

        order_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.order_type, Unset):
            order_type = self.order_type.to_dict() if self.order_type else None

        way_of_delivery: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.way_of_delivery, Unset):
            way_of_delivery = self.way_of_delivery.to_dict() if self.way_of_delivery else None

        email_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.email_notification, Unset):
            email_notification = self.email_notification.to_dict() if self.email_notification else None

        sms_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sms_notification, Unset):
            sms_notification = self.sms_notification.to_dict() if self.sms_notification else None

        telephone_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.telephone_notification, Unset):
            telephone_notification = self.telephone_notification.to_dict() if self.telephone_notification else None

        transporter: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transporter, Unset):
            transporter = self.transporter.to_dict() if self.transporter else None

        return_transporter: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.return_transporter, Unset):
            return_transporter = self.return_transporter.to_dict() if self.return_transporter else None

        order_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines, Unset):
            if self.order_lines is None:
                order_lines = None
            else:
                order_lines = []
                for order_lines_item_data in self.order_lines:
                    order_lines_item = order_lines_item_data.to_dict()

                    order_lines.append(order_lines_item)

        customs_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customs_info, Unset):
            customs_info = self.customs_info.to_dict() if self.customs_info else None

        prepared_transport_document_id = self.prepared_transport_document_id
        freight_price = self.freight_price
        warehouse_id = self.warehouse_id
        classes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classes, Unset):
            if self.classes is None:
                classes = None
            else:
                classes = []
                for classes_item_data in self.classes:
                    classes_item = classes_item_data.to_dict()

                    classes.append(classes_item)

        terms_of_delivery_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.terms_of_delivery_type, Unset):
            terms_of_delivery_type = self.terms_of_delivery_type.to_dict() if self.terms_of_delivery_type else None

        customer_price = self.customer_price
        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        consignee_order_number = self.consignee_order_number
        warehouse_instruction = self.warehouse_instruction
        market_place: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.market_place, Unset):
            market_place = self.market_place.to_dict() if self.market_place else None

        picking_priority = self.picking_priority
        production_code = self.production_code
        transporter_bulk_id = self.transporter_bulk_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "goodsOwnerId": goods_owner_id,
                "orderNumber": order_number,
                "deliveryDate": delivery_date,
                "consignee": consignee,
            }
        )
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if goods_owner_order_id is not UNSET:
            field_dict["goodsOwnerOrderId"] = goods_owner_order_id
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
        if order_free_date_time_1 is not UNSET:
            field_dict["orderFreeDateTime1"] = order_free_date_time_1
        if order_type is not UNSET:
            field_dict["orderType"] = order_type
        if way_of_delivery is not UNSET:
            field_dict["wayOfDelivery"] = way_of_delivery
        if email_notification is not UNSET:
            field_dict["emailNotification"] = email_notification
        if sms_notification is not UNSET:
            field_dict["smsNotification"] = sms_notification
        if telephone_notification is not UNSET:
            field_dict["telephoneNotification"] = telephone_notification
        if transporter is not UNSET:
            field_dict["transporter"] = transporter
        if return_transporter is not UNSET:
            field_dict["returnTransporter"] = return_transporter
        if order_lines is not UNSET:
            field_dict["orderLines"] = order_lines
        if customs_info is not UNSET:
            field_dict["customsInfo"] = customs_info
        if prepared_transport_document_id is not UNSET:
            field_dict["preparedTransportDocumentId"] = prepared_transport_document_id
        if freight_price is not UNSET:
            field_dict["freightPrice"] = freight_price
        if warehouse_id is not UNSET:
            field_dict["warehouseId"] = warehouse_id
        if classes is not UNSET:
            field_dict["classes"] = classes
        if terms_of_delivery_type is not UNSET:
            field_dict["termsOfDeliveryType"] = terms_of_delivery_type
        if customer_price is not UNSET:
            field_dict["customerPrice"] = customer_price
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
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
        if transporter_bulk_id is not UNSET:
            field_dict["transporterBulkId"] = transporter_bulk_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.post_order_advanced import PostOrderAdvanced
        from ..models.post_order_class import PostOrderClass
        from ..models.post_order_consignee import PostOrderConsignee
        from ..models.post_order_customs_info import PostOrderCustomsInfo
        from ..models.post_order_line import PostOrderLine
        from ..models.post_order_market_place import PostOrderMarketPlace
        from ..models.post_order_notification import PostOrderNotification
        from ..models.post_order_return_transporter import PostOrderReturnTransporter
        from ..models.post_order_transporter import PostOrderTransporter

        d = src_dict.copy()
        goods_owner_id = d.pop("goodsOwnerId")

        order_number = d.pop("orderNumber")

        delivery_date = isoparse(d.pop("deliveryDate"))

        consignee = PostOrderConsignee.from_dict(d.pop("consignee"))

        reference_number = d.pop("referenceNumber", UNSET)

        goods_owner_order_id = d.pop("goodsOwnerOrderId", UNSET)

        sales_code = d.pop("salesCode", UNSET)

        order_remark = d.pop("orderRemark", UNSET)

        delivery_instruction = d.pop("deliveryInstruction", UNSET)

        service_point_code = d.pop("servicePointCode", UNSET)

        free_text_1 = d.pop("freeText1", UNSET)

        free_text_2 = d.pop("freeText2", UNSET)

        free_text_3 = d.pop("freeText3", UNSET)

        _order_free_date_time_1 = d.pop("orderFreeDateTime1", UNSET)
        order_free_date_time_1: Union[Unset, None, datetime.datetime]
        if _order_free_date_time_1 is None:
            order_free_date_time_1 = None
        elif isinstance(_order_free_date_time_1, Unset):
            order_free_date_time_1 = UNSET
        else:
            order_free_date_time_1 = isoparse(_order_free_date_time_1)

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

        _email_notification = d.pop("emailNotification", UNSET)
        email_notification: Union[Unset, None, PostOrderNotification]
        if _email_notification is None:
            email_notification = None
        elif isinstance(_email_notification, Unset):
            email_notification = UNSET
        else:
            email_notification = PostOrderNotification.from_dict(_email_notification)

        _sms_notification = d.pop("smsNotification", UNSET)
        sms_notification: Union[Unset, None, PostOrderNotification]
        if _sms_notification is None:
            sms_notification = None
        elif isinstance(_sms_notification, Unset):
            sms_notification = UNSET
        else:
            sms_notification = PostOrderNotification.from_dict(_sms_notification)

        _telephone_notification = d.pop("telephoneNotification", UNSET)
        telephone_notification: Union[Unset, None, PostOrderNotification]
        if _telephone_notification is None:
            telephone_notification = None
        elif isinstance(_telephone_notification, Unset):
            telephone_notification = UNSET
        else:
            telephone_notification = PostOrderNotification.from_dict(_telephone_notification)

        _transporter = d.pop("transporter", UNSET)
        transporter: Union[Unset, None, PostOrderTransporter]
        if _transporter is None:
            transporter = None
        elif isinstance(_transporter, Unset):
            transporter = UNSET
        else:
            transporter = PostOrderTransporter.from_dict(_transporter)

        _return_transporter = d.pop("returnTransporter", UNSET)
        return_transporter: Union[Unset, None, PostOrderReturnTransporter]
        if _return_transporter is None:
            return_transporter = None
        elif isinstance(_return_transporter, Unset):
            return_transporter = UNSET
        else:
            return_transporter = PostOrderReturnTransporter.from_dict(_return_transporter)

        order_lines = []
        _order_lines = d.pop("orderLines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = PostOrderLine.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        _customs_info = d.pop("customsInfo", UNSET)
        customs_info: Union[Unset, None, PostOrderCustomsInfo]
        if _customs_info is None:
            customs_info = None
        elif isinstance(_customs_info, Unset):
            customs_info = UNSET
        else:
            customs_info = PostOrderCustomsInfo.from_dict(_customs_info)

        prepared_transport_document_id = d.pop("preparedTransportDocumentId", UNSET)

        freight_price = d.pop("freightPrice", UNSET)

        warehouse_id = d.pop("warehouseId", UNSET)

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = PostOrderClass.from_dict(classes_item_data)

            classes.append(classes_item)

        _terms_of_delivery_type = d.pop("termsOfDeliveryType", UNSET)
        terms_of_delivery_type: Union[Unset, None, CodeNamePair]
        if _terms_of_delivery_type is None:
            terms_of_delivery_type = None
        elif isinstance(_terms_of_delivery_type, Unset):
            terms_of_delivery_type = UNSET
        else:
            terms_of_delivery_type = CodeNamePair.from_dict(_terms_of_delivery_type)

        customer_price = d.pop("customerPrice", UNSET)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, PostOrderAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = PostOrderAdvanced.from_dict(_advanced)

        consignee_order_number = d.pop("consigneeOrderNumber", UNSET)

        warehouse_instruction = d.pop("warehouseInstruction", UNSET)

        _market_place = d.pop("marketPlace", UNSET)
        market_place: Union[Unset, None, PostOrderMarketPlace]
        if _market_place is None:
            market_place = None
        elif isinstance(_market_place, Unset):
            market_place = UNSET
        else:
            market_place = PostOrderMarketPlace.from_dict(_market_place)

        picking_priority = d.pop("pickingPriority", UNSET)

        production_code = d.pop("productionCode", UNSET)

        transporter_bulk_id = d.pop("transporterBulkId", UNSET)

        post_order_model = cls(
            goods_owner_id=goods_owner_id,
            order_number=order_number,
            delivery_date=delivery_date,
            consignee=consignee,
            reference_number=reference_number,
            goods_owner_order_id=goods_owner_order_id,
            sales_code=sales_code,
            order_remark=order_remark,
            delivery_instruction=delivery_instruction,
            service_point_code=service_point_code,
            free_text_1=free_text_1,
            free_text_2=free_text_2,
            free_text_3=free_text_3,
            order_free_date_time_1=order_free_date_time_1,
            order_type=order_type,
            way_of_delivery=way_of_delivery,
            email_notification=email_notification,
            sms_notification=sms_notification,
            telephone_notification=telephone_notification,
            transporter=transporter,
            return_transporter=return_transporter,
            order_lines=order_lines,
            customs_info=customs_info,
            prepared_transport_document_id=prepared_transport_document_id,
            freight_price=freight_price,
            warehouse_id=warehouse_id,
            classes=classes,
            terms_of_delivery_type=terms_of_delivery_type,
            customer_price=customer_price,
            advanced=advanced,
            consignee_order_number=consignee_order_number,
            warehouse_instruction=warehouse_instruction,
            market_place=market_place,
            picking_priority=picking_priority,
            production_code=production_code,
            transporter_bulk_id=transporter_bulk_id,
        )

        return post_order_model
