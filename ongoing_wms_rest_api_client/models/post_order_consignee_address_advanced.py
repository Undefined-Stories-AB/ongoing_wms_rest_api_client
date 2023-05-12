from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_order_consignee_customer_notification import PostOrderConsigneeCustomerNotification


T = TypeVar("T", bound="PostOrderConsigneeAddressAdvanced")


@attr.s(auto_attribs=True)
class PostOrderConsigneeAddressAdvanced:
    """
    Attributes:
        telephone_notification (Union[Unset, None, PostOrderConsigneeCustomerNotification]):
        email_notification (Union[Unset, None, PostOrderConsigneeCustomerNotification]):
        sms_notification (Union[Unset, None, PostOrderConsigneeCustomerNotification]):
        external_customer_code (Union[Unset, None, str]):
    """

    telephone_notification: Union[Unset, None, "PostOrderConsigneeCustomerNotification"] = UNSET
    email_notification: Union[Unset, None, "PostOrderConsigneeCustomerNotification"] = UNSET
    sms_notification: Union[Unset, None, "PostOrderConsigneeCustomerNotification"] = UNSET
    external_customer_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        telephone_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.telephone_notification, Unset):
            telephone_notification = self.telephone_notification.to_dict() if self.telephone_notification else None

        email_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.email_notification, Unset):
            email_notification = self.email_notification.to_dict() if self.email_notification else None

        sms_notification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sms_notification, Unset):
            sms_notification = self.sms_notification.to_dict() if self.sms_notification else None

        external_customer_code = self.external_customer_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if telephone_notification is not UNSET:
            field_dict["telephoneNotification"] = telephone_notification
        if email_notification is not UNSET:
            field_dict["emailNotification"] = email_notification
        if sms_notification is not UNSET:
            field_dict["smsNotification"] = sms_notification
        if external_customer_code is not UNSET:
            field_dict["externalCustomerCode"] = external_customer_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_order_consignee_customer_notification import PostOrderConsigneeCustomerNotification

        d = src_dict.copy()
        _telephone_notification = d.pop("telephoneNotification", UNSET)
        telephone_notification: Union[Unset, None, PostOrderConsigneeCustomerNotification]
        if _telephone_notification is None:
            telephone_notification = None
        elif isinstance(_telephone_notification, Unset):
            telephone_notification = UNSET
        else:
            telephone_notification = PostOrderConsigneeCustomerNotification.from_dict(_telephone_notification)

        _email_notification = d.pop("emailNotification", UNSET)
        email_notification: Union[Unset, None, PostOrderConsigneeCustomerNotification]
        if _email_notification is None:
            email_notification = None
        elif isinstance(_email_notification, Unset):
            email_notification = UNSET
        else:
            email_notification = PostOrderConsigneeCustomerNotification.from_dict(_email_notification)

        _sms_notification = d.pop("smsNotification", UNSET)
        sms_notification: Union[Unset, None, PostOrderConsigneeCustomerNotification]
        if _sms_notification is None:
            sms_notification = None
        elif isinstance(_sms_notification, Unset):
            sms_notification = UNSET
        else:
            sms_notification = PostOrderConsigneeCustomerNotification.from_dict(_sms_notification)

        external_customer_code = d.pop("externalCustomerCode", UNSET)

        post_order_consignee_address_advanced = cls(
            telephone_notification=telephone_notification,
            email_notification=email_notification,
            sms_notification=sms_notification,
            external_customer_code=external_customer_code,
        )

        return post_order_consignee_address_advanced
