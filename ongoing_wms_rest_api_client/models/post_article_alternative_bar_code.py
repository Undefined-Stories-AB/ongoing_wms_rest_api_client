from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair


T = TypeVar("T", bound="PostArticleAlternativeBarCode")


@attr.s(auto_attribs=True)
class PostArticleAlternativeBarCode:
    """
    Attributes:
        bar_code (Union[Unset, None, str]):
        quantity_per_bar_code (Union[Unset, None, float]):
        bar_code_type (Union[Unset, None, CodeNamePair]):
    """

    bar_code: Union[Unset, None, str] = UNSET
    quantity_per_bar_code: Union[Unset, None, float] = UNSET
    bar_code_type: Union[Unset, None, "CodeNamePair"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bar_code = self.bar_code
        quantity_per_bar_code = self.quantity_per_bar_code
        bar_code_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.bar_code_type, Unset):
            bar_code_type = self.bar_code_type.to_dict() if self.bar_code_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bar_code is not UNSET:
            field_dict["barCode"] = bar_code
        if quantity_per_bar_code is not UNSET:
            field_dict["quantityPerBarCode"] = quantity_per_bar_code
        if bar_code_type is not UNSET:
            field_dict["barCodeType"] = bar_code_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair

        d = src_dict.copy()
        bar_code = d.pop("barCode", UNSET)

        quantity_per_bar_code = d.pop("quantityPerBarCode", UNSET)

        _bar_code_type = d.pop("barCodeType", UNSET)
        bar_code_type: Union[Unset, None, CodeNamePair]
        if _bar_code_type is None:
            bar_code_type = None
        elif isinstance(_bar_code_type, Unset):
            bar_code_type = UNSET
        else:
            bar_code_type = CodeNamePair.from_dict(_bar_code_type)

        post_article_alternative_bar_code = cls(
            bar_code=bar_code,
            quantity_per_bar_code=quantity_per_bar_code,
            bar_code_type=bar_code_type,
        )

        return post_article_alternative_bar_code
