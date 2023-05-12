from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_order_transporter_consignee_pays import PostOrderTransporterConsigneePays
    from ..models.post_order_transporter_sender_pays_pays import PostOrderTransporterSenderPaysPays
    from ..models.post_order_transporter_third_party_pays import PostOrderTransporterThirdPartyPays


T = TypeVar("T", bound="PostOrderTransporterPayment")


@attr.s(auto_attribs=True)
class PostOrderTransporterPayment:
    """
    Attributes:
        consignee_collects (Union[Unset, None, bool]):
        consignee_pays (Union[Unset, None, PostOrderTransporterConsigneePays]):
        third_party_pays (Union[Unset, None, PostOrderTransporterThirdPartyPays]):
        sender_pays (Union[Unset, None, PostOrderTransporterSenderPaysPays]):
    """

    consignee_collects: Union[Unset, None, bool] = UNSET
    consignee_pays: Union[Unset, None, "PostOrderTransporterConsigneePays"] = UNSET
    third_party_pays: Union[Unset, None, "PostOrderTransporterThirdPartyPays"] = UNSET
    sender_pays: Union[Unset, None, "PostOrderTransporterSenderPaysPays"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        consignee_collects = self.consignee_collects
        consignee_pays: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.consignee_pays, Unset):
            consignee_pays = self.consignee_pays.to_dict() if self.consignee_pays else None

        third_party_pays: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.third_party_pays, Unset):
            third_party_pays = self.third_party_pays.to_dict() if self.third_party_pays else None

        sender_pays: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sender_pays, Unset):
            sender_pays = self.sender_pays.to_dict() if self.sender_pays else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if consignee_collects is not UNSET:
            field_dict["consigneeCollects"] = consignee_collects
        if consignee_pays is not UNSET:
            field_dict["consigneePays"] = consignee_pays
        if third_party_pays is not UNSET:
            field_dict["thirdPartyPays"] = third_party_pays
        if sender_pays is not UNSET:
            field_dict["senderPays"] = sender_pays

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_order_transporter_consignee_pays import PostOrderTransporterConsigneePays
        from ..models.post_order_transporter_sender_pays_pays import PostOrderTransporterSenderPaysPays
        from ..models.post_order_transporter_third_party_pays import PostOrderTransporterThirdPartyPays

        d = src_dict.copy()
        consignee_collects = d.pop("consigneeCollects", UNSET)

        _consignee_pays = d.pop("consigneePays", UNSET)
        consignee_pays: Union[Unset, None, PostOrderTransporterConsigneePays]
        if _consignee_pays is None:
            consignee_pays = None
        elif isinstance(_consignee_pays, Unset):
            consignee_pays = UNSET
        else:
            consignee_pays = PostOrderTransporterConsigneePays.from_dict(_consignee_pays)

        _third_party_pays = d.pop("thirdPartyPays", UNSET)
        third_party_pays: Union[Unset, None, PostOrderTransporterThirdPartyPays]
        if _third_party_pays is None:
            third_party_pays = None
        elif isinstance(_third_party_pays, Unset):
            third_party_pays = UNSET
        else:
            third_party_pays = PostOrderTransporterThirdPartyPays.from_dict(_third_party_pays)

        _sender_pays = d.pop("senderPays", UNSET)
        sender_pays: Union[Unset, None, PostOrderTransporterSenderPaysPays]
        if _sender_pays is None:
            sender_pays = None
        elif isinstance(_sender_pays, Unset):
            sender_pays = UNSET
        else:
            sender_pays = PostOrderTransporterSenderPaysPays.from_dict(_sender_pays)

        post_order_transporter_payment = cls(
            consignee_collects=consignee_collects,
            consignee_pays=consignee_pays,
            third_party_pays=third_party_pays,
            sender_pays=sender_pays,
        )

        return post_order_transporter_payment
