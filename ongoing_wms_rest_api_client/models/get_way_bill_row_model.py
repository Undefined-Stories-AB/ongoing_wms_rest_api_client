from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_way_bill_row_parcel_type_model import GetWayBillRowParcelTypeModel


T = TypeVar("T", bound="GetWayBillRowModel")


@attr.s(auto_attribs=True)
class GetWayBillRowModel:
    """
    Attributes:
        way_bill_row_id (Union[Unset, int]):
        weight (Union[Unset, None, float]):
        volume (Union[Unset, None, float]):
        length (Union[Unset, None, float]):
        width (Union[Unset, None, float]):
        height (Union[Unset, None, float]):
        number_of_packages (Union[Unset, int]):
        approved_number_of_packages (Union[Unset, None, int]):
        comment (Union[Unset, None, str]):
        category (Union[Unset, None, str]):
        parcel_type (Union[Unset, None, GetWayBillRowParcelTypeModel]):
    """

    way_bill_row_id: Union[Unset, int] = UNSET
    weight: Union[Unset, None, float] = UNSET
    volume: Union[Unset, None, float] = UNSET
    length: Union[Unset, None, float] = UNSET
    width: Union[Unset, None, float] = UNSET
    height: Union[Unset, None, float] = UNSET
    number_of_packages: Union[Unset, int] = UNSET
    approved_number_of_packages: Union[Unset, None, int] = UNSET
    comment: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET
    parcel_type: Union[Unset, None, "GetWayBillRowParcelTypeModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        way_bill_row_id = self.way_bill_row_id
        weight = self.weight
        volume = self.volume
        length = self.length
        width = self.width
        height = self.height
        number_of_packages = self.number_of_packages
        approved_number_of_packages = self.approved_number_of_packages
        comment = self.comment
        category = self.category
        parcel_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parcel_type, Unset):
            parcel_type = self.parcel_type.to_dict() if self.parcel_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if way_bill_row_id is not UNSET:
            field_dict["wayBillRowId"] = way_bill_row_id
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
        if number_of_packages is not UNSET:
            field_dict["numberOfPackages"] = number_of_packages
        if approved_number_of_packages is not UNSET:
            field_dict["approvedNumberOfPackages"] = approved_number_of_packages
        if comment is not UNSET:
            field_dict["comment"] = comment
        if category is not UNSET:
            field_dict["category"] = category
        if parcel_type is not UNSET:
            field_dict["parcelType"] = parcel_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_way_bill_row_parcel_type_model import GetWayBillRowParcelTypeModel

        d = src_dict.copy()
        way_bill_row_id = d.pop("wayBillRowId", UNSET)

        weight = d.pop("weight", UNSET)

        volume = d.pop("volume", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        number_of_packages = d.pop("numberOfPackages", UNSET)

        approved_number_of_packages = d.pop("approvedNumberOfPackages", UNSET)

        comment = d.pop("comment", UNSET)

        category = d.pop("category", UNSET)

        _parcel_type = d.pop("parcelType", UNSET)
        parcel_type: Union[Unset, None, GetWayBillRowParcelTypeModel]
        if _parcel_type is None:
            parcel_type = None
        elif isinstance(_parcel_type, Unset):
            parcel_type = UNSET
        else:
            parcel_type = GetWayBillRowParcelTypeModel.from_dict(_parcel_type)

        get_way_bill_row_model = cls(
            way_bill_row_id=way_bill_row_id,
            weight=weight,
            volume=volume,
            length=length,
            width=width,
            height=height,
            number_of_packages=number_of_packages,
            approved_number_of_packages=approved_number_of_packages,
            comment=comment,
            category=category,
            parcel_type=parcel_type,
        )

        return get_way_bill_row_model
