from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderInvoiceArticleModel")


@attr.s(auto_attribs=True)
class GetOrderInvoiceArticleModel:
    """
    Attributes:
        invoice_article_id (Union[Unset, int]):
        code (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        account (Union[Unset, None, str]):
    """

    invoice_article_id: Union[Unset, int] = UNSET
    code: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    account: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        invoice_article_id = self.invoice_article_id
        code = self.code
        title = self.title
        account = self.account

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if invoice_article_id is not UNSET:
            field_dict["invoiceArticleId"] = invoice_article_id
        if code is not UNSET:
            field_dict["code"] = code
        if title is not UNSET:
            field_dict["title"] = title
        if account is not UNSET:
            field_dict["account"] = account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_article_id = d.pop("invoiceArticleId", UNSET)

        code = d.pop("code", UNSET)

        title = d.pop("title", UNSET)

        account = d.pop("account", UNSET)

        get_order_invoice_article_model = cls(
            invoice_article_id=invoice_article_id,
            code=code,
            title=title,
            account=account,
        )

        return get_order_invoice_article_model
