from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PostOrderTransporterSenderPaysPays")


@attr.s(auto_attribs=True)
class PostOrderTransporterSenderPaysPays:
    """
    Attributes:
        edi_code (str):
    """

    edi_code: str

    def to_dict(self) -> Dict[str, Any]:
        edi_code = self.edi_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ediCode": edi_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        edi_code = d.pop("ediCode")

        post_order_transporter_sender_pays_pays = cls(
            edi_code=edi_code,
        )

        return post_order_transporter_sender_pays_pays
