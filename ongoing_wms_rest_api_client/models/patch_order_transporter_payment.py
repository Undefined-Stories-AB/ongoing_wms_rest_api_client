from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_order_transporter_consignee_pays import PatchOrderTransporterConsigneePays
    from ..models.patch_order_transporter_third_party_pays import PatchOrderTransporterThirdPartyPays


T = TypeVar("T", bound="PatchOrderTransporterPayment")


@attr.s(auto_attribs=True)
class PatchOrderTransporterPayment:
    """
    Attributes:
        consignee_collects (Union[Unset, None, bool]):
        consignee_pays (Union[Unset, None, PatchOrderTransporterConsigneePays]):
        third_party_pays (Union[Unset, None, PatchOrderTransporterThirdPartyPays]):
    """

    consignee_collects: Union[Unset, None, bool] = UNSET
    consignee_pays: Union[Unset, None, "PatchOrderTransporterConsigneePays"] = UNSET
    third_party_pays: Union[Unset, None, "PatchOrderTransporterThirdPartyPays"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        consignee_collects = self.consignee_collects
        consignee_pays: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.consignee_pays, Unset):
            consignee_pays = self.consignee_pays.to_dict() if self.consignee_pays else None

        third_party_pays: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.third_party_pays, Unset):
            third_party_pays = self.third_party_pays.to_dict() if self.third_party_pays else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if consignee_collects is not UNSET:
            field_dict["consigneeCollects"] = consignee_collects
        if consignee_pays is not UNSET:
            field_dict["consigneePays"] = consignee_pays
        if third_party_pays is not UNSET:
            field_dict["thirdPartyPays"] = third_party_pays

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_order_transporter_consignee_pays import PatchOrderTransporterConsigneePays
        from ..models.patch_order_transporter_third_party_pays import PatchOrderTransporterThirdPartyPays

        d = src_dict.copy()
        consignee_collects = d.pop("consigneeCollects", UNSET)

        _consignee_pays = d.pop("consigneePays", UNSET)
        consignee_pays: Union[Unset, None, PatchOrderTransporterConsigneePays]
        if _consignee_pays is None:
            consignee_pays = None
        elif isinstance(_consignee_pays, Unset):
            consignee_pays = UNSET
        else:
            consignee_pays = PatchOrderTransporterConsigneePays.from_dict(_consignee_pays)

        _third_party_pays = d.pop("thirdPartyPays", UNSET)
        third_party_pays: Union[Unset, None, PatchOrderTransporterThirdPartyPays]
        if _third_party_pays is None:
            third_party_pays = None
        elif isinstance(_third_party_pays, Unset):
            third_party_pays = UNSET
        else:
            third_party_pays = PatchOrderTransporterThirdPartyPays.from_dict(_third_party_pays)

        patch_order_transporter_payment = cls(
            consignee_collects=consignee_collects,
            consignee_pays=consignee_pays,
            third_party_pays=third_party_pays,
        )

        return patch_order_transporter_payment
