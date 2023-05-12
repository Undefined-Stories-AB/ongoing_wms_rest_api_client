from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_class_model import GetOrderClassModel


T = TypeVar("T", bound="GetOrderClassesModel")


@attr.s(auto_attribs=True)
class GetOrderClassesModel:
    """
    Attributes:
        order_classes (Union[Unset, None, List['GetOrderClassModel']]):
    """

    order_classes: Union[Unset, None, List["GetOrderClassModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_classes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_classes, Unset):
            if self.order_classes is None:
                order_classes = None
            else:
                order_classes = []
                for order_classes_item_data in self.order_classes:
                    order_classes_item = order_classes_item_data.to_dict()

                    order_classes.append(order_classes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_classes is not UNSET:
            field_dict["orderClasses"] = order_classes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_order_class_model import GetOrderClassModel

        d = src_dict.copy()
        order_classes = []
        _order_classes = d.pop("orderClasses", UNSET)
        for order_classes_item_data in _order_classes or []:
            order_classes_item = GetOrderClassModel.from_dict(order_classes_item_data)

            order_classes.append(order_classes_item)

        get_order_classes_model = cls(
            order_classes=order_classes,
        )

        return get_order_classes_model
