from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetReturnCauseModel")


@attr.s(auto_attribs=True)
class GetReturnCauseModel:
    """
    Attributes:
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        is_remove_cause (Union[Unset, bool]):
        is_change_cause (Union[Unset, bool]):
        is_return_comment_mandatory (Union[Unset, bool]):
        id (Union[Unset, int]):
    """

    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_remove_cause: Union[Unset, bool] = UNSET
    is_change_cause: Union[Unset, bool] = UNSET
    is_return_comment_mandatory: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        is_remove_cause = self.is_remove_cause
        is_change_cause = self.is_change_cause
        is_return_comment_mandatory = self.is_return_comment_mandatory
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if is_remove_cause is not UNSET:
            field_dict["isRemoveCause"] = is_remove_cause
        if is_change_cause is not UNSET:
            field_dict["isChangeCause"] = is_change_cause
        if is_return_comment_mandatory is not UNSET:
            field_dict["isReturnCommentMandatory"] = is_return_comment_mandatory
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        is_remove_cause = d.pop("isRemoveCause", UNSET)

        is_change_cause = d.pop("isChangeCause", UNSET)

        is_return_comment_mandatory = d.pop("isReturnCommentMandatory", UNSET)

        id = d.pop("id", UNSET)

        get_return_cause_model = cls(
            code=code,
            name=name,
            is_remove_cause=is_remove_cause,
            is_change_cause=is_change_cause,
            is_return_comment_mandatory=is_return_comment_mandatory,
            id=id,
        )

        return get_return_cause_model
