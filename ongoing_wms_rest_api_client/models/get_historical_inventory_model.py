from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_historical_inventory_article_model import GetHistoricalInventoryArticleModel


T = TypeVar("T", bound="GetHistoricalInventoryModel")


@attr.s(auto_attribs=True)
class GetHistoricalInventoryModel:
    """
    Attributes:
        articles (Union[Unset, None, List['GetHistoricalInventoryArticleModel']]):
    """

    articles: Union[Unset, None, List["GetHistoricalInventoryArticleModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        articles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.articles, Unset):
            if self.articles is None:
                articles = None
            else:
                articles = []
                for articles_item_data in self.articles:
                    articles_item = articles_item_data.to_dict()

                    articles.append(articles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if articles is not UNSET:
            field_dict["articles"] = articles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_historical_inventory_article_model import GetHistoricalInventoryArticleModel

        d = src_dict.copy()
        articles = []
        _articles = d.pop("articles", UNSET)
        for articles_item_data in _articles or []:
            articles_item = GetHistoricalInventoryArticleModel.from_dict(articles_item_data)

            articles.append(articles_item)

        get_historical_inventory_model = cls(
            articles=articles,
        )

        return get_historical_inventory_model
