from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticleItemStatusModel")


@attr.s(auto_attribs=True)
class GetArticleItemStatusModel:
    """
    Attributes:
        id (Union[Unset, int]):
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        is_locked (Union[Unset, bool]):
        is_locked_for_sale (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    is_locked_for_sale: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        code = self.code
        name = self.name
        is_locked = self.is_locked
        is_locked_for_sale = self.is_locked_for_sale

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if is_locked_for_sale is not UNSET:
            field_dict["isLockedForSale"] = is_locked_for_sale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        is_locked_for_sale = d.pop("isLockedForSale", UNSET)

        get_article_item_status_model = cls(
            id=id,
            code=code,
            name=name,
            is_locked=is_locked,
            is_locked_for_sale=is_locked_for_sale,
        )

        return get_article_item_status_model
