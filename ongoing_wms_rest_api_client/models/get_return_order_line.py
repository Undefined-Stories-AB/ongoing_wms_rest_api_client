from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_return_order_line_article import GetReturnOrderLineArticle
    from ..models.get_return_order_line_customer_order_line import GetReturnOrderLineCustomerOrderLine
    from ..models.get_returned_article_item import GetReturnedArticleItem


T = TypeVar("T", bound="GetReturnOrderLine")


@attr.s(auto_attribs=True)
class GetReturnOrderLine:
    """
    Attributes:
        return_order_line_id (Union[Unset, int]):
        return_order_row_number (Union[Unset, None, str]):
        customer_order_line (Union[Unset, None, GetReturnOrderLineCustomerOrderLine]):
        article (Union[Unset, None, GetReturnOrderLineArticle]):
        return_cause (Union[Unset, None, CodeNamePair]):
        returned_number_of_items (Union[Unset, float]):
        picked_number_of_items (Union[Unset, float]):
        to_be_returned_number_of_items (Union[Unset, float]):
        returned_removed_by_inventory_number_of_items (Union[Unset, float]):
        returned_article_items (Union[Unset, None, List['GetReturnedArticleItem']]):
    """

    return_order_line_id: Union[Unset, int] = UNSET
    return_order_row_number: Union[Unset, None, str] = UNSET
    customer_order_line: Union[Unset, None, "GetReturnOrderLineCustomerOrderLine"] = UNSET
    article: Union[Unset, None, "GetReturnOrderLineArticle"] = UNSET
    return_cause: Union[Unset, None, "CodeNamePair"] = UNSET
    returned_number_of_items: Union[Unset, float] = UNSET
    picked_number_of_items: Union[Unset, float] = UNSET
    to_be_returned_number_of_items: Union[Unset, float] = UNSET
    returned_removed_by_inventory_number_of_items: Union[Unset, float] = UNSET
    returned_article_items: Union[Unset, None, List["GetReturnedArticleItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        return_order_line_id = self.return_order_line_id
        return_order_row_number = self.return_order_row_number
        customer_order_line: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_order_line, Unset):
            customer_order_line = self.customer_order_line.to_dict() if self.customer_order_line else None

        article: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict() if self.article else None

        return_cause: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.return_cause, Unset):
            return_cause = self.return_cause.to_dict() if self.return_cause else None

        returned_number_of_items = self.returned_number_of_items
        picked_number_of_items = self.picked_number_of_items
        to_be_returned_number_of_items = self.to_be_returned_number_of_items
        returned_removed_by_inventory_number_of_items = self.returned_removed_by_inventory_number_of_items
        returned_article_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.returned_article_items, Unset):
            if self.returned_article_items is None:
                returned_article_items = None
            else:
                returned_article_items = []
                for returned_article_items_item_data in self.returned_article_items:
                    returned_article_items_item = returned_article_items_item_data.to_dict()

                    returned_article_items.append(returned_article_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if return_order_line_id is not UNSET:
            field_dict["returnOrderLineId"] = return_order_line_id
        if return_order_row_number is not UNSET:
            field_dict["returnOrderRowNumber"] = return_order_row_number
        if customer_order_line is not UNSET:
            field_dict["customerOrderLine"] = customer_order_line
        if article is not UNSET:
            field_dict["article"] = article
        if return_cause is not UNSET:
            field_dict["returnCause"] = return_cause
        if returned_number_of_items is not UNSET:
            field_dict["returnedNumberOfItems"] = returned_number_of_items
        if picked_number_of_items is not UNSET:
            field_dict["pickedNumberOfItems"] = picked_number_of_items
        if to_be_returned_number_of_items is not UNSET:
            field_dict["toBeReturnedNumberOfItems"] = to_be_returned_number_of_items
        if returned_removed_by_inventory_number_of_items is not UNSET:
            field_dict["returnedRemovedByInventoryNumberOfItems"] = returned_removed_by_inventory_number_of_items
        if returned_article_items is not UNSET:
            field_dict["returnedArticleItems"] = returned_article_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_return_order_line_article import GetReturnOrderLineArticle
        from ..models.get_return_order_line_customer_order_line import GetReturnOrderLineCustomerOrderLine
        from ..models.get_returned_article_item import GetReturnedArticleItem

        d = src_dict.copy()
        return_order_line_id = d.pop("returnOrderLineId", UNSET)

        return_order_row_number = d.pop("returnOrderRowNumber", UNSET)

        _customer_order_line = d.pop("customerOrderLine", UNSET)
        customer_order_line: Union[Unset, None, GetReturnOrderLineCustomerOrderLine]
        if _customer_order_line is None:
            customer_order_line = None
        elif isinstance(_customer_order_line, Unset):
            customer_order_line = UNSET
        else:
            customer_order_line = GetReturnOrderLineCustomerOrderLine.from_dict(_customer_order_line)

        _article = d.pop("article", UNSET)
        article: Union[Unset, None, GetReturnOrderLineArticle]
        if _article is None:
            article = None
        elif isinstance(_article, Unset):
            article = UNSET
        else:
            article = GetReturnOrderLineArticle.from_dict(_article)

        _return_cause = d.pop("returnCause", UNSET)
        return_cause: Union[Unset, None, CodeNamePair]
        if _return_cause is None:
            return_cause = None
        elif isinstance(_return_cause, Unset):
            return_cause = UNSET
        else:
            return_cause = CodeNamePair.from_dict(_return_cause)

        returned_number_of_items = d.pop("returnedNumberOfItems", UNSET)

        picked_number_of_items = d.pop("pickedNumberOfItems", UNSET)

        to_be_returned_number_of_items = d.pop("toBeReturnedNumberOfItems", UNSET)

        returned_removed_by_inventory_number_of_items = d.pop("returnedRemovedByInventoryNumberOfItems", UNSET)

        returned_article_items = []
        _returned_article_items = d.pop("returnedArticleItems", UNSET)
        for returned_article_items_item_data in _returned_article_items or []:
            returned_article_items_item = GetReturnedArticleItem.from_dict(returned_article_items_item_data)

            returned_article_items.append(returned_article_items_item)

        get_return_order_line = cls(
            return_order_line_id=return_order_line_id,
            return_order_row_number=return_order_row_number,
            customer_order_line=customer_order_line,
            article=article,
            return_cause=return_cause,
            returned_number_of_items=returned_number_of_items,
            picked_number_of_items=picked_number_of_items,
            to_be_returned_number_of_items=to_be_returned_number_of_items,
            returned_removed_by_inventory_number_of_items=returned_removed_by_inventory_number_of_items,
            returned_article_items=returned_article_items,
        )

        return get_return_order_line
