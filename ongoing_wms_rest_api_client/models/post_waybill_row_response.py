from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostWaybillRowResponse")


@attr.s(auto_attribs=True)
class PostWaybillRowResponse:
    """
    Attributes:
        way_bill_row_id (Union[Unset, int]):
        success (Union[Unset, bool]):
        message (Union[Unset, None, str]):
    """

    way_bill_row_id: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        way_bill_row_id = self.way_bill_row_id
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if way_bill_row_id is not UNSET:
            field_dict["wayBillRowId"] = way_bill_row_id
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        way_bill_row_id = d.pop("wayBillRowId", UNSET)

        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        post_waybill_row_response = cls(
            way_bill_row_id=way_bill_row_id,
            success=success,
            message=message,
        )

        return post_waybill_row_response
