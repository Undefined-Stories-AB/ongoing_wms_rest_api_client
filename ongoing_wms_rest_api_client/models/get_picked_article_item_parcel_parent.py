from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_picked_article_item_parent_parcel_advanced import GetPickedArticleItemParentParcelAdvanced
    from ..models.get_picked_article_item_parent_parcel_type import GetPickedArticleItemParentParcelType


T = TypeVar("T", bound="GetPickedArticleItemParcelParent")


@attr.s(auto_attribs=True)
class GetPickedArticleItemParcelParent:
    """
    Attributes:
        id (Union[Unset, int]):
        parcel_number (Union[Unset, None, str]):
        parcel_type (Union[Unset, None, GetPickedArticleItemParentParcelType]):
        advanced (Union[Unset, None, GetPickedArticleItemParentParcelAdvanced]):
    """

    id: Union[Unset, int] = UNSET
    parcel_number: Union[Unset, None, str] = UNSET
    parcel_type: Union[Unset, None, "GetPickedArticleItemParentParcelType"] = UNSET
    advanced: Union[Unset, None, "GetPickedArticleItemParentParcelAdvanced"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parcel_number = self.parcel_number
        parcel_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parcel_type, Unset):
            parcel_type = self.parcel_type.to_dict() if self.parcel_type else None

        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parcel_number is not UNSET:
            field_dict["parcelNumber"] = parcel_number
        if parcel_type is not UNSET:
            field_dict["parcelType"] = parcel_type
        if advanced is not UNSET:
            field_dict["advanced"] = advanced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_picked_article_item_parent_parcel_advanced import GetPickedArticleItemParentParcelAdvanced
        from ..models.get_picked_article_item_parent_parcel_type import GetPickedArticleItemParentParcelType

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parcel_number = d.pop("parcelNumber", UNSET)

        _parcel_type = d.pop("parcelType", UNSET)
        parcel_type: Union[Unset, None, GetPickedArticleItemParentParcelType]
        if _parcel_type is None:
            parcel_type = None
        elif isinstance(_parcel_type, Unset):
            parcel_type = UNSET
        else:
            parcel_type = GetPickedArticleItemParentParcelType.from_dict(_parcel_type)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, GetPickedArticleItemParentParcelAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = GetPickedArticleItemParentParcelAdvanced.from_dict(_advanced)

        get_picked_article_item_parcel_parent = cls(
            id=id,
            parcel_number=parcel_number,
            parcel_type=parcel_type,
            advanced=advanced,
        )

        return get_picked_article_item_parcel_parent
