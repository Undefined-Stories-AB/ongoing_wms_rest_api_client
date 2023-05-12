from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.post_article_dangerous_goods_model import PostArticleDangerousGoodsModel


T = TypeVar("T", bound="PostArticleDangerousGoodsByArticleNumberModel")


@attr.s(auto_attribs=True)
class PostArticleDangerousGoodsByArticleNumberModel:
    """
    Attributes:
        goods_owner_id (int):
        article_number (str):
        dangerous_goods (PostArticleDangerousGoodsModel):
    """

    goods_owner_id: int
    article_number: str
    dangerous_goods: "PostArticleDangerousGoodsModel"

    def to_dict(self) -> Dict[str, Any]:
        goods_owner_id = self.goods_owner_id
        article_number = self.article_number
        dangerous_goods = self.dangerous_goods.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "goodsOwnerId": goods_owner_id,
                "articleNumber": article_number,
                "dangerousGoods": dangerous_goods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_article_dangerous_goods_model import PostArticleDangerousGoodsModel

        d = src_dict.copy()
        goods_owner_id = d.pop("goodsOwnerId")

        article_number = d.pop("articleNumber")

        dangerous_goods = PostArticleDangerousGoodsModel.from_dict(d.pop("dangerousGoods"))

        post_article_dangerous_goods_by_article_number_model = cls(
            goods_owner_id=goods_owner_id,
            article_number=article_number,
            dangerous_goods=dangerous_goods,
        )

        return post_article_dangerous_goods_by_article_number_model
