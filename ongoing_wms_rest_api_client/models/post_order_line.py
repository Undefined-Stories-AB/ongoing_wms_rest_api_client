from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.post_order_line_free_values import PostOrderLineFreeValues
    from ..models.post_order_line_prices import PostOrderLinePrices


T = TypeVar("T", bound="PostOrderLine")


@attr.s(auto_attribs=True)
class PostOrderLine:
    """
    Attributes:
        row_number (str):
        article_number (str):
        number_of_items (Union[Unset, float]):
        comment (Union[Unset, None, str]):
        should_be_picked (Union[Unset, None, bool]):
        serial_number (Union[Unset, None, str]):
        line_total_customs_value (Union[Unset, None, float]):
        batch_number (Union[Unset, None, str]):
        line_type (Union[Unset, None, CodeNamePair]):
        prices (Union[Unset, None, PostOrderLinePrices]):
        customer_article_number (Union[Unset, None, str]):
        warehouse_instruction (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        article_item_status (Union[Unset, None, CodeNamePair]):
        line_free_values (Union[Unset, None, PostOrderLineFreeValues]):
    """

    row_number: str
    article_number: str
    number_of_items: Union[Unset, float] = UNSET
    comment: Union[Unset, None, str] = UNSET
    should_be_picked: Union[Unset, None, bool] = UNSET
    serial_number: Union[Unset, None, str] = UNSET
    line_total_customs_value: Union[Unset, None, float] = UNSET
    batch_number: Union[Unset, None, str] = UNSET
    line_type: Union[Unset, None, "CodeNamePair"] = UNSET
    prices: Union[Unset, None, "PostOrderLinePrices"] = UNSET
    customer_article_number: Union[Unset, None, str] = UNSET
    warehouse_instruction: Union[Unset, None, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    article_item_status: Union[Unset, None, "CodeNamePair"] = UNSET
    line_free_values: Union[Unset, None, "PostOrderLineFreeValues"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        row_number = self.row_number
        article_number = self.article_number
        number_of_items = self.number_of_items
        comment = self.comment
        should_be_picked = self.should_be_picked
        serial_number = self.serial_number
        line_total_customs_value = self.line_total_customs_value
        batch_number = self.batch_number
        line_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.line_type, Unset):
            line_type = self.line_type.to_dict() if self.line_type else None

        prices: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.prices, Unset):
            prices = self.prices.to_dict() if self.prices else None

        customer_article_number = self.customer_article_number
        warehouse_instruction = self.warehouse_instruction
        external_id = self.external_id
        article_item_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_item_status, Unset):
            article_item_status = self.article_item_status.to_dict() if self.article_item_status else None

        line_free_values: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.line_free_values, Unset):
            line_free_values = self.line_free_values.to_dict() if self.line_free_values else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "rowNumber": row_number,
                "articleNumber": article_number,
            }
        )
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items
        if comment is not UNSET:
            field_dict["comment"] = comment
        if should_be_picked is not UNSET:
            field_dict["shouldBePicked"] = should_be_picked
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if line_total_customs_value is not UNSET:
            field_dict["lineTotalCustomsValue"] = line_total_customs_value
        if batch_number is not UNSET:
            field_dict["batchNumber"] = batch_number
        if line_type is not UNSET:
            field_dict["lineType"] = line_type
        if prices is not UNSET:
            field_dict["prices"] = prices
        if customer_article_number is not UNSET:
            field_dict["customerArticleNumber"] = customer_article_number
        if warehouse_instruction is not UNSET:
            field_dict["warehouseInstruction"] = warehouse_instruction
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if article_item_status is not UNSET:
            field_dict["articleItemStatus"] = article_item_status
        if line_free_values is not UNSET:
            field_dict["lineFreeValues"] = line_free_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.post_order_line_free_values import PostOrderLineFreeValues
        from ..models.post_order_line_prices import PostOrderLinePrices

        d = src_dict.copy()
        row_number = d.pop("rowNumber")

        article_number = d.pop("articleNumber")

        number_of_items = d.pop("numberOfItems", UNSET)

        comment = d.pop("comment", UNSET)

        should_be_picked = d.pop("shouldBePicked", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        line_total_customs_value = d.pop("lineTotalCustomsValue", UNSET)

        batch_number = d.pop("batchNumber", UNSET)

        _line_type = d.pop("lineType", UNSET)
        line_type: Union[Unset, None, CodeNamePair]
        if _line_type is None:
            line_type = None
        elif isinstance(_line_type, Unset):
            line_type = UNSET
        else:
            line_type = CodeNamePair.from_dict(_line_type)

        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, None, PostOrderLinePrices]
        if _prices is None:
            prices = None
        elif isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = PostOrderLinePrices.from_dict(_prices)

        customer_article_number = d.pop("customerArticleNumber", UNSET)

        warehouse_instruction = d.pop("warehouseInstruction", UNSET)

        external_id = d.pop("externalId", UNSET)

        _article_item_status = d.pop("articleItemStatus", UNSET)
        article_item_status: Union[Unset, None, CodeNamePair]
        if _article_item_status is None:
            article_item_status = None
        elif isinstance(_article_item_status, Unset):
            article_item_status = UNSET
        else:
            article_item_status = CodeNamePair.from_dict(_article_item_status)

        _line_free_values = d.pop("lineFreeValues", UNSET)
        line_free_values: Union[Unset, None, PostOrderLineFreeValues]
        if _line_free_values is None:
            line_free_values = None
        elif isinstance(_line_free_values, Unset):
            line_free_values = UNSET
        else:
            line_free_values = PostOrderLineFreeValues.from_dict(_line_free_values)

        post_order_line = cls(
            row_number=row_number,
            article_number=article_number,
            number_of_items=number_of_items,
            comment=comment,
            should_be_picked=should_be_picked,
            serial_number=serial_number,
            line_total_customs_value=line_total_customs_value,
            batch_number=batch_number,
            line_type=line_type,
            prices=prices,
            customer_article_number=customer_article_number,
            warehouse_instruction=warehouse_instruction,
            external_id=external_id,
            article_item_status=article_item_status,
            line_free_values=line_free_values,
        )

        return post_order_line
