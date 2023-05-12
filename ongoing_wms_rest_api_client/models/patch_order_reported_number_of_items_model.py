from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchOrderReportedNumberOfItemsModel")


@attr.s(auto_attribs=True)
class PatchOrderReportedNumberOfItemsModel:
    """
    Attributes:
        reported_number_of_items (float):
    """

    reported_number_of_items: float

    def to_dict(self) -> Dict[str, Any]:
        reported_number_of_items = self.reported_number_of_items

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "reportedNumberOfItems": reported_number_of_items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reported_number_of_items = d.pop("reportedNumberOfItems")

        patch_order_reported_number_of_items_model = cls(
            reported_number_of_items=reported_number_of_items,
        )

        return patch_order_reported_number_of_items_model
