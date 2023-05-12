from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTransporterService")


@attr.s(auto_attribs=True)
class GetTransporterService:
    """
    Attributes:
        transporter_service_name (Union[Unset, None, str]):
        transporter_service_code (Union[Unset, None, str]):
    """

    transporter_service_name: Union[Unset, None, str] = UNSET
    transporter_service_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transporter_service_name = self.transporter_service_name
        transporter_service_code = self.transporter_service_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if transporter_service_name is not UNSET:
            field_dict["transporterServiceName"] = transporter_service_name
        if transporter_service_code is not UNSET:
            field_dict["transporterServiceCode"] = transporter_service_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transporter_service_name = d.pop("transporterServiceName", UNSET)

        transporter_service_code = d.pop("transporterServiceCode", UNSET)

        get_transporter_service = cls(
            transporter_service_name=transporter_service_name,
            transporter_service_code=transporter_service_code,
        )

        return get_transporter_service
