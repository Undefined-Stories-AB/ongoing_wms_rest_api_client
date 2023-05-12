from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_taric_number import GetArticleTaricNumber


T = TypeVar("T", bound="GetArticleTaricNumbersInfo")


@attr.s(auto_attribs=True)
class GetArticleTaricNumbersInfo:
    """
    Attributes:
        taric_numbers (Union[Unset, None, List['GetArticleTaricNumber']]):
    """

    taric_numbers: Union[Unset, None, List["GetArticleTaricNumber"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        taric_numbers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.taric_numbers, Unset):
            if self.taric_numbers is None:
                taric_numbers = None
            else:
                taric_numbers = []
                for taric_numbers_item_data in self.taric_numbers:
                    taric_numbers_item = taric_numbers_item_data.to_dict()

                    taric_numbers.append(taric_numbers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if taric_numbers is not UNSET:
            field_dict["taricNumbers"] = taric_numbers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_taric_number import GetArticleTaricNumber

        d = src_dict.copy()
        taric_numbers = []
        _taric_numbers = d.pop("taricNumbers", UNSET)
        for taric_numbers_item_data in _taric_numbers or []:
            taric_numbers_item = GetArticleTaricNumber.from_dict(taric_numbers_item_data)

            taric_numbers.append(taric_numbers_item)

        get_article_taric_numbers_info = cls(
            taric_numbers=taric_numbers,
        )

        return get_article_taric_numbers_info
