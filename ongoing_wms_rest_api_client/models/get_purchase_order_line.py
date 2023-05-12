from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_purchase_order_article import GetPurchaseOrderArticle
    from ..models.get_purchase_order_article_item import GetPurchaseOrderArticleItem
    from ..models.get_purchase_order_line_free_values import GetPurchaseOrderLineFreeValues


T = TypeVar("T", bound="GetPurchaseOrderLine")


@attr.s(auto_attribs=True)
class GetPurchaseOrderLine:
    """
    Attributes:
        id (Union[Unset, int]):
        row_number (Union[Unset, None, str]):
        article (Union[Unset, None, GetPurchaseOrderArticle]):
        comment (Union[Unset, None, str]):
        row_price (Union[Unset, None, float]):
        advised_number_of_items (Union[Unset, float]):
        received_number_of_items (Union[Unset, float]):
        reported_number_of_items (Union[Unset, None, float]):
        article_items (Union[Unset, None, List['GetPurchaseOrderArticleItem']]):
        sub_purchase_order_lines (Union[Unset, None, List['GetPurchaseOrderLine']]):
        external_order_line_id (Union[Unset, None, str]):
        line_type (Union[Unset, None, CodeNamePair]):
        free_values (Union[Unset, None, GetPurchaseOrderLineFreeValues]):
    """

    id: Union[Unset, int] = UNSET
    row_number: Union[Unset, None, str] = UNSET
    article: Union[Unset, None, "GetPurchaseOrderArticle"] = UNSET
    comment: Union[Unset, None, str] = UNSET
    row_price: Union[Unset, None, float] = UNSET
    advised_number_of_items: Union[Unset, float] = UNSET
    received_number_of_items: Union[Unset, float] = UNSET
    reported_number_of_items: Union[Unset, None, float] = UNSET
    article_items: Union[Unset, None, List["GetPurchaseOrderArticleItem"]] = UNSET
    sub_purchase_order_lines: Union[Unset, None, List["GetPurchaseOrderLine"]] = UNSET
    external_order_line_id: Union[Unset, None, str] = UNSET
    line_type: Union[Unset, None, "CodeNamePair"] = UNSET
    free_values: Union[Unset, None, "GetPurchaseOrderLineFreeValues"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        row_number = self.row_number
        article: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict() if self.article else None

        comment = self.comment
        row_price = self.row_price
        advised_number_of_items = self.advised_number_of_items
        received_number_of_items = self.received_number_of_items
        reported_number_of_items = self.reported_number_of_items
        article_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.article_items, Unset):
            if self.article_items is None:
                article_items = None
            else:
                article_items = []
                for article_items_item_data in self.article_items:
                    article_items_item = article_items_item_data.to_dict()

                    article_items.append(article_items_item)

        sub_purchase_order_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_purchase_order_lines, Unset):
            if self.sub_purchase_order_lines is None:
                sub_purchase_order_lines = None
            else:
                sub_purchase_order_lines = []
                for sub_purchase_order_lines_item_data in self.sub_purchase_order_lines:
                    sub_purchase_order_lines_item = sub_purchase_order_lines_item_data.to_dict()

                    sub_purchase_order_lines.append(sub_purchase_order_lines_item)

        external_order_line_id = self.external_order_line_id
        line_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.line_type, Unset):
            line_type = self.line_type.to_dict() if self.line_type else None

        free_values: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.free_values, Unset):
            free_values = self.free_values.to_dict() if self.free_values else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if row_number is not UNSET:
            field_dict["rowNumber"] = row_number
        if article is not UNSET:
            field_dict["article"] = article
        if comment is not UNSET:
            field_dict["comment"] = comment
        if row_price is not UNSET:
            field_dict["rowPrice"] = row_price
        if advised_number_of_items is not UNSET:
            field_dict["advisedNumberOfItems"] = advised_number_of_items
        if received_number_of_items is not UNSET:
            field_dict["receivedNumberOfItems"] = received_number_of_items
        if reported_number_of_items is not UNSET:
            field_dict["reportedNumberOfItems"] = reported_number_of_items
        if article_items is not UNSET:
            field_dict["articleItems"] = article_items
        if sub_purchase_order_lines is not UNSET:
            field_dict["subPurchaseOrderLines"] = sub_purchase_order_lines
        if external_order_line_id is not UNSET:
            field_dict["externalOrderLineId"] = external_order_line_id
        if line_type is not UNSET:
            field_dict["lineType"] = line_type
        if free_values is not UNSET:
            field_dict["freeValues"] = free_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_purchase_order_article import GetPurchaseOrderArticle
        from ..models.get_purchase_order_article_item import GetPurchaseOrderArticleItem
        from ..models.get_purchase_order_line_free_values import GetPurchaseOrderLineFreeValues

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        row_number = d.pop("rowNumber", UNSET)

        _article = d.pop("article", UNSET)
        article: Union[Unset, None, GetPurchaseOrderArticle]
        if _article is None:
            article = None
        elif isinstance(_article, Unset):
            article = UNSET
        else:
            article = GetPurchaseOrderArticle.from_dict(_article)

        comment = d.pop("comment", UNSET)

        row_price = d.pop("rowPrice", UNSET)

        advised_number_of_items = d.pop("advisedNumberOfItems", UNSET)

        received_number_of_items = d.pop("receivedNumberOfItems", UNSET)

        reported_number_of_items = d.pop("reportedNumberOfItems", UNSET)

        article_items = []
        _article_items = d.pop("articleItems", UNSET)
        for article_items_item_data in _article_items or []:
            article_items_item = GetPurchaseOrderArticleItem.from_dict(article_items_item_data)

            article_items.append(article_items_item)

        sub_purchase_order_lines = []
        _sub_purchase_order_lines = d.pop("subPurchaseOrderLines", UNSET)
        for sub_purchase_order_lines_item_data in _sub_purchase_order_lines or []:
            sub_purchase_order_lines_item = GetPurchaseOrderLine.from_dict(sub_purchase_order_lines_item_data)

            sub_purchase_order_lines.append(sub_purchase_order_lines_item)

        external_order_line_id = d.pop("externalOrderLineId", UNSET)

        _line_type = d.pop("lineType", UNSET)
        line_type: Union[Unset, None, CodeNamePair]
        if _line_type is None:
            line_type = None
        elif isinstance(_line_type, Unset):
            line_type = UNSET
        else:
            line_type = CodeNamePair.from_dict(_line_type)

        _free_values = d.pop("freeValues", UNSET)
        free_values: Union[Unset, None, GetPurchaseOrderLineFreeValues]
        if _free_values is None:
            free_values = None
        elif isinstance(_free_values, Unset):
            free_values = UNSET
        else:
            free_values = GetPurchaseOrderLineFreeValues.from_dict(_free_values)

        get_purchase_order_line = cls(
            id=id,
            row_number=row_number,
            article=article,
            comment=comment,
            row_price=row_price,
            advised_number_of_items=advised_number_of_items,
            received_number_of_items=received_number_of_items,
            reported_number_of_items=reported_number_of_items,
            article_items=article_items,
            sub_purchase_order_lines=sub_purchase_order_lines,
            external_order_line_id=external_order_line_id,
            line_type=line_type,
            free_values=free_values,
        )

        return get_purchase_order_line
