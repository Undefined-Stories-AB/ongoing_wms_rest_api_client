from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.warehouse_address_model import WarehouseAddressModel


T = TypeVar("T", bound="WarehouseModel")


@attr.s(auto_attribs=True)
class WarehouseModel:
    """
    Attributes:
        id (Union[Unset, int]):
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        address (Union[Unset, None, WarehouseAddressModel]):
    """

    id: Union[Unset, int] = UNSET
    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    address: Union[Unset, None, "WarehouseAddressModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        code = self.code
        name = self.name
        address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict() if self.address else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.warehouse_address_model import WarehouseAddressModel

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, None, WarehouseAddressModel]
        if _address is None:
            address = None
        elif isinstance(_address, Unset):
            address = UNSET
        else:
            address = WarehouseAddressModel.from_dict(_address)

        warehouse_model = cls(
            id=id,
            code=code,
            name=name,
            address=address,
        )

        return warehouse_model
