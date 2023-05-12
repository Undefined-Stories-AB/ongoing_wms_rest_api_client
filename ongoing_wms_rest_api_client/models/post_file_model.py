from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_file_advanced import PostFileAdvanced


T = TypeVar("T", bound="PostFileModel")


@attr.s(auto_attribs=True)
class PostFileModel:
    """
    Attributes:
        file_name (str):
        mime_type (str):
        file_data_base_64 (str):
        advanced (Union[Unset, None, PostFileAdvanced]):
    """

    file_name: str
    mime_type: str
    file_data_base_64: str
    advanced: Union[Unset, None, "PostFileAdvanced"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name
        mime_type = self.mime_type
        file_data_base_64 = self.file_data_base_64
        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "fileName": file_name,
                "mimeType": mime_type,
                "fileDataBase64": file_data_base_64,
            }
        )
        if advanced is not UNSET:
            field_dict["advanced"] = advanced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_file_advanced import PostFileAdvanced

        d = src_dict.copy()
        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        file_data_base_64 = d.pop("fileDataBase64")

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, PostFileAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = PostFileAdvanced.from_dict(_advanced)

        post_file_model = cls(
            file_name=file_name,
            mime_type=mime_type,
            file_data_base_64=file_data_base_64,
            advanced=advanced,
        )

        return post_file_model
