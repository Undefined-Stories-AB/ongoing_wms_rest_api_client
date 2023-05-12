from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="PortArticleArticleClassesModel")


@attr.s(auto_attribs=True)
class PortArticleArticleClassesModel:
    """
    Attributes:
        article_class_ids (List[int]):
    """

    article_class_ids: List[int]

    def to_dict(self) -> Dict[str, Any]:
        article_class_ids = self.article_class_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "articleClassIds": article_class_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        article_class_ids = cast(List[int], d.pop("articleClassIds"))

        port_article_article_classes_model = cls(
            article_class_ids=article_class_ids,
        )

        return port_article_article_classes_model
