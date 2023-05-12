from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPurchaseOrderSellerAddress")


@attr.s(auto_attribs=True)
class PostPurchaseOrderSellerAddress:
    """
    Attributes:
        name (Union[Unset, None, str]):
        address (Union[Unset, None, str]):
        address2 (Union[Unset, None, str]):
        address3 (Union[Unset, None, str]):
        post_code (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        tele_phone (Union[Unset, None, str]):
        remark (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        mobile_phone (Union[Unset, None, str]):
        country_state_code (Union[Unset, None, str]):
        country_code (Union[Unset, None, str]):
        delivery_instruction (Union[Unset, None, str]):
        is_visible (Union[Unset, None, bool]):
        notify_by_sms (Union[Unset, None, bool]):
        notify_by_email (Union[Unset, None, bool]):
        notify_by_telephone (Union[Unset, None, bool]):
    """

    name: Union[Unset, None, str] = UNSET
    address: Union[Unset, None, str] = UNSET
    address2: Union[Unset, None, str] = UNSET
    address3: Union[Unset, None, str] = UNSET
    post_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    tele_phone: Union[Unset, None, str] = UNSET
    remark: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    mobile_phone: Union[Unset, None, str] = UNSET
    country_state_code: Union[Unset, None, str] = UNSET
    country_code: Union[Unset, None, str] = UNSET
    delivery_instruction: Union[Unset, None, str] = UNSET
    is_visible: Union[Unset, None, bool] = UNSET
    notify_by_sms: Union[Unset, None, bool] = UNSET
    notify_by_email: Union[Unset, None, bool] = UNSET
    notify_by_telephone: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address = self.address
        address2 = self.address2
        address3 = self.address3
        post_code = self.post_code
        city = self.city
        tele_phone = self.tele_phone
        remark = self.remark
        email = self.email
        mobile_phone = self.mobile_phone
        country_state_code = self.country_state_code
        country_code = self.country_code
        delivery_instruction = self.delivery_instruction
        is_visible = self.is_visible
        notify_by_sms = self.notify_by_sms
        notify_by_email = self.notify_by_email
        notify_by_telephone = self.notify_by_telephone

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if address3 is not UNSET:
            field_dict["address3"] = address3
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if city is not UNSET:
            field_dict["city"] = city
        if tele_phone is not UNSET:
            field_dict["telePhone"] = tele_phone
        if remark is not UNSET:
            field_dict["remark"] = remark
        if email is not UNSET:
            field_dict["email"] = email
        if mobile_phone is not UNSET:
            field_dict["mobilePhone"] = mobile_phone
        if country_state_code is not UNSET:
            field_dict["countryStateCode"] = country_state_code
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if delivery_instruction is not UNSET:
            field_dict["deliveryInstruction"] = delivery_instruction
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if notify_by_sms is not UNSET:
            field_dict["notifyBySMS"] = notify_by_sms
        if notify_by_email is not UNSET:
            field_dict["notifyByEmail"] = notify_by_email
        if notify_by_telephone is not UNSET:
            field_dict["notifyByTelephone"] = notify_by_telephone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        address2 = d.pop("address2", UNSET)

        address3 = d.pop("address3", UNSET)

        post_code = d.pop("postCode", UNSET)

        city = d.pop("city", UNSET)

        tele_phone = d.pop("telePhone", UNSET)

        remark = d.pop("remark", UNSET)

        email = d.pop("email", UNSET)

        mobile_phone = d.pop("mobilePhone", UNSET)

        country_state_code = d.pop("countryStateCode", UNSET)

        country_code = d.pop("countryCode", UNSET)

        delivery_instruction = d.pop("deliveryInstruction", UNSET)

        is_visible = d.pop("isVisible", UNSET)

        notify_by_sms = d.pop("notifyBySMS", UNSET)

        notify_by_email = d.pop("notifyByEmail", UNSET)

        notify_by_telephone = d.pop("notifyByTelephone", UNSET)

        post_purchase_order_seller_address = cls(
            name=name,
            address=address,
            address2=address2,
            address3=address3,
            post_code=post_code,
            city=city,
            tele_phone=tele_phone,
            remark=remark,
            email=email,
            mobile_phone=mobile_phone,
            country_state_code=country_state_code,
            country_code=country_code,
            delivery_instruction=delivery_instruction,
            is_visible=is_visible,
            notify_by_sms=notify_by_sms,
            notify_by_email=notify_by_email,
            notify_by_telephone=notify_by_telephone,
        )

        return post_purchase_order_seller_address
