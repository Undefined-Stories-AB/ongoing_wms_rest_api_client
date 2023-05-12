from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.warehouse_address_notification import WarehouseAddressNotification


T = TypeVar("T", bound="WarehouseAddressModel")


@attr.s(auto_attribs=True)
class WarehouseAddressModel:
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
        delivery_instruction (Union[Unset, None, str]):
        address_free_text_1 (Union[Unset, None, str]):
        telephone_notification (Union[Unset, None, WarehouseAddressNotification]):
        email_notification (Union[Unset, None, WarehouseAddressNotification]):
        sms_notification (Union[Unset, None, WarehouseAddressNotification]):
        address_free_text_2 (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    address1: Union[Unset, None, str] = UNSET
    address2: Union[Unset, None, str] = UNSET
    address3: Union[Unset, None, str] = UNSET
    post_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    country_code: Union[Unset, None, str] = UNSET
    country_state_code: Union[Unset, None, str] = UNSET
    delivery_instruction: Union[Unset, None, str] = UNSET
    address_free_text_1: Union[Unset, None, str] = UNSET
    telephone_notification: Union[Unset, None, "WarehouseAddressNotification"] = UNSET
    email_notification: Union[Unset, None, "WarehouseAddressNotification"] = UNSET
    sms_notification: Union[Unset, None, "WarehouseAddressNotification"] = UNSET
    address_free_text_2: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address1 = self.address1
        address2 = self.address2
        address3 = self.address3
        post_code = self.post_code
        city = self.city
        country_code = self.country_code
        country_state_code = self.country_state_code
        delivery_instruction = self.delivery_instruction
        address_free_text_1 = self.address_free_text_1
        telephone_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.telephone_notification, Unset):
            telephone_notification = self.telephone_notification.to_dict() if self.telephone_notification else None

        email_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.email_notification, Unset):
            email_notification = self.email_notification.to_dict() if self.email_notification else None

        sms_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sms_notification, Unset):
            sms_notification = self.sms_notification.to_dict() if self.sms_notification else None

        address_free_text_2 = self.address_free_text_2

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
        if delivery_instruction is not UNSET:
            field_dict["deliveryInstruction"] = delivery_instruction
        if address_free_text_1 is not UNSET:
            field_dict["addressFreeText1"] = address_free_text_1
        if telephone_notification is not UNSET:
            field_dict["telephoneNotification"] = telephone_notification
        if email_notification is not UNSET:
            field_dict["emailNotification"] = email_notification
        if sms_notification is not UNSET:
            field_dict["smsNotification"] = sms_notification
        if address_free_text_2 is not UNSET:
            field_dict["addressFreeText2"] = address_free_text_2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.warehouse_address_notification import WarehouseAddressNotification

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address1 = d.pop("address1", UNSET)

        address2 = d.pop("address2", UNSET)

        address3 = d.pop("address3", UNSET)

        post_code = d.pop("postCode", UNSET)

        city = d.pop("city", UNSET)

        country_code = d.pop("countryCode", UNSET)

        country_state_code = d.pop("countryStateCode", UNSET)

        delivery_instruction = d.pop("deliveryInstruction", UNSET)

        address_free_text_1 = d.pop("addressFreeText1", UNSET)

        _telephone_notification = d.pop("telephoneNotification", UNSET)
        telephone_notification: Union[Unset, None, WarehouseAddressNotification]
        if _telephone_notification is None:
            telephone_notification = None
        elif isinstance(_telephone_notification, Unset):
            telephone_notification = UNSET
        else:
            telephone_notification = WarehouseAddressNotification.from_dict(_telephone_notification)

        _email_notification = d.pop("emailNotification", UNSET)
        email_notification: Union[Unset, None, WarehouseAddressNotification]
        if _email_notification is None:
            email_notification = None
        elif isinstance(_email_notification, Unset):
            email_notification = UNSET
        else:
            email_notification = WarehouseAddressNotification.from_dict(_email_notification)

        _sms_notification = d.pop("smsNotification", UNSET)
        sms_notification: Union[Unset, None, WarehouseAddressNotification]
        if _sms_notification is None:
            sms_notification = None
        elif isinstance(_sms_notification, Unset):
            sms_notification = UNSET
        else:
            sms_notification = WarehouseAddressNotification.from_dict(_sms_notification)

        address_free_text_2 = d.pop("addressFreeText2", UNSET)

        warehouse_address_model = cls(
            name=name,
            address1=address1,
            address2=address2,
            address3=address3,
            post_code=post_code,
            city=city,
            country_code=country_code,
            country_state_code=country_state_code,
            delivery_instruction=delivery_instruction,
            address_free_text_1=address_free_text_1,
            telephone_notification=telephone_notification,
            email_notification=email_notification,
            sms_notification=sms_notification,
            address_free_text_2=address_free_text_2,
        )

        return warehouse_address_model
