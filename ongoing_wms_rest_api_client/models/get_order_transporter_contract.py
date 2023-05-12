from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderTransporterContract")


@attr.s(auto_attribs=True)
class GetOrderTransporterContract:
    """
    Attributes:
        comment (Union[Unset, None, str]):
    """

    comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comment = d.pop("comment", UNSET)

        get_order_transporter_contract = cls(
            comment=comment,
        )

        return get_order_transporter_contract
