from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticleStorageProperties")


@attr.s(auto_attribs=True)
class GetArticleStorageProperties:
    """
    Attributes:
        is_obsolete (Union[Unset, bool]):
    """

    is_obsolete: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_obsolete = self.is_obsolete

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_obsolete is not UNSET:
            field_dict["isObsolete"] = is_obsolete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_obsolete = d.pop("isObsolete", UNSET)

        get_article_storage_properties = cls(
            is_obsolete=is_obsolete,
        )

        return get_article_storage_properties
