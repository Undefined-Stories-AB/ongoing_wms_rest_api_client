from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PatchOrderReportedReturnedNumberOfItemsModel")


@attr.s(auto_attribs=True)
class PatchOrderReportedReturnedNumberOfItemsModel:
    """
    Attributes:
        reported_returned_number_of_items (float):
    """

    reported_returned_number_of_items: float

    def to_dict(self) -> Dict[str, Any]:
        reported_returned_number_of_items = self.reported_returned_number_of_items

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "reportedReturnedNumberOfItems": reported_returned_number_of_items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reported_returned_number_of_items = d.pop("reportedReturnedNumberOfItems")

        patch_order_reported_returned_number_of_items_model = cls(
            reported_returned_number_of_items=reported_returned_number_of_items,
        )

        return patch_order_reported_returned_number_of_items_model
