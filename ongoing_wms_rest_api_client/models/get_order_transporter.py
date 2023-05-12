from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_transporter_contract import GetOrderTransporterContract


T = TypeVar("T", bound="GetOrderTransporter")


@attr.s(auto_attribs=True)
class GetOrderTransporter:
    """
    Attributes:
        transporter_name (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        code (Union[Unset, None, str]):
        service_code (Union[Unset, None, str]):
        transporter_contract (Union[Unset, None, GetOrderTransporterContract]):
        service_comment (Union[Unset, None, str]):
    """

    transporter_name: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    code: Union[Unset, None, str] = UNSET
    service_code: Union[Unset, None, str] = UNSET
    transporter_contract: Union[Unset, None, "GetOrderTransporterContract"] = UNSET
    service_comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transporter_name = self.transporter_name
        name = self.name
        code = self.code
        service_code = self.service_code
        transporter_contract: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transporter_contract, Unset):
            transporter_contract = self.transporter_contract.to_dict() if self.transporter_contract else None

        service_comment = self.service_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if transporter_name is not UNSET:
            field_dict["transporterName"] = transporter_name
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if service_code is not UNSET:
            field_dict["serviceCode"] = service_code
        if transporter_contract is not UNSET:
            field_dict["transporterContract"] = transporter_contract
        if service_comment is not UNSET:
            field_dict["serviceComment"] = service_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_order_transporter_contract import GetOrderTransporterContract

        d = src_dict.copy()
        transporter_name = d.pop("transporterName", UNSET)

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        service_code = d.pop("serviceCode", UNSET)

        _transporter_contract = d.pop("transporterContract", UNSET)
        transporter_contract: Union[Unset, None, GetOrderTransporterContract]
        if _transporter_contract is None:
            transporter_contract = None
        elif isinstance(_transporter_contract, Unset):
            transporter_contract = UNSET
        else:
            transporter_contract = GetOrderTransporterContract.from_dict(_transporter_contract)

        service_comment = d.pop("serviceComment", UNSET)

        get_order_transporter = cls(
            transporter_name=transporter_name,
            name=name,
            code=code,
            service_code=service_code,
            transporter_contract=transporter_contract,
            service_comment=service_comment,
        )

        return get_order_transporter
