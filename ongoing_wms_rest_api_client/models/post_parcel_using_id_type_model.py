from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_parcel_advanced import PostParcelAdvanced


T = TypeVar("T", bound="PostParcelUsingIdTypeModel")


@attr.s(auto_attribs=True)
class PostParcelUsingIdTypeModel:
    """
    Attributes:
        parcel_number (Union[Unset, None, str]):
        transport_administration_type (Union[Unset, None, str]):
        advanced (Union[Unset, None, PostParcelAdvanced]):
    """

    parcel_number: Union[Unset, None, str] = UNSET
    transport_administration_type: Union[Unset, None, str] = UNSET
    advanced: Union[Unset, None, "PostParcelAdvanced"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        parcel_number = self.parcel_number
        transport_administration_type = self.transport_administration_type
        advanced: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict() if self.advanced else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if parcel_number is not UNSET:
            field_dict["parcelNumber"] = parcel_number
        if transport_administration_type is not UNSET:
            field_dict["transportAdministrationType"] = transport_administration_type
        if advanced is not UNSET:
            field_dict["advanced"] = advanced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_parcel_advanced import PostParcelAdvanced

        d = src_dict.copy()
        parcel_number = d.pop("parcelNumber", UNSET)

        transport_administration_type = d.pop("transportAdministrationType", UNSET)

        _advanced = d.pop("advanced", UNSET)
        advanced: Union[Unset, None, PostParcelAdvanced]
        if _advanced is None:
            advanced = None
        elif isinstance(_advanced, Unset):
            advanced = UNSET
        else:
            advanced = PostParcelAdvanced.from_dict(_advanced)

        post_parcel_using_id_type_model = cls(
            parcel_number=parcel_number,
            transport_administration_type=transport_administration_type,
            advanced=advanced,
        )

        return post_parcel_using_id_type_model
