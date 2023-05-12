from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_order_consignee_invoice_address_advanced import PostOrderConsigneeInvoiceAddressAdvanced


T = TypeVar("T", bound="PostOrderConsigneeInvoiceAddress")


@attr.s(auto_attribs=True)
class PostOrderConsigneeInvoiceAddress:
    """
    Attributes:
        name (Union[Unset, None, str]):
        address1 (Union[Unset, None, str]):
        address2 (Union[Unset, None, str]):
        address3 (Union[Unset, None, str]):
        post_code (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        country_code (Union[Unset, None, str]):
        country_state_code (Union[Unset, None, str]):
        advanced (Union[Unset, None, PostOrderConsigneeInvoiceAddressAdvanced]):
    """

    name: Union[Unset, None, str] = UNSET
    address1: Union[Unset, None, str] = UNSET
    address2: Union[Unset, None, str] = UNSET
    address3: Union[Unset, None, str] = UNSET
    post_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    country_code: Union[Unset, None, str] = UNSET
    country_state_code: Union[Unset, None, str] = UNSET
    advanced: Union[Unset, None, "PostOrderConsigneeInvoiceAddressAdvanced"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address1 = self.address1
        address2 = self.address2
        address3 = self.address3
        post_code = self.post_code
        city = self.city
        country_code = self.country_code
        country_state_code = self.country_state_code
        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if address3 is not UNSET:
            field_dict["address3"] = address3
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if city is not UNSET:
            field_dict["city"] = city
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if country_state_code is not UNSET:
            field_dict["countryStateCode"] = country_state_code
        if advanced is not UNSET:
            field_dict["advanced"] = advanced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_order_consignee_invoice_address_advanced import PostOrderConsigneeInvoiceAddressAdvanced

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address1 = d.pop("address1", UNSET)

        address2 = d.pop("address2", UNSET)

        address3 = d.pop("address3", UNSET)

        post_code = d.pop("postCode", UNSET)

        city = d.pop("city", UNSET)

        country_code = d.pop("countryCode", UNSET)

        country_state_code = d.pop("countryStateCode", UNSET)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, PostOrderConsigneeInvoiceAddressAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = PostOrderConsigneeInvoiceAddressAdvanced.from_dict(_advanced)

        post_order_consignee_invoice_address = cls(
            name=name,
            address1=address1,
            address2=address2,
            address3=address3,
            post_code=post_code,
            city=city,
            country_code=country_code,
            country_state_code=country_state_code,
            advanced=advanced,
        )

        return post_order_consignee_invoice_address
