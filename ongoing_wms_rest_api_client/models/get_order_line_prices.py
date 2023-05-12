from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderLinePrices")


@attr.s(auto_attribs=True)
class GetOrderLinePrices:
    """
    Attributes:
        line_price (Union[Unset, None, float]):
        customer_line_price (Union[Unset, None, float]):
        currency_code (Union[Unset, None, str]):
        discount_percentage (Union[Unset, None, float]):
    """

    line_price: Union[Unset, None, float] = UNSET
    customer_line_price: Union[Unset, None, float] = UNSET
    currency_code: Union[Unset, None, str] = UNSET
    discount_percentage: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        line_price = self.line_price
        customer_line_price = self.customer_line_price
        currency_code = self.currency_code
        discount_percentage = self.discount_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if line_price is not UNSET:
            field_dict["linePrice"] = line_price
        if customer_line_price is not UNSET:
            field_dict["customerLinePrice"] = customer_line_price
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_price = d.pop("linePrice", UNSET)

        customer_line_price = d.pop("customerLinePrice", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        get_order_line_prices = cls(
            line_price=line_price,
            customer_line_price=customer_line_price,
            currency_code=currency_code,
            discount_percentage=discount_percentage,
        )

        return get_order_line_prices
