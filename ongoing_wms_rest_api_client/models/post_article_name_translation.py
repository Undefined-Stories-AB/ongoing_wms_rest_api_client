from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostArticleNameTranslation")


@attr.s(auto_attribs=True)
class PostArticleNameTranslation:
    """
    Attributes:
        language_code (Union[Unset, None, str]):
        article_name (Union[Unset, None, str]):
    """

    language_code: Union[Unset, None, str] = UNSET
    article_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        language_code = self.language_code
        article_name = self.article_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if article_name is not UNSET:
            field_dict["articleName"] = article_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_code = d.pop("languageCode", UNSET)

        article_name = d.pop("articleName", UNSET)

        post_article_name_translation = cls(
            language_code=language_code,
            article_name=article_name,
        )

        return post_article_name_translation
