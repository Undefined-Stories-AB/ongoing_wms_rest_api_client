from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_class_model import GetArticleClassModel


T = TypeVar("T", bound="GetArticleClassesModel")


@attr.s(auto_attribs=True)
class GetArticleClassesModel:
    """
    Attributes:
        article_classes (Union[Unset, None, List['GetArticleClassModel']]):
    """

    article_classes: Union[Unset, None, List["GetArticleClassModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_classes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.article_classes, Unset):
            if self.article_classes is None:
                article_classes = None
            else:
                article_classes = []
                for article_classes_item_data in self.article_classes:
                    article_classes_item = article_classes_item_data.to_dict()

                    article_classes.append(article_classes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_classes is not UNSET:
            field_dict["articleClasses"] = article_classes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_class_model import GetArticleClassModel

        d = src_dict.copy()
        article_classes = []
        _article_classes = d.pop("articleClasses", UNSET)
        for article_classes_item_data in _article_classes or []:
            article_classes_item = GetArticleClassModel.from_dict(article_classes_item_data)

            article_classes.append(article_classes_item)

        get_article_classes_model = cls(
            article_classes=article_classes,
        )

        return get_article_classes_model
