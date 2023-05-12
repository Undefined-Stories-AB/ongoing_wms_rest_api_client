from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostArticleFreeValues")


@attr.s(auto_attribs=True)
class PostArticleFreeValues:
    """
    Attributes:
        free_decimal_1 (Union[Unset, None, float]):
        free_decimal_2 (Union[Unset, None, float]):
        free_decimal_3 (Union[Unset, None, float]):
        free_boolean_1 (Union[Unset, None, bool]):
        free_boolean_2 (Union[Unset, None, bool]):
        free_boolean_3 (Union[Unset, None, bool]):
    """

    free_decimal_1: Union[Unset, None, float] = UNSET
    free_decimal_2: Union[Unset, None, float] = UNSET
    free_decimal_3: Union[Unset, None, float] = UNSET
    free_boolean_1: Union[Unset, None, bool] = UNSET
    free_boolean_2: Union[Unset, None, bool] = UNSET
    free_boolean_3: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        free_decimal_1 = self.free_decimal_1
        free_decimal_2 = self.free_decimal_2
        free_decimal_3 = self.free_decimal_3
        free_boolean_1 = self.free_boolean_1
        free_boolean_2 = self.free_boolean_2
        free_boolean_3 = self.free_boolean_3

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if free_decimal_1 is not UNSET:
            field_dict["freeDecimal1"] = free_decimal_1
        if free_decimal_2 is not UNSET:
            field_dict["freeDecimal2"] = free_decimal_2
        if free_decimal_3 is not UNSET:
            field_dict["freeDecimal3"] = free_decimal_3
        if free_boolean_1 is not UNSET:
            field_dict["freeBoolean1"] = free_boolean_1
        if free_boolean_2 is not UNSET:
            field_dict["freeBoolean2"] = free_boolean_2
        if free_boolean_3 is not UNSET:
            field_dict["freeBoolean3"] = free_boolean_3

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        free_decimal_1 = d.pop("freeDecimal1", UNSET)

        free_decimal_2 = d.pop("freeDecimal2", UNSET)

        free_decimal_3 = d.pop("freeDecimal3", UNSET)

        free_boolean_1 = d.pop("freeBoolean1", UNSET)

        free_boolean_2 = d.pop("freeBoolean2", UNSET)

        free_boolean_3 = d.pop("freeBoolean3", UNSET)

        post_article_free_values = cls(
            free_decimal_1=free_decimal_1,
            free_decimal_2=free_decimal_2,
            free_decimal_3=free_decimal_3,
            free_boolean_1=free_boolean_1,
            free_boolean_2=free_boolean_2,
            free_boolean_3=free_boolean_3,
        )

        return post_article_free_values
