from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PostArticleTaricNumber")


@attr.s(auto_attribs=True)
class PostArticleTaricNumber:
    """
    Attributes:
        country_code (str):
        taric_number (str):
    """

    country_code: str
    taric_number: str

    def to_dict(self) -> Dict[str, Any]:
        country_code = self.country_code
        taric_number = self.taric_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "countryCode": country_code,
                "taricNumber": taric_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country_code = d.pop("countryCode")

        taric_number = d.pop("taricNumber")

        post_article_taric_number = cls(
            country_code=country_code,
            taric_number=taric_number,
        )

        return post_article_taric_number
