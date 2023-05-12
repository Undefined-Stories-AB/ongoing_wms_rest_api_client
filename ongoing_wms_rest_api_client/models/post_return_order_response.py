from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostReturnOrderResponse")


@attr.s(auto_attribs=True)
class PostReturnOrderResponse:
    """
    Attributes:
        return_order_id (Union[Unset, None, int]):
        message (Union[Unset, None, str]):
    """

    return_order_id: Union[Unset, None, int] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        return_order_id = self.return_order_id
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if return_order_id is not UNSET:
            field_dict["returnOrderId"] = return_order_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_order_id = d.pop("returnOrderId", UNSET)

        message = d.pop("message", UNSET)

        post_return_order_response = cls(
            return_order_id=return_order_id,
            message=message,
        )

        return post_return_order_response
