from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PostFileNoFilenameModel")


@attr.s(auto_attribs=True)
class PostFileNoFilenameModel:
    """
    Attributes:
        mime_type (str):
        file_data_base_64 (str):
    """

    mime_type: str
    file_data_base_64: str

    def to_dict(self) -> Dict[str, Any]:
        mime_type = self.mime_type
        file_data_base_64 = self.file_data_base_64

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "mimeType": mime_type,
                "fileDataBase64": file_data_base_64,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mime_type = d.pop("mimeType")

        file_data_base_64 = d.pop("fileDataBase64")

        post_file_no_filename_model = cls(
            mime_type=mime_type,
            file_data_base_64=file_data_base_64,
        )

        return post_file_no_filename_model
