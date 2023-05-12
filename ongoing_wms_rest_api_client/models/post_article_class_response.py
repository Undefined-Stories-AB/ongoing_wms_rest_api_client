from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostArticleClassResponse")


@attr.s(auto_attribs=True)
class PostArticleClassResponse:
    """
    Attributes:
        article_class_id (Union[Unset, None, int]):
        success (Union[Unset, bool]):
        message (Union[Unset, None, str]):
    """

    article_class_id: Union[Unset, None, int] = UNSET
    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_class_id = self.article_class_id
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_class_id is not UNSET:
            field_dict["articleClassId"] = article_class_id
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        article_class_id = d.pop("articleClassId", UNSET)

        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        post_article_class_response = cls(
            article_class_id=article_class_id,
            success=success,
            message=message,
        )

        return post_article_class_response
