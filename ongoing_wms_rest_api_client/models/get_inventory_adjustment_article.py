from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInventoryAdjustmentArticle")


@attr.s(auto_attribs=True)
class GetInventoryAdjustmentArticle:
    """
    Attributes:
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        article_name (Union[Unset, None, str]):
        product_code (Union[Unset, None, str]):
    """

    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    article_name: Union[Unset, None, str] = UNSET
    product_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_system_id = self.article_system_id
        article_number = self.article_number
        article_name = self.article_name
        product_code = self.product_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if article_name is not UNSET:
            field_dict["articleName"] = article_name
        if product_code is not UNSET:
            field_dict["productCode"] = product_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        article_name = d.pop("articleName", UNSET)

        product_code = d.pop("productCode", UNSET)

        get_inventory_adjustment_article = cls(
            article_system_id=article_system_id,
            article_number=article_number,
            article_name=article_name,
            product_code=product_code,
        )

        return get_inventory_adjustment_article
