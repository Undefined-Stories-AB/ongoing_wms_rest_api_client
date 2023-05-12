from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair


T = TypeVar("T", bound="PostPurchaseOrderCustoms")


@attr.s(auto_attribs=True)
class PostPurchaseOrderCustoms:
    """
    Attributes:
        terms_of_delivery_type (Union[Unset, None, CodeNamePair]):
        terms_of_delivery_type_location (Union[Unset, None, str]):
    """

    terms_of_delivery_type: Union[Unset, None, "CodeNamePair"] = UNSET
    terms_of_delivery_type_location: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        terms_of_delivery_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.terms_of_delivery_type, Unset):
            terms_of_delivery_type = self.terms_of_delivery_type.to_dict() if self.terms_of_delivery_type else None

        terms_of_delivery_type_location = self.terms_of_delivery_type_location

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if terms_of_delivery_type is not UNSET:
            field_dict["termsOfDeliveryType"] = terms_of_delivery_type
        if terms_of_delivery_type_location is not UNSET:
            field_dict["termsOfDeliveryTypeLocation"] = terms_of_delivery_type_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair

        d = src_dict.copy()
        _terms_of_delivery_type = d.pop("termsOfDeliveryType", UNSET)
        terms_of_delivery_type: Union[Unset, None, CodeNamePair]
        if _terms_of_delivery_type is None:
            terms_of_delivery_type = None
        elif isinstance(_terms_of_delivery_type, Unset):
            terms_of_delivery_type = UNSET
        else:
            terms_of_delivery_type = CodeNamePair.from_dict(_terms_of_delivery_type)

        terms_of_delivery_type_location = d.pop("termsOfDeliveryTypeLocation", UNSET)

        post_purchase_order_customs = cls(
            terms_of_delivery_type=terms_of_delivery_type,
            terms_of_delivery_type_location=terms_of_delivery_type_location,
        )

        return post_purchase_order_customs
