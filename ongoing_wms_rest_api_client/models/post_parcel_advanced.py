from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_parcel_parcel_status import PostParcelParcelStatus
    from ..models.post_parcel_parcel_type import PostParcelParcelType


T = TypeVar("T", bound="PostParcelAdvanced")


@attr.s(auto_attribs=True)
class PostParcelAdvanced:
    """
    Attributes:
        parcel_type (Union[Unset, None, PostParcelParcelType]):
        parcel_status (Union[Unset, None, PostParcelParcelStatus]):
    """

    parcel_type: Union[Unset, None, "PostParcelParcelType"] = UNSET
    parcel_status: Union[Unset, None, "PostParcelParcelStatus"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        parcel_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parcel_type, Unset):
            parcel_type = self.parcel_type.to_dict() if self.parcel_type else None

        parcel_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parcel_status, Unset):
            parcel_status = self.parcel_status.to_dict() if self.parcel_status else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if parcel_type is not UNSET:
            field_dict["parcelType"] = parcel_type
        if parcel_status is not UNSET:
            field_dict["parcelStatus"] = parcel_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_parcel_parcel_status import PostParcelParcelStatus
        from ..models.post_parcel_parcel_type import PostParcelParcelType

        d = src_dict.copy()
        _parcel_type = d.pop("parcelType", UNSET)
        parcel_type: Union[Unset, None, PostParcelParcelType]
        if _parcel_type is None:
            parcel_type = None
        elif isinstance(_parcel_type, Unset):
            parcel_type = UNSET
        else:
            parcel_type = PostParcelParcelType.from_dict(_parcel_type)

        _parcel_status = d.pop("parcelStatus", UNSET)
        parcel_status: Union[Unset, None, PostParcelParcelStatus]
        if _parcel_status is None:
            parcel_status = None
        elif isinstance(_parcel_status, Unset):
            parcel_status = UNSET
        else:
            parcel_status = PostParcelParcelStatus.from_dict(_parcel_status)

        post_parcel_advanced = cls(
            parcel_type=parcel_type,
            parcel_status=parcel_status,
        )

        return post_parcel_advanced
