from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_dangerous_goods_info_model import GetArticleDangerousGoodsInfoModel


T = TypeVar("T", bound="GetArticleDangerousGoodsModel")


@attr.s(auto_attribs=True)
class GetArticleDangerousGoodsModel:
    """
    Attributes:
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        dangerous_goods (Union[Unset, None, GetArticleDangerousGoodsInfoModel]):
    """

    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    dangerous_goods: Union[Unset, None, "GetArticleDangerousGoodsInfoModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_system_id = self.article_system_id
        article_number = self.article_number
        dangerous_goods: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.dangerous_goods, Unset):
            dangerous_goods = self.dangerous_goods.to_dict() if self.dangerous_goods else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if dangerous_goods is not UNSET:
            field_dict["dangerousGoods"] = dangerous_goods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_dangerous_goods_info_model import GetArticleDangerousGoodsInfoModel

        d = src_dict.copy()
        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        _dangerous_goods = d.pop("dangerousGoods", UNSET)
        dangerous_goods: Union[Unset, None, GetArticleDangerousGoodsInfoModel]
        if _dangerous_goods is None:
            dangerous_goods = None
        elif isinstance(_dangerous_goods, Unset):
            dangerous_goods = UNSET
        else:
            dangerous_goods = GetArticleDangerousGoodsInfoModel.from_dict(_dangerous_goods)

        get_article_dangerous_goods_model = cls(
            article_system_id=article_system_id,
            article_number=article_number,
            dangerous_goods=dangerous_goods,
        )

        return get_article_dangerous_goods_model
