from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostArticleProperShippingNameModel")


@attr.s(auto_attribs=True)
class PostArticleProperShippingNameModel:
    """
    Attributes:
        language_code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
    """

    language_code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        language_code = self.language_code
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_code = d.pop("languageCode", UNSET)

        name = d.pop("name", UNSET)

        post_article_proper_shipping_name_model = cls(
            language_code=language_code,
            name=name,
        )

        return post_article_proper_shipping_name_model
