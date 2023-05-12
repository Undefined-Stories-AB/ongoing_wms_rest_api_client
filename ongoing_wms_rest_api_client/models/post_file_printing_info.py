from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_file_print_as_user import PostFilePrintAsUser
    from ..models.post_file_print_as_workstation import PostFilePrintAsWorkstation


T = TypeVar("T", bound="PostFilePrintingInfo")


@attr.s(auto_attribs=True)
class PostFilePrintingInfo:
    """
    Attributes:
        report_id (Union[Unset, None, int]):
        print_as_user (Union[Unset, None, PostFilePrintAsUser]):
        print_as_workstation (Union[Unset, None, PostFilePrintAsWorkstation]):
    """

    report_id: Union[Unset, None, int] = UNSET
    print_as_user: Union[Unset, None, "PostFilePrintAsUser"] = UNSET
    print_as_workstation: Union[Unset, None, "PostFilePrintAsWorkstation"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        report_id = self.report_id
        print_as_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.print_as_user, Unset):
            print_as_user = self.print_as_user.to_dict() if self.print_as_user else None

        print_as_workstation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.print_as_workstation, Unset):
            print_as_workstation = self.print_as_workstation.to_dict() if self.print_as_workstation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
        if print_as_user is not UNSET:
            field_dict["printAsUser"] = print_as_user
        if print_as_workstation is not UNSET:
            field_dict["printAsWorkstation"] = print_as_workstation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_file_print_as_user import PostFilePrintAsUser
        from ..models.post_file_print_as_workstation import PostFilePrintAsWorkstation

        d = src_dict.copy()
        report_id = d.pop("reportId", UNSET)

        _print_as_user = d.pop("printAsUser", UNSET)
        print_as_user: Union[Unset, None, PostFilePrintAsUser]
        if _print_as_user is None:
            print_as_user = None
        elif isinstance(_print_as_user, Unset):
            print_as_user = UNSET
        else:
            print_as_user = PostFilePrintAsUser.from_dict(_print_as_user)

        _print_as_workstation = d.pop("printAsWorkstation", UNSET)
        print_as_workstation: Union[Unset, None, PostFilePrintAsWorkstation]
        if _print_as_workstation is None:
            print_as_workstation = None
        elif isinstance(_print_as_workstation, Unset):
            print_as_workstation = UNSET
        else:
            print_as_workstation = PostFilePrintAsWorkstation.from_dict(_print_as_workstation)

        post_file_printing_info = cls(
            report_id=report_id,
            print_as_user=print_as_user,
            print_as_workstation=print_as_workstation,
        )

        return post_file_printing_info
