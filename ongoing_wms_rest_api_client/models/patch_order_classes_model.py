from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_order_class import PostOrderClass


T = TypeVar("T", bound="PatchOrderClassesModel")


@attr.s(auto_attribs=True)
class PatchOrderClassesModel:
    """
    Attributes:
        classes (Union[Unset, None, List['PostOrderClass']]):
    """

    classes: Union[Unset, None, List["PostOrderClass"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        classes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classes, Unset):
            if self.classes is None:
                classes = None
            else:
                classes = []
                for classes_item_data in self.classes:
                    classes_item = classes_item_data.to_dict()

                    classes.append(classes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if classes is not UNSET:
            field_dict["classes"] = classes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_order_class import PostOrderClass

        d = src_dict.copy()
        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = PostOrderClass.from_dict(classes_item_data)

            classes.append(classes_item)

        patch_order_classes_model = cls(
            classes=classes,
        )

        return patch_order_classes_model
