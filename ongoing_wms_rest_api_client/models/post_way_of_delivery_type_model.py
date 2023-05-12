from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PostWayOfDeliveryTypeModel")


@attr.s(auto_attribs=True)
class PostWayOfDeliveryTypeModel:
    """
    Attributes:
        goods_owner_id (int):
        code (str):
        name (str):
    """

    goods_owner_id: int
    code: str
    name: str

    def to_dict(self) -> Dict[str, Any]:
        goods_owner_id = self.goods_owner_id
        code = self.code
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "goodsOwnerId": goods_owner_id,
                "code": code,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        goods_owner_id = d.pop("goodsOwnerId")

        code = d.pop("code")

        name = d.pop("name")

        post_way_of_delivery_type_model = cls(
            goods_owner_id=goods_owner_id,
            code=code,
            name=name,
        )

        return post_way_of_delivery_type_model
