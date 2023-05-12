from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_transporter_service import GetTransporterService


T = TypeVar("T", bound="GetTransporterContract")


@attr.s(auto_attribs=True)
class GetTransporterContract:
    """
    Attributes:
        edi_code (Union[Unset, None, str]):
        transporter_name (Union[Unset, None, str]):
        transporter_code (Union[Unset, None, str]):
        transporter_service_code (Union[Unset, None, str]):
        transporter_services (Union[Unset, None, List['GetTransporterService']]):
    """

    edi_code: Union[Unset, None, str] = UNSET
    transporter_name: Union[Unset, None, str] = UNSET
    transporter_code: Union[Unset, None, str] = UNSET
    transporter_service_code: Union[Unset, None, str] = UNSET
    transporter_services: Union[Unset, None, List["GetTransporterService"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        edi_code = self.edi_code
        transporter_name = self.transporter_name
        transporter_code = self.transporter_code
        transporter_service_code = self.transporter_service_code
        transporter_services: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transporter_services, Unset):
            if self.transporter_services is None:
                transporter_services = None
            else:
                transporter_services = []
                for transporter_services_item_data in self.transporter_services:
                    transporter_services_item = transporter_services_item_data.to_dict()

                    transporter_services.append(transporter_services_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if edi_code is not UNSET:
            field_dict["ediCode"] = edi_code
        if transporter_name is not UNSET:
            field_dict["transporterName"] = transporter_name
        if transporter_code is not UNSET:
            field_dict["transporterCode"] = transporter_code
        if transporter_service_code is not UNSET:
            field_dict["transporterServiceCode"] = transporter_service_code
        if transporter_services is not UNSET:
            field_dict["transporterServices"] = transporter_services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_transporter_service import GetTransporterService

        d = src_dict.copy()
        edi_code = d.pop("ediCode", UNSET)

        transporter_name = d.pop("transporterName", UNSET)

        transporter_code = d.pop("transporterCode", UNSET)

        transporter_service_code = d.pop("transporterServiceCode", UNSET)

        transporter_services = []
        _transporter_services = d.pop("transporterServices", UNSET)
        for transporter_services_item_data in _transporter_services or []:
            transporter_services_item = GetTransporterService.from_dict(transporter_services_item_data)

            transporter_services.append(transporter_services_item)

        get_transporter_contract = cls(
            edi_code=edi_code,
            transporter_name=transporter_name,
            transporter_code=transporter_code,
            transporter_service_code=transporter_service_code,
            transporter_services=transporter_services,
        )

        return get_transporter_contract
