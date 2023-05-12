from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderShipmentInfo")


@attr.s(auto_attribs=True)
class GetOrderShipmentInfo:
    """
    Attributes:
        shipment_id (Union[Unset, int]):
    """

    shipment_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if shipment_id is not UNSET:
            field_dict["shipmentId"] = shipment_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shipment_id = d.pop("shipmentId", UNSET)

        get_order_shipment_info = cls(
            shipment_id=shipment_id,
        )

        return get_order_shipment_info
