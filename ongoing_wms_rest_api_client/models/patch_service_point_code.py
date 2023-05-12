from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchServicePointCode")


@attr.s(auto_attribs=True)
class PatchServicePointCode:
    """
    Attributes:
        service_point_code (str):
    """

    service_point_code: str

    def to_dict(self) -> Dict[str, Any]:
        service_point_code = self.service_point_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "servicePointCode": service_point_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_point_code = d.pop("servicePointCode")

        patch_service_point_code = cls(
            service_point_code=service_point_code,
        )

        return patch_service_point_code
