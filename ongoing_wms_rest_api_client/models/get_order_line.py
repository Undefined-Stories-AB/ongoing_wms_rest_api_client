from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_order_article import GetOrderArticle
    from ..models.get_order_line_free_values import GetOrderLineFreeValues
    from ..models.get_order_line_prices import GetOrderLinePrices
    from ..models.get_order_picked_article_item import GetOrderPickedArticleItem


T = TypeVar("T", bound="GetOrderLine")


@attr.s(auto_attribs=True)
class GetOrderLine:
    """
    Attributes:
        id (Union[Unset, int]):
        row_number (Union[Unset, None, str]):
        article (Union[Unset, None, GetOrderArticle]):
        comment (Union[Unset, None, str]):
        ordered_number_of_items (Union[Unset, float]):
        allocated_number_of_items (Union[Unset, float]):
        picked_number_of_items (Union[Unset, float]):
        packed_number_of_items (Union[Unset, float]):
        reported_number_of_items (Union[Unset, None, float]):
        should_be_picked (Union[Unset, bool]):
        picked_article_items (Union[Unset, None, List['GetOrderPickedArticleItem']]):
        sub_order_lines (Union[Unset, None, List['GetOrderLine']]):
        serial_number (Union[Unset, None, str]):
        line_total_customs_value (Union[Unset, None, float]):
        batch_number (Union[Unset, None, str]):
        reported_returned_number_of_items (Union[Unset, None, float]):
        line_type (Union[Unset, None, CodeNamePair]):
        prices (Union[Unset, None, GetOrderLinePrices]):
        customer_article_number (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        returned_number_of_items (Union[Unset, float]):
        free_values (Union[Unset, None, GetOrderLineFreeValues]):
    """

    id: Union[Unset, int] = UNSET
    row_number: Union[Unset, None, str] = UNSET
    article: Union[Unset, None, "GetOrderArticle"] = UNSET
    comment: Union[Unset, None, str] = UNSET
    ordered_number_of_items: Union[Unset, float] = UNSET
    allocated_number_of_items: Union[Unset, float] = UNSET
    picked_number_of_items: Union[Unset, float] = UNSET
    packed_number_of_items: Union[Unset, float] = UNSET
    reported_number_of_items: Union[Unset, None, float] = UNSET
    should_be_picked: Union[Unset, bool] = UNSET
    picked_article_items: Union[Unset, None, List["GetOrderPickedArticleItem"]] = UNSET
    sub_order_lines: Union[Unset, None, List["GetOrderLine"]] = UNSET
    serial_number: Union[Unset, None, str] = UNSET
    line_total_customs_value: Union[Unset, None, float] = UNSET
    batch_number: Union[Unset, None, str] = UNSET
    reported_returned_number_of_items: Union[Unset, None, float] = UNSET
    line_type: Union[Unset, None, "CodeNamePair"] = UNSET
    prices: Union[Unset, None, "GetOrderLinePrices"] = UNSET
    customer_article_number: Union[Unset, None, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    returned_number_of_items: Union[Unset, float] = UNSET
    free_values: Union[Unset, None, "GetOrderLineFreeValues"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        row_number = self.row_number
        article: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict() if self.article else None

        comment = self.comment
        ordered_number_of_items = self.ordered_number_of_items
        allocated_number_of_items = self.allocated_number_of_items
        picked_number_of_items = self.picked_number_of_items
        packed_number_of_items = self.packed_number_of_items
        reported_number_of_items = self.reported_number_of_items
        should_be_picked = self.should_be_picked
        picked_article_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.picked_article_items, Unset):
            if self.picked_article_items is None:
                picked_article_items = None
            else:
                picked_article_items = []
                for picked_article_items_item_data in self.picked_article_items:
                    picked_article_items_item = picked_article_items_item_data.to_dict()

                    picked_article_items.append(picked_article_items_item)

        sub_order_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_order_lines, Unset):
            if self.sub_order_lines is None:
                sub_order_lines = None
            else:
                sub_order_lines = []
                for sub_order_lines_item_data in self.sub_order_lines:
                    sub_order_lines_item = sub_order_lines_item_data.to_dict()

                    sub_order_lines.append(sub_order_lines_item)

        serial_number = self.serial_number
        line_total_customs_value = self.line_total_customs_value
        batch_number = self.batch_number
        reported_returned_number_of_items = self.reported_returned_number_of_items
        line_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.line_type, Unset):
            line_type = self.line_type.to_dict() if self.line_type else None

        prices: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.prices, Unset):
            prices = self.prices.to_dict() if self.prices else None

        customer_article_number = self.customer_article_number
        external_id = self.external_id
        returned_number_of_items = self.returned_number_of_items
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
        if ordered_number_of_items is not UNSET:
            field_dict["orderedNumberOfItems"] = ordered_number_of_items
        if allocated_number_of_items is not UNSET:
            field_dict["allocatedNumberOfItems"] = allocated_number_of_items
        if picked_number_of_items is not UNSET:
            field_dict["pickedNumberOfItems"] = picked_number_of_items
        if packed_number_of_items is not UNSET:
            field_dict["packedNumberOfItems"] = packed_number_of_items
        if reported_number_of_items is not UNSET:
            field_dict["reportedNumberOfItems"] = reported_number_of_items
        if should_be_picked is not UNSET:
            field_dict["shouldBePicked"] = should_be_picked
        if picked_article_items is not UNSET:
            field_dict["pickedArticleItems"] = picked_article_items
        if sub_order_lines is not UNSET:
            field_dict["subOrderLines"] = sub_order_lines
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if line_total_customs_value is not UNSET:
            field_dict["lineTotalCustomsValue"] = line_total_customs_value
        if batch_number is not UNSET:
            field_dict["batchNumber"] = batch_number
        if reported_returned_number_of_items is not UNSET:
            field_dict["reportedReturnedNumberOfItems"] = reported_returned_number_of_items
        if line_type is not UNSET:
            field_dict["lineType"] = line_type
        if prices is not UNSET:
            field_dict["prices"] = prices
        if customer_article_number is not UNSET:
            field_dict["customerArticleNumber"] = customer_article_number
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if returned_number_of_items is not UNSET:
            field_dict["returnedNumberOfItems"] = returned_number_of_items
        if free_values is not UNSET:
            field_dict["freeValues"] = free_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_order_article import GetOrderArticle
        from ..models.get_order_line_free_values import GetOrderLineFreeValues
        from ..models.get_order_line_prices import GetOrderLinePrices
        from ..models.get_order_picked_article_item import GetOrderPickedArticleItem

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        row_number = d.pop("rowNumber", UNSET)

        _article = d.pop("article", UNSET)
        article: Union[Unset, None, GetOrderArticle]
        if _article is None:
            article = None
        elif isinstance(_article, Unset):
            article = UNSET
        else:
            article = GetOrderArticle.from_dict(_article)

        comment = d.pop("comment", UNSET)

        ordered_number_of_items = d.pop("orderedNumberOfItems", UNSET)

        allocated_number_of_items = d.pop("allocatedNumberOfItems", UNSET)

        picked_number_of_items = d.pop("pickedNumberOfItems", UNSET)

        packed_number_of_items = d.pop("packedNumberOfItems", UNSET)

        reported_number_of_items = d.pop("reportedNumberOfItems", UNSET)

        should_be_picked = d.pop("shouldBePicked", UNSET)

        picked_article_items = []
        _picked_article_items = d.pop("pickedArticleItems", UNSET)
        for picked_article_items_item_data in _picked_article_items or []:
            picked_article_items_item = GetOrderPickedArticleItem.from_dict(picked_article_items_item_data)

            picked_article_items.append(picked_article_items_item)

        sub_order_lines = []
        _sub_order_lines = d.pop("subOrderLines", UNSET)
        for sub_order_lines_item_data in _sub_order_lines or []:
            sub_order_lines_item = GetOrderLine.from_dict(sub_order_lines_item_data)

            sub_order_lines.append(sub_order_lines_item)

        serial_number = d.pop("serialNumber", UNSET)

        line_total_customs_value = d.pop("lineTotalCustomsValue", UNSET)

        batch_number = d.pop("batchNumber", UNSET)

        reported_returned_number_of_items = d.pop("reportedReturnedNumberOfItems", UNSET)

        _line_type = d.pop("lineType", UNSET)
        line_type: Union[Unset, None, CodeNamePair]
        if _line_type is None:
            line_type = None
        elif isinstance(_line_type, Unset):
            line_type = UNSET
        else:
            line_type = CodeNamePair.from_dict(_line_type)

        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, None, GetOrderLinePrices]
        if _prices is None:
            prices = None
        elif isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = GetOrderLinePrices.from_dict(_prices)

        customer_article_number = d.pop("customerArticleNumber", UNSET)

        external_id = d.pop("externalId", UNSET)

        returned_number_of_items = d.pop("returnedNumberOfItems", UNSET)

        _free_values = d.pop("freeValues", UNSET)
        free_values: Union[Unset, None, GetOrderLineFreeValues]
        if _free_values is None:
            free_values = None
        elif isinstance(_free_values, Unset):
            free_values = UNSET
        else:
            free_values = GetOrderLineFreeValues.from_dict(_free_values)

        get_order_line = cls(
            id=id,
            row_number=row_number,
            article=article,
            comment=comment,
            ordered_number_of_items=ordered_number_of_items,
            allocated_number_of_items=allocated_number_of_items,
            picked_number_of_items=picked_number_of_items,
            packed_number_of_items=packed_number_of_items,
            reported_number_of_items=reported_number_of_items,
            should_be_picked=should_be_picked,
            picked_article_items=picked_article_items,
            sub_order_lines=sub_order_lines,
            serial_number=serial_number,
            line_total_customs_value=line_total_customs_value,
            batch_number=batch_number,
            reported_returned_number_of_items=reported_returned_number_of_items,
            line_type=line_type,
            prices=prices,
            customer_article_number=customer_article_number,
            external_id=external_id,
            returned_number_of_items=returned_number_of_items,
            free_values=free_values,
        )

        return get_order_line
