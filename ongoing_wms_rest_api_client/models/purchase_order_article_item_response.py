from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_order_article_item_response_message import PurchaseOrderArticleItemResponseMessage


T = TypeVar("T", bound="PurchaseOrderArticleItemResponse")


@attr.s(auto_attribs=True)
class PurchaseOrderArticleItemResponse:
    """
    Attributes:
        success (Union[Unset, bool]):
        messages (Union[Unset, None, List['PurchaseOrderArticleItemResponseMessage']]):
    """

    success: Union[Unset, bool] = UNSET
    messages: Union[Unset, None, List["PurchaseOrderArticleItemResponseMessage"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        messages: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            if self.messages is None:
                messages = None
            else:
                messages = []
                for messages_item_data in self.messages:
                    messages_item = messages_item_data.to_dict()

                    messages.append(messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_order_article_item_response_message import PurchaseOrderArticleItemResponseMessage

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = PurchaseOrderArticleItemResponseMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        purchase_order_article_item_response = cls(
            success=success,
            messages=messages,
        )

        return purchase_order_article_item_response
