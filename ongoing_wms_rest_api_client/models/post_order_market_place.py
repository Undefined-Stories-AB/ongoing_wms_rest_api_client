from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOrderMarketPlace")


@attr.s(auto_attribs=True)
class PostOrderMarketPlace:
    """
    Attributes:
        market_place (Union[Unset, None, str]):
        market_place_order_number (Union[Unset, None, str]):
    """

    market_place: Union[Unset, None, str] = UNSET
    market_place_order_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        market_place = self.market_place
        market_place_order_number = self.market_place_order_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if market_place is not UNSET:
            field_dict["marketPlace"] = market_place
        if market_place_order_number is not UNSET:
            field_dict["marketPlaceOrderNumber"] = market_place_order_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        market_place = d.pop("marketPlace", UNSET)

        market_place_order_number = d.pop("marketPlaceOrderNumber", UNSET)

        post_order_market_place = cls(
            market_place=market_place,
            market_place_order_number=market_place_order_number,
        )

        return post_order_market_place
