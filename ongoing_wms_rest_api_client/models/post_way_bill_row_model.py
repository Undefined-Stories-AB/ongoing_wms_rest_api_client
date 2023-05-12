from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_waybill_parcel_parcel_type import PostWaybillParcelParcelType


T = TypeVar("T", bound="PostWayBillRowModel")


@attr.s(auto_attribs=True)
class PostWayBillRowModel:
    """
    Attributes:
        number_of_packages (int):
        parcel_type (PostWaybillParcelParcelType):
        weight (Union[Unset, None, float]):
        volume (Union[Unset, None, float]):
        length (Union[Unset, None, float]):
        width (Union[Unset, None, float]):
        height (Union[Unset, None, float]):
        approved_number_of_packages (Union[Unset, None, int]):
        load_meters (Union[Unset, None, float]):
        comment (Union[Unset, None, str]):
        category (Union[Unset, None, str]):
    """

    number_of_packages: int
    parcel_type: "PostWaybillParcelParcelType"
    weight: Union[Unset, None, float] = UNSET
    volume: Union[Unset, None, float] = UNSET
    length: Union[Unset, None, float] = UNSET
    width: Union[Unset, None, float] = UNSET
    height: Union[Unset, None, float] = UNSET
    approved_number_of_packages: Union[Unset, None, int] = UNSET
    load_meters: Union[Unset, None, float] = UNSET
    comment: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number_of_packages = self.number_of_packages
        parcel_type = self.parcel_type.to_dict()

        weight = self.weight
        volume = self.volume
        length = self.length
        width = self.width
        height = self.height
        approved_number_of_packages = self.approved_number_of_packages
        load_meters = self.load_meters
        comment = self.comment
        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "numberOfPackages": number_of_packages,
                "parcelType": parcel_type,
            }
        )
        if weight is not UNSET:
            field_dict["weight"] = weight
        if volume is not UNSET:
            field_dict["volume"] = volume
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if approved_number_of_packages is not UNSET:
            field_dict["approvedNumberOfPackages"] = approved_number_of_packages
        if load_meters is not UNSET:
            field_dict["loadMeters"] = load_meters
        if comment is not UNSET:
            field_dict["comment"] = comment
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_waybill_parcel_parcel_type import PostWaybillParcelParcelType

        d = src_dict.copy()
        number_of_packages = d.pop("numberOfPackages")

        parcel_type = PostWaybillParcelParcelType.from_dict(d.pop("parcelType"))

        weight = d.pop("weight", UNSET)

        volume = d.pop("volume", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        approved_number_of_packages = d.pop("approvedNumberOfPackages", UNSET)

        load_meters = d.pop("loadMeters", UNSET)

        comment = d.pop("comment", UNSET)

        category = d.pop("category", UNSET)

        post_way_bill_row_model = cls(
            number_of_packages=number_of_packages,
            parcel_type=parcel_type,
            weight=weight,
            volume=volume,
            length=length,
            width=width,
            height=height,
            approved_number_of_packages=approved_number_of_packages,
            load_meters=load_meters,
            comment=comment,
            category=category,
        )

        return post_way_bill_row_model
