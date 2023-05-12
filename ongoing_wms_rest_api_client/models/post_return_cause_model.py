from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostReturnCauseModel")


@attr.s(auto_attribs=True)
class PostReturnCauseModel:
    """
    Attributes:
        goods_owner_id (int):
        code (str):
        name (str):
        is_remove_cause (Union[Unset, None, bool]):
        is_change_cause (Union[Unset, None, bool]):
        is_return_comment_mandatory (Union[Unset, None, bool]):
    """

    goods_owner_id: int
    code: str
    name: str
    is_remove_cause: Union[Unset, None, bool] = UNSET
    is_change_cause: Union[Unset, None, bool] = UNSET
    is_return_comment_mandatory: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner_id = self.goods_owner_id
        code = self.code
        name = self.name
        is_remove_cause = self.is_remove_cause
        is_change_cause = self.is_change_cause
        is_return_comment_mandatory = self.is_return_comment_mandatory

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "goodsOwnerId": goods_owner_id,
                "code": code,
                "name": name,
            }
        )
        if is_remove_cause is not UNSET:
            field_dict["isRemoveCause"] = is_remove_cause
        if is_change_cause is not UNSET:
            field_dict["isChangeCause"] = is_change_cause
        if is_return_comment_mandatory is not UNSET:
            field_dict["isReturnCommentMandatory"] = is_return_comment_mandatory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        goods_owner_id = d.pop("goodsOwnerId")

        code = d.pop("code")

        name = d.pop("name")

        is_remove_cause = d.pop("isRemoveCause", UNSET)

        is_change_cause = d.pop("isChangeCause", UNSET)

        is_return_comment_mandatory = d.pop("isReturnCommentMandatory", UNSET)

        post_return_cause_model = cls(
            goods_owner_id=goods_owner_id,
            code=code,
            name=name,
            is_remove_cause=is_remove_cause,
            is_change_cause=is_change_cause,
            is_return_comment_mandatory=is_return_comment_mandatory,
        )

        return post_return_cause_model
