from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_order_transporter_payment import PatchOrderTransporterPayment


T = TypeVar("T", bound="PatchOrderTransporterModel")


@attr.s(auto_attribs=True)
class PatchOrderTransporterModel:
    """
    Attributes:
        transporter_code (Union[Unset, None, str]):
        transporter_service_code (Union[Unset, None, str]):
        payment_advanced (Union[Unset, None, PatchOrderTransporterPayment]):
    """

    transporter_code: Union[Unset, None, str] = UNSET
    transporter_service_code: Union[Unset, None, str] = UNSET
    payment_advanced: Union[Unset, None, "PatchOrderTransporterPayment"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transporter_code = self.transporter_code
        transporter_service_code = self.transporter_service_code
        payment_advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_advanced, Unset):
            payment_advanced = self.payment_advanced.to_dict() if self.payment_advanced else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if transporter_code is not UNSET:
            field_dict["transporterCode"] = transporter_code
        if transporter_service_code is not UNSET:
            field_dict["transporterServiceCode"] = transporter_service_code
        if payment_advanced is not UNSET:
            field_dict["paymentAdvanced"] = payment_advanced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_order_transporter_payment import PatchOrderTransporterPayment

        d = src_dict.copy()
        transporter_code = d.pop("transporterCode", UNSET)

        transporter_service_code = d.pop("transporterServiceCode", UNSET)

        _payment_advanced = d.pop("paymentAdvanced", UNSET)
        payment_advanced: Union[Unset, None, PatchOrderTransporterPayment]
        if _payment_advanced is None:
            payment_advanced = None
        elif isinstance(_payment_advanced, Unset):
            payment_advanced = UNSET
        else:
            payment_advanced = PatchOrderTransporterPayment.from_dict(_payment_advanced)

        patch_order_transporter_model = cls(
            transporter_code=transporter_code,
            transporter_service_code=transporter_service_code,
            payment_advanced=payment_advanced,
        )

        return patch_order_transporter_model
