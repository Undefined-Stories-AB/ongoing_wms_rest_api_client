from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_item_status_model import GetArticleItemStatusModel


T = TypeVar("T", bound="ArticleItemStatusModel")


@attr.s(auto_attribs=True)
class ArticleItemStatusModel:
    """
    Attributes:
        article_item_statuses (Union[Unset, None, List['GetArticleItemStatusModel']]):
    """

    article_item_statuses: Union[Unset, None, List["GetArticleItemStatusModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_item_statuses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.article_item_statuses, Unset):
            if self.article_item_statuses is None:
                article_item_statuses = None
            else:
                article_item_statuses = []
                for article_item_statuses_item_data in self.article_item_statuses:
                    article_item_statuses_item = article_item_statuses_item_data.to_dict()

                    article_item_statuses.append(article_item_statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_item_statuses is not UNSET:
            field_dict["articleItemStatuses"] = article_item_statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_item_status_model import GetArticleItemStatusModel

        d = src_dict.copy()
        article_item_statuses = []
        _article_item_statuses = d.pop("articleItemStatuses", UNSET)
        for article_item_statuses_item_data in _article_item_statuses or []:
            article_item_statuses_item = GetArticleItemStatusModel.from_dict(article_item_statuses_item_data)

            article_item_statuses.append(article_item_statuses_item)

        article_item_status_model = cls(
            article_item_statuses=article_item_statuses,
        )

        return article_item_status_model
