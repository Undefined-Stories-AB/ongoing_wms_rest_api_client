from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_order_consignee_address_advanced import PostOrderConsigneeAddressAdvanced
    from ..models.post_order_consignee_invoice_address import PostOrderConsigneeInvoiceAddress


T = TypeVar("T", bound="PostOrderConsignee")


@attr.s(auto_attribs=True)
class PostOrderConsignee:
    """
    Attributes:
        customer_number (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        address1 (Union[Unset, None, str]):
        address2 (Union[Unset, None, str]):
        address3 (Union[Unset, None, str]):
        post_code (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        country_code (Union[Unset, None, str]):
        country_state_code (Union[Unset, None, str]):
        remark (Union[Unset, None, str]):
        door_code (Union[Unset, None, str]):
        advanced (Union[Unset, None, PostOrderConsigneeAddressAdvanced]):
        invoice_address (Union[Unset, None, PostOrderConsigneeInvoiceAddress]):
        organisation_number (Union[Unset, None, str]):
        vat_number (Union[Unset, None, str]):
    """

    customer_number: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    address1: Union[Unset, None, str] = UNSET
    address2: Union[Unset, None, str] = UNSET
    address3: Union[Unset, None, str] = UNSET
    post_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    country_code: Union[Unset, None, str] = UNSET
    country_state_code: Union[Unset, None, str] = UNSET
    remark: Union[Unset, None, str] = UNSET
    door_code: Union[Unset, None, str] = UNSET
    advanced: Union[Unset, None, "PostOrderConsigneeAddressAdvanced"] = UNSET
    invoice_address: Union[Unset, None, "PostOrderConsigneeInvoiceAddress"] = UNSET
    organisation_number: Union[Unset, None, str] = UNSET
    vat_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        customer_number = self.customer_number
        name = self.name
        address1 = self.address1
        address2 = self.address2
        address3 = self.address3
        post_code = self.post_code
        city = self.city
        country_code = self.country_code
        country_state_code = self.country_state_code
        remark = self.remark
        door_code = self.door_code
        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        invoice_address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_address, Unset):
            invoice_address = self.invoice_address.to_dict() if self.invoice_address else None

        organisation_number = self.organisation_number
        vat_number = self.vat_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if customer_number is not UNSET:
            field_dict["customerNumber"] = customer_number
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
        if remark is not UNSET:
            field_dict["remark"] = remark
        if door_code is not UNSET:
            field_dict["doorCode"] = door_code
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if invoice_address is not UNSET:
            field_dict["invoiceAddress"] = invoice_address
        if organisation_number is not UNSET:
            field_dict["organisationNumber"] = organisation_number
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_order_consignee_address_advanced import PostOrderConsigneeAddressAdvanced
        from ..models.post_order_consignee_invoice_address import PostOrderConsigneeInvoiceAddress

        d = src_dict.copy()
        customer_number = d.pop("customerNumber", UNSET)

        name = d.pop("name", UNSET)

        address1 = d.pop("address1", UNSET)

        address2 = d.pop("address2", UNSET)

        address3 = d.pop("address3", UNSET)

        post_code = d.pop("postCode", UNSET)

        city = d.pop("city", UNSET)

        country_code = d.pop("countryCode", UNSET)

        country_state_code = d.pop("countryStateCode", UNSET)

        remark = d.pop("remark", UNSET)

        door_code = d.pop("doorCode", UNSET)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, PostOrderConsigneeAddressAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = PostOrderConsigneeAddressAdvanced.from_dict(_advanced)

        _invoice_address = d.pop("invoiceAddress", UNSET)
        invoice_address: Union[Unset, None, PostOrderConsigneeInvoiceAddress]
        if _invoice_address is None:
            invoice_address = None
        elif isinstance(_invoice_address, Unset):
            invoice_address = UNSET
        else:
            invoice_address = PostOrderConsigneeInvoiceAddress.from_dict(_invoice_address)

        organisation_number = d.pop("organisationNumber", UNSET)

        vat_number = d.pop("vatNumber", UNSET)

        post_order_consignee = cls(
            customer_number=customer_number,
            name=name,
            address1=address1,
            address2=address2,
            address3=address3,
            post_code=post_code,
            city=city,
            country_code=country_code,
            country_state_code=country_state_code,
            remark=remark,
            door_code=door_code,
            advanced=advanced,
            invoice_address=invoice_address,
            organisation_number=organisation_number,
            vat_number=vat_number,
        )

        return post_order_consignee
