from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPurchaseOrderFreeValues")


@attr.s(auto_attribs=True)
class GetPurchaseOrderFreeValues:
    """
    Attributes:
        free_text_1 (Union[Unset, None, str]):
        free_text_2 (Union[Unset, None, str]):
        free_text_3 (Union[Unset, None, str]):
        free_text_4 (Union[Unset, None, str]):
        free_text_5 (Union[Unset, None, str]):
        free_decimal_1 (Union[Unset, None, float]):
        free_decimal_2 (Union[Unset, None, float]):
        free_bool_1 (Union[Unset, None, bool]):
        free_bool_2 (Union[Unset, None, bool]):
    """

    free_text_1: Union[Unset, None, str] = UNSET
    free_text_2: Union[Unset, None, str] = UNSET
    free_text_3: Union[Unset, None, str] = UNSET
    free_text_4: Union[Unset, None, str] = UNSET
    free_text_5: Union[Unset, None, str] = UNSET
    free_decimal_1: Union[Unset, None, float] = UNSET
    free_decimal_2: Union[Unset, None, float] = UNSET
    free_bool_1: Union[Unset, None, bool] = UNSET
    free_bool_2: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        free_text_1 = self.free_text_1
        free_text_2 = self.free_text_2
        free_text_3 = self.free_text_3
        free_text_4 = self.free_text_4
        free_text_5 = self.free_text_5
        free_decimal_1 = self.free_decimal_1
        free_decimal_2 = self.free_decimal_2
        free_bool_1 = self.free_bool_1
        free_bool_2 = self.free_bool_2

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
        if free_bool_1 is not UNSET:
            field_dict["freeBool1"] = free_bool_1
        if free_bool_2 is not UNSET:
            field_dict["freeBool2"] = free_bool_2

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

        free_bool_1 = d.pop("freeBool1", UNSET)

        free_bool_2 = d.pop("freeBool2", UNSET)

        get_purchase_order_free_values = cls(
            free_text_1=free_text_1,
            free_text_2=free_text_2,
            free_text_3=free_text_3,
            free_text_4=free_text_4,
            free_text_5=free_text_5,
            free_decimal_1=free_decimal_1,
            free_decimal_2=free_decimal_2,
            free_bool_1=free_bool_1,
            free_bool_2=free_bool_2,
        )

        return get_purchase_order_free_values
