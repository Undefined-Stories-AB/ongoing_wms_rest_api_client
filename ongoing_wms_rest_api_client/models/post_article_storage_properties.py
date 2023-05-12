from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostArticleStorageProperties")


@attr.s(auto_attribs=True)
class PostArticleStorageProperties:
    """
    Attributes:
        is_obsolete (Union[Unset, None, bool]):
        is_serial_number_article (Union[Unset, None, bool]):
        is_batch_article (Union[Unset, None, bool]):
        is_expiry_date_article (Union[Unset, None, bool]):
    """

    is_obsolete: Union[Unset, None, bool] = UNSET
    is_serial_number_article: Union[Unset, None, bool] = UNSET
    is_batch_article: Union[Unset, None, bool] = UNSET
    is_expiry_date_article: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_obsolete = self.is_obsolete
        is_serial_number_article = self.is_serial_number_article
        is_batch_article = self.is_batch_article
        is_expiry_date_article = self.is_expiry_date_article

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_obsolete is not UNSET:
            field_dict["isObsolete"] = is_obsolete
        if is_serial_number_article is not UNSET:
            field_dict["isSerialNumberArticle"] = is_serial_number_article
        if is_batch_article is not UNSET:
            field_dict["isBatchArticle"] = is_batch_article
        if is_expiry_date_article is not UNSET:
            field_dict["isExpiryDateArticle"] = is_expiry_date_article

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_obsolete = d.pop("isObsolete", UNSET)

        is_serial_number_article = d.pop("isSerialNumberArticle", UNSET)

        is_batch_article = d.pop("isBatchArticle", UNSET)

        is_expiry_date_article = d.pop("isExpiryDateArticle", UNSET)

        post_article_storage_properties = cls(
            is_obsolete=is_obsolete,
            is_serial_number_article=is_serial_number_article,
            is_batch_article=is_batch_article,
            is_expiry_date_article=is_expiry_date_article,
        )

        return post_article_storage_properties
