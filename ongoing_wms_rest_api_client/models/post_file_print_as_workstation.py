from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFilePrintAsWorkstation")


@attr.s(auto_attribs=True)
class PostFilePrintAsWorkstation:
    """
    Attributes:
        workstation_id (Union[Unset, None, int]):
    """

    workstation_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        workstation_id = self.workstation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if workstation_id is not UNSET:
            field_dict["workstationId"] = workstation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workstation_id = d.pop("workstationId", UNSET)

        post_file_print_as_workstation = cls(
            workstation_id=workstation_id,
        )

        return post_file_print_as_workstation
