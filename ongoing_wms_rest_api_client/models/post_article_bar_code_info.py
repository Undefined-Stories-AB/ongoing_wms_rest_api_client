from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_article_alternative_bar_code import PostArticleAlternativeBarCode


T = TypeVar("T", bound="PostArticleBarCodeInfo")


@attr.s(auto_attribs=True)
class PostArticleBarCodeInfo:
    """
    Attributes:
        bar_code (Union[Unset, None, str]):
        bar_code_package (Union[Unset, None, str]):
        bar_code_pallet (Union[Unset, None, str]):
        alternative_bar_codes (Union[Unset, None, List['PostArticleAlternativeBarCode']]):
    """

    bar_code: Union[Unset, None, str] = UNSET
    bar_code_package: Union[Unset, None, str] = UNSET
    bar_code_pallet: Union[Unset, None, str] = UNSET
    alternative_bar_codes: Union[Unset, None, List["PostArticleAlternativeBarCode"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bar_code = self.bar_code
        bar_code_package = self.bar_code_package
        bar_code_pallet = self.bar_code_pallet
        alternative_bar_codes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alternative_bar_codes, Unset):
            if self.alternative_bar_codes is None:
                alternative_bar_codes = None
            else:
                alternative_bar_codes = []
                for alternative_bar_codes_item_data in self.alternative_bar_codes:
                    alternative_bar_codes_item = alternative_bar_codes_item_data.to_dict()

                    alternative_bar_codes.append(alternative_bar_codes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bar_code is not UNSET:
            field_dict["barCode"] = bar_code
        if bar_code_package is not UNSET:
            field_dict["barCodePackage"] = bar_code_package
        if bar_code_pallet is not UNSET:
            field_dict["barCodePallet"] = bar_code_pallet
        if alternative_bar_codes is not UNSET:
            field_dict["alternativeBarCodes"] = alternative_bar_codes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_article_alternative_bar_code import PostArticleAlternativeBarCode

        d = src_dict.copy()
        bar_code = d.pop("barCode", UNSET)

        bar_code_package = d.pop("barCodePackage", UNSET)

        bar_code_pallet = d.pop("barCodePallet", UNSET)

        alternative_bar_codes = []
        _alternative_bar_codes = d.pop("alternativeBarCodes", UNSET)
        for alternative_bar_codes_item_data in _alternative_bar_codes or []:
            alternative_bar_codes_item = PostArticleAlternativeBarCode.from_dict(alternative_bar_codes_item_data)

            alternative_bar_codes.append(alternative_bar_codes_item)

        post_article_bar_code_info = cls(
            bar_code=bar_code,
            bar_code_package=bar_code_package,
            bar_code_pallet=bar_code_pallet,
            alternative_bar_codes=alternative_bar_codes,
        )

        return post_article_bar_code_info
