from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_purchase_order_article_item_model import PostPurchaseOrderArticleItemModel


T = TypeVar("T", bound="PostPurchaseOrderArticleItemsModel")


@attr.s(auto_attribs=True)
class PostPurchaseOrderArticleItemsModel:
    """
    Attributes:
        items (Union[Unset, None, List['PostPurchaseOrderArticleItemModel']]):
    """

    items: Union[Unset, None, List["PostPurchaseOrderArticleItemModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = []
                for items_item_data in self.items:
                    items_item = items_item_data.to_dict()

                    items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_purchase_order_article_item_model import PostPurchaseOrderArticleItemModel

        d = src_dict.copy()
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = PostPurchaseOrderArticleItemModel.from_dict(items_item_data)

            items.append(items_item)

        post_purchase_order_article_items_model = cls(
            items=items,
        )

        return post_purchase_order_article_items_model
