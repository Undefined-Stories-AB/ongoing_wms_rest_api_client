from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_file_printing_info import PostFilePrintingInfo


T = TypeVar("T", bound="PostFileAdvanced")


@attr.s(auto_attribs=True)
class PostFileAdvanced:
    """
    Attributes:
        printing_info (Union[Unset, None, PostFilePrintingInfo]):
    """

    printing_info: Union[Unset, None, "PostFilePrintingInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        printing_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.printing_info, Unset):
            printing_info = self.printing_info.to_dict() if self.printing_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if printing_info is not UNSET:
            field_dict["printingInfo"] = printing_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_file_printing_info import PostFilePrintingInfo

        d = src_dict.copy()
        _printing_info = d.pop("printingInfo", UNSET)
        printing_info: Union[Unset, None, PostFilePrintingInfo]
        if _printing_info is None:
            printing_info = None
        elif isinstance(_printing_info, Unset):
            printing_info = UNSET
        else:
            printing_info = PostFilePrintingInfo.from_dict(_printing_info)

        post_file_advanced = cls(
            printing_info=printing_info,
        )

        return post_file_advanced
