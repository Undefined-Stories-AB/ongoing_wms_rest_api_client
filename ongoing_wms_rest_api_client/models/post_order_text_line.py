from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOrderTextLine")


@attr.s(auto_attribs=True)
class PostOrderTextLine:
    """
    Attributes:
        row_number (str):
        comment (Union[Unset, None, str]):
        number_of_items (Union[Unset, float]):
    """

    row_number: str
    comment: Union[Unset, None, str] = UNSET
    number_of_items: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        row_number = self.row_number
        comment = self.comment
        number_of_items = self.number_of_items

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "rowNumber": row_number,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        row_number = d.pop("rowNumber")

        comment = d.pop("comment", UNSET)

        number_of_items = d.pop("numberOfItems", UNSET)

        post_order_text_line = cls(
            row_number=row_number,
            comment=comment,
            number_of_items=number_of_items,
        )

        return post_order_text_line
