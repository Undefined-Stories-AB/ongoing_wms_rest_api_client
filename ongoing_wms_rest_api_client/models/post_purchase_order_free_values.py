from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPurchaseOrderFreeValues")


@attr.s(auto_attribs=True)
class PostPurchaseOrderFreeValues:
    """
    Attributes:
        free_text_1 (Union[Unset, None, str]):
        free_text_2 (Union[Unset, None, str]):
        free_text_3 (Union[Unset, None, str]):
        free_text_4 (Union[Unset, None, str]):
        free_text_5 (Union[Unset, None, str]):
        free_decimal_1 (Union[Unset, None, float]):
        free_decimal_2 (Union[Unset, None, float]):
        free_boolean_1 (Union[Unset, None, bool]):
        free_boolean_2 (Union[Unset, None, bool]):
    """

    free_text_1: Union[Unset, None, str] = UNSET
    free_text_2: Union[Unset, None, str] = UNSET
    free_text_3: Union[Unset, None, str] = UNSET
    free_text_4: Union[Unset, None, str] = UNSET
    free_text_5: Union[Unset, None, str] = UNSET
    free_decimal_1: Union[Unset, None, float] = UNSET
    free_decimal_2: Union[Unset, None, float] = UNSET
    free_boolean_1: Union[Unset, None, bool] = UNSET
    free_boolean_2: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        free_text_1 = self.free_text_1
        free_text_2 = self.free_text_2
        free_text_3 = self.free_text_3
        free_text_4 = self.free_text_4
        free_text_5 = self.free_text_5
        free_decimal_1 = self.free_decimal_1
        free_decimal_2 = self.free_decimal_2
        free_boolean_1 = self.free_boolean_1
        free_boolean_2 = self.free_boolean_2

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if free_text_1 is not UNSET:
            field_dict["freeText1"] = free_text_1
        if free_text_2 is not UNSET:
            field_dict["freeText2"] = free_text_2
        if free_text_3 is not UNSET:
            field_dict["freeText3"] = free_text_3
        if free_text_4 is not UNSET:
            field_dict["freeText4"] = free_text_4
        if free_text_5 is not UNSET:
            field_dict["freeText5"] = free_text_5
        if free_decimal_1 is not UNSET:
            field_dict["freeDecimal1"] = free_decimal_1
        if free_decimal_2 is not UNSET:
            field_dict["freeDecimal2"] = free_decimal_2
        if free_boolean_1 is not UNSET:
            field_dict["freeBoolean1"] = free_boolean_1
        if free_boolean_2 is not UNSET:
            field_dict["freeBoolean2"] = free_boolean_2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        free_text_1 = d.pop("freeText1", UNSET)

        free_text_2 = d.pop("freeText2", UNSET)

        free_text_3 = d.pop("freeText3", UNSET)

        free_text_4 = d.pop("freeText4", UNSET)

        free_text_5 = d.pop("freeText5", UNSET)

        free_decimal_1 = d.pop("freeDecimal1", UNSET)

        free_decimal_2 = d.pop("freeDecimal2", UNSET)

        free_boolean_1 = d.pop("freeBoolean1", UNSET)

        free_boolean_2 = d.pop("freeBoolean2", UNSET)

        post_purchase_order_free_values = cls(
            free_text_1=free_text_1,
            free_text_2=free_text_2,
            free_text_3=free_text_3,
            free_text_4=free_text_4,
            free_text_5=free_text_5,
            free_decimal_1=free_decimal_1,
            free_decimal_2=free_decimal_2,
            free_boolean_1=free_boolean_1,
            free_boolean_2=free_boolean_2,
        )

        return post_purchase_order_free_values
