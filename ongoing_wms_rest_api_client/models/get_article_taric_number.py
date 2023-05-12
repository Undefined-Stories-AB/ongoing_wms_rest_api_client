from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticleTaricNumber")


@attr.s(auto_attribs=True)
class GetArticleTaricNumber:
    """
    Attributes:
        country_code (Union[Unset, None, str]):
        taric_number (Union[Unset, None, str]):
    """

    country_code: Union[Unset, None, str] = UNSET
    taric_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        country_code = self.country_code
        taric_number = self.taric_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if taric_number is not UNSET:
            field_dict["taricNumber"] = taric_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country_code = d.pop("countryCode", UNSET)

        taric_number = d.pop("taricNumber", UNSET)

        get_article_taric_number = cls(
            country_code=country_code,
            taric_number=taric_number,
        )

        return get_article_taric_number
