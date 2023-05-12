from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOrderReturnTransporter")


@attr.s(auto_attribs=True)
class PostOrderReturnTransporter:
    """
    Attributes:
        transporter_code (Union[Unset, None, str]):
        transporter_service_code (Union[Unset, None, str]):
    """

    transporter_code: Union[Unset, None, str] = UNSET
    transporter_service_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transporter_code = self.transporter_code
        transporter_service_code = self.transporter_service_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if transporter_code is not UNSET:
            field_dict["transporterCode"] = transporter_code
        if transporter_service_code is not UNSET:
            field_dict["transporterServiceCode"] = transporter_service_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transporter_code = d.pop("transporterCode", UNSET)

        transporter_service_code = d.pop("transporterServiceCode", UNSET)

        post_order_return_transporter = cls(
            transporter_code=transporter_code,
            transporter_service_code=transporter_service_code,
        )

        return post_order_return_transporter
