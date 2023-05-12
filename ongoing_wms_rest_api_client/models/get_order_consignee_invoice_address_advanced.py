from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_consignee_customer_invoice_notification import GetOrderConsigneeCustomerInvoiceNotification


T = TypeVar("T", bound="GetOrderConsigneeInvoiceAddressAdvanced")


@attr.s(auto_attribs=True)
class GetOrderConsigneeInvoiceAddressAdvanced:
    """
    Attributes:
        telephone_notification (Union[Unset, None, GetOrderConsigneeCustomerInvoiceNotification]):
        email_notification (Union[Unset, None, GetOrderConsigneeCustomerInvoiceNotification]):
        sms_notification (Union[Unset, None, GetOrderConsigneeCustomerInvoiceNotification]):
    """

    telephone_notification: Union[Unset, None, "GetOrderConsigneeCustomerInvoiceNotification"] = UNSET
    email_notification: Union[Unset, None, "GetOrderConsigneeCustomerInvoiceNotification"] = UNSET
    sms_notification: Union[Unset, None, "GetOrderConsigneeCustomerInvoiceNotification"] = UNSET

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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if telephone_notification is not UNSET:
            field_dict["telephoneNotification"] = telephone_notification
        if email_notification is not UNSET:
            field_dict["emailNotification"] = email_notification
        if sms_notification is not UNSET:
            field_dict["smsNotification"] = sms_notification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_order_consignee_customer_invoice_notification import (
            GetOrderConsigneeCustomerInvoiceNotification,
        )

        d = src_dict.copy()
        _telephone_notification = d.pop("telephoneNotification", UNSET)
        telephone_notification: Union[Unset, None, GetOrderConsigneeCustomerInvoiceNotification]
        if _telephone_notification is None:
            telephone_notification = None
        elif isinstance(_telephone_notification, Unset):
            telephone_notification = UNSET
        else:
            telephone_notification = GetOrderConsigneeCustomerInvoiceNotification.from_dict(_telephone_notification)

        _email_notification = d.pop("emailNotification", UNSET)
        email_notification: Union[Unset, None, GetOrderConsigneeCustomerInvoiceNotification]
        if _email_notification is None:
            email_notification = None
        elif isinstance(_email_notification, Unset):
            email_notification = UNSET
        else:
            email_notification = GetOrderConsigneeCustomerInvoiceNotification.from_dict(_email_notification)

        _sms_notification = d.pop("smsNotification", UNSET)
        sms_notification: Union[Unset, None, GetOrderConsigneeCustomerInvoiceNotification]
        if _sms_notification is None:
            sms_notification = None
        elif isinstance(_sms_notification, Unset):
            sms_notification = UNSET
        else:
            sms_notification = GetOrderConsigneeCustomerInvoiceNotification.from_dict(_sms_notification)

        get_order_consignee_invoice_address_advanced = cls(
            telephone_notification=telephone_notification,
            email_notification=email_notification,
            sms_notification=sms_notification,
        )

        return get_order_consignee_invoice_address_advanced
