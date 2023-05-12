from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_class import GetOrderClass
    from ..models.get_order_consignee import GetOrderConsignee
    from ..models.get_order_goods_owner import GetOrderGoodsOwner
    from ..models.get_order_info import GetOrderInfo
    from ..models.get_order_line import GetOrderLine
    from ..models.get_order_parcel import GetOrderParcel
    from ..models.get_order_shipment_info import GetOrderShipmentInfo
    from ..models.get_order_tracking import GetOrderTracking
    from ..models.get_order_transporter import GetOrderTransporter


T = TypeVar("T", bound="GetOrderModel")


@attr.s(auto_attribs=True)
class GetOrderModel:
    """
    Attributes:
        goods_owner (Union[Unset, None, GetOrderGoodsOwner]):
        order_info (Union[Unset, None, GetOrderInfo]):
        consignee (Union[Unset, None, GetOrderConsignee]):
        parcels (Union[Unset, None, List['GetOrderParcel']]):
        order_lines (Union[Unset, None, List['GetOrderLine']]):
        transporter (Union[Unset, None, GetOrderTransporter]):
        return_transporter (Union[Unset, None, GetOrderTransporter]):
        tracking (Union[Unset, None, List['GetOrderTracking']]):
        classes (Union[Unset, None, List['GetOrderClass']]):
        shipment_info (Union[Unset, None, GetOrderShipmentInfo]):
    """

    goods_owner: Union[Unset, None, "GetOrderGoodsOwner"] = UNSET
    order_info: Union[Unset, None, "GetOrderInfo"] = UNSET
    consignee: Union[Unset, None, "GetOrderConsignee"] = UNSET
    parcels: Union[Unset, None, List["GetOrderParcel"]] = UNSET
    order_lines: Union[Unset, None, List["GetOrderLine"]] = UNSET
    transporter: Union[Unset, None, "GetOrderTransporter"] = UNSET
    return_transporter: Union[Unset, None, "GetOrderTransporter"] = UNSET
    tracking: Union[Unset, None, List["GetOrderTracking"]] = UNSET
    classes: Union[Unset, None, List["GetOrderClass"]] = UNSET
    shipment_info: Union[Unset, None, "GetOrderShipmentInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.goods_owner, Unset):
            goods_owner = self.goods_owner.to_dict() if self.goods_owner else None

        order_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.order_info, Unset):
            order_info = self.order_info.to_dict() if self.order_info else None

        consignee: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.consignee, Unset):
            consignee = self.consignee.to_dict() if self.consignee else None

        parcels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parcels, Unset):
            if self.parcels is None:
                parcels = None
            else:
                parcels = []
                for parcels_item_data in self.parcels:
                    parcels_item = parcels_item_data.to_dict()

                    parcels.append(parcels_item)

        order_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines, Unset):
            if self.order_lines is None:
                order_lines = None
            else:
                order_lines = []
                for order_lines_item_data in self.order_lines:
                    order_lines_item = order_lines_item_data.to_dict()

                    order_lines.append(order_lines_item)

        transporter: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transporter, Unset):
            transporter = self.transporter.to_dict() if self.transporter else None

        return_transporter: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.return_transporter, Unset):
            return_transporter = self.return_transporter.to_dict() if self.return_transporter else None

        tracking: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking, Unset):
            if self.tracking is None:
                tracking = None
            else:
                tracking = []
                for tracking_item_data in self.tracking:
                    tracking_item = tracking_item_data.to_dict()

                    tracking.append(tracking_item)

        classes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classes, Unset):
            if self.classes is None:
                classes = None
            else:
                classes = []
                for classes_item_data in self.classes:
                    classes_item = classes_item_data.to_dict()

                    classes.append(classes_item)

        shipment_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment_info, Unset):
            shipment_info = self.shipment_info.to_dict() if self.shipment_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if goods_owner is not UNSET:
            field_dict["goodsOwner"] = goods_owner
        if order_info is not UNSET:
            field_dict["orderInfo"] = order_info
        if consignee is not UNSET:
            field_dict["consignee"] = consignee
        if parcels is not UNSET:
            field_dict["parcels"] = parcels
        if order_lines is not UNSET:
            field_dict["orderLines"] = order_lines
        if transporter is not UNSET:
            field_dict["transporter"] = transporter
        if return_transporter is not UNSET:
            field_dict["returnTransporter"] = return_transporter
        if tracking is not UNSET:
            field_dict["tracking"] = tracking
        if classes is not UNSET:
            field_dict["classes"] = classes
        if shipment_info is not UNSET:
            field_dict["shipmentInfo"] = shipment_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_order_class import GetOrderClass
        from ..models.get_order_consignee import GetOrderConsignee
        from ..models.get_order_goods_owner import GetOrderGoodsOwner
        from ..models.get_order_info import GetOrderInfo
        from ..models.get_order_line import GetOrderLine
        from ..models.get_order_parcel import GetOrderParcel
        from ..models.get_order_shipment_info import GetOrderShipmentInfo
        from ..models.get_order_tracking import GetOrderTracking
        from ..models.get_order_transporter import GetOrderTransporter

        d = src_dict.copy()
        _goods_owner = d.pop("goodsOwner", UNSET)
        goods_owner: Union[Unset, None, GetOrderGoodsOwner]
        if _goods_owner is None:
            goods_owner = None
        elif isinstance(_goods_owner, Unset):
            goods_owner = UNSET
        else:
            goods_owner = GetOrderGoodsOwner.from_dict(_goods_owner)

        _order_info = d.pop("orderInfo", UNSET)
        order_info: Union[Unset, None, GetOrderInfo]
        if _order_info is None:
            order_info = None
        elif isinstance(_order_info, Unset):
            order_info = UNSET
        else:
            order_info = GetOrderInfo.from_dict(_order_info)

        _consignee = d.pop("consignee", UNSET)
        consignee: Union[Unset, None, GetOrderConsignee]
        if _consignee is None:
            consignee = None
        elif isinstance(_consignee, Unset):
            consignee = UNSET
        else:
            consignee = GetOrderConsignee.from_dict(_consignee)

        parcels = []
        _parcels = d.pop("parcels", UNSET)
        for parcels_item_data in _parcels or []:
            parcels_item = GetOrderParcel.from_dict(parcels_item_data)

            parcels.append(parcels_item)

        order_lines = []
        _order_lines = d.pop("orderLines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = GetOrderLine.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        _transporter = d.pop("transporter", UNSET)
        transporter: Union[Unset, None, GetOrderTransporter]
        if _transporter is None:
            transporter = None
        elif isinstance(_transporter, Unset):
            transporter = UNSET
        else:
            transporter = GetOrderTransporter.from_dict(_transporter)

        _return_transporter = d.pop("returnTransporter", UNSET)
        return_transporter: Union[Unset, None, GetOrderTransporter]
        if _return_transporter is None:
            return_transporter = None
        elif isinstance(_return_transporter, Unset):
            return_transporter = UNSET
        else:
            return_transporter = GetOrderTransporter.from_dict(_return_transporter)

        tracking = []
        _tracking = d.pop("tracking", UNSET)
        for tracking_item_data in _tracking or []:
            tracking_item = GetOrderTracking.from_dict(tracking_item_data)

            tracking.append(tracking_item)

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = GetOrderClass.from_dict(classes_item_data)

            classes.append(classes_item)

        _shipment_info = d.pop("shipmentInfo", UNSET)
        shipment_info: Union[Unset, None, GetOrderShipmentInfo]
        if _shipment_info is None:
            shipment_info = None
        elif isinstance(_shipment_info, Unset):
            shipment_info = UNSET
        else:
            shipment_info = GetOrderShipmentInfo.from_dict(_shipment_info)

        get_order_model = cls(
            goods_owner=goods_owner,
            order_info=order_info,
            consignee=consignee,
            parcels=parcels,
            order_lines=order_lines,
            transporter=transporter,
            return_transporter=return_transporter,
            tracking=tracking,
            classes=classes,
            shipment_info=shipment_info,
        )

        return get_order_model
