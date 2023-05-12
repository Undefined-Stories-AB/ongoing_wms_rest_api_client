from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PostOrderTransporterThirdPartyPays")


@attr.s(auto_attribs=True)
class PostOrderTransporterThirdPartyPays:
    """
    Attributes:
        customer_number (str):
    """

    customer_number: str

    def to_dict(self) -> Dict[str, Any]:
        customer_number = self.customer_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "customerNumber": customer_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_number = d.pop("customerNumber")

        post_order_transporter_third_party_pays = cls(
            customer_number=customer_number,
        )

        return post_order_transporter_third_party_pays
