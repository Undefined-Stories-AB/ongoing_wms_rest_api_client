import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_order_invoice_article_model import GetOrderInvoiceArticleModel


T = TypeVar("T", bound="GetOrderInvoiceChargeModel")


@attr.s(auto_attribs=True)
class GetOrderInvoiceChargeModel:
    """
    Attributes:
        invoice_id (Union[Unset, int]):
        charge_id (Union[Unset, int]):
        price (Union[Unset, float]):
        number_of_items (Union[Unset, float]):
        action_date (Union[Unset, None, datetime.datetime]):
        comment (Union[Unset, None, str]):
        profit_center (Union[Unset, None, CodeNamePair]):
        invoice_article (Union[Unset, None, GetOrderInvoiceArticleModel]):
    """

    invoice_id: Union[Unset, int] = UNSET
    charge_id: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    number_of_items: Union[Unset, float] = UNSET
    action_date: Union[Unset, None, datetime.datetime] = UNSET
    comment: Union[Unset, None, str] = UNSET
    profit_center: Union[Unset, None, "CodeNamePair"] = UNSET
    invoice_article: Union[Unset, None, "GetOrderInvoiceArticleModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id
        charge_id = self.charge_id
        price = self.price
        number_of_items = self.number_of_items
        action_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.action_date, Unset):
            action_date = self.action_date.isoformat() if self.action_date else None

        comment = self.comment
        profit_center: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profit_center, Unset):
            profit_center = self.profit_center.to_dict() if self.profit_center else None

        invoice_article: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_article, Unset):
            invoice_article = self.invoice_article.to_dict() if self.invoice_article else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if charge_id is not UNSET:
            field_dict["chargeId"] = charge_id
        if price is not UNSET:
            field_dict["price"] = price
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if action_date is not UNSET:
            field_dict["actionDate"] = action_date
        if comment is not UNSET:
            field_dict["comment"] = comment
        if profit_center is not UNSET:
            field_dict["profitCenter"] = profit_center
        if invoice_article is not UNSET:
            field_dict["invoiceArticle"] = invoice_article

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_order_invoice_article_model import GetOrderInvoiceArticleModel

        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        charge_id = d.pop("chargeId", UNSET)

        price = d.pop("price", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        _action_date = d.pop("actionDate", UNSET)
        action_date: Union[Unset, None, datetime.datetime]
        if _action_date is None:
            action_date = None
        elif isinstance(_action_date, Unset):
            action_date = UNSET
        else:
            action_date = isoparse(_action_date)

        comment = d.pop("comment", UNSET)

        _profit_center = d.pop("profitCenter", UNSET)
        profit_center: Union[Unset, None, CodeNamePair]
        if _profit_center is None:
            profit_center = None
        elif isinstance(_profit_center, Unset):
            profit_center = UNSET
        else:
            profit_center = CodeNamePair.from_dict(_profit_center)

        _invoice_article = d.pop("invoiceArticle", UNSET)
        invoice_article: Union[Unset, None, GetOrderInvoiceArticleModel]
        if _invoice_article is None:
            invoice_article = None
        elif isinstance(_invoice_article, Unset):
            invoice_article = UNSET
        else:
            invoice_article = GetOrderInvoiceArticleModel.from_dict(_invoice_article)

        get_order_invoice_charge_model = cls(
            invoice_id=invoice_id,
            charge_id=charge_id,
            price=price,
            number_of_items=number_of_items,
            action_date=action_date,
            comment=comment,
            profit_center=profit_center,
            invoice_article=invoice_article,
        )

        return get_order_invoice_charge_model
