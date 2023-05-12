from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderCustomsInfo")


@attr.s(auto_attribs=True)
class GetOrderCustomsInfo:
    """
    Attributes:
        customs_value_currency_code (Union[Unset, None, str]):
    """

    customs_value_currency_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        customs_value_currency_code = self.customs_value_currency_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if customs_value_currency_code is not UNSET:
            field_dict["customsValueCurrencyCode"] = customs_value_currency_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customs_value_currency_code = d.pop("customsValueCurrencyCode", UNSET)

        get_order_customs_info = cls(
            customs_value_currency_code=customs_value_currency_code,
        )

        return get_order_customs_info
