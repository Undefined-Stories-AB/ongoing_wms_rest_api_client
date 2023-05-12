from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPickedArticleItemHandling")


@attr.s(auto_attribs=True)
class GetPickedArticleItemHandling:
    """
    Attributes:
        picked_by_user_id (Union[Unset, None, int]):
        packed_by_user_id (Union[Unset, None, int]):
    """

    picked_by_user_id: Union[Unset, None, int] = UNSET
    packed_by_user_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        picked_by_user_id = self.picked_by_user_id
        packed_by_user_id = self.packed_by_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if picked_by_user_id is not UNSET:
            field_dict["pickedByUserId"] = picked_by_user_id
        if packed_by_user_id is not UNSET:
            field_dict["packedByUserId"] = packed_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        picked_by_user_id = d.pop("pickedByUserId", UNSET)

        packed_by_user_id = d.pop("packedByUserId", UNSET)

        get_picked_article_item_handling = cls(
            picked_by_user_id=picked_by_user_id,
            packed_by_user_id=packed_by_user_id,
        )

        return get_picked_article_item_handling
