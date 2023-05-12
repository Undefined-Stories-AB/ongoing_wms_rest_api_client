from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_purchase_order_type_model import GetPurchaseOrderTypeModel


T = TypeVar("T", bound="GetPurchaseOrderTypesModel")


@attr.s(auto_attribs=True)
class GetPurchaseOrderTypesModel:
    """
    Attributes:
        purchase_order_types (Union[Unset, None, List['GetPurchaseOrderTypeModel']]):
    """

    purchase_order_types: Union[Unset, None, List["GetPurchaseOrderTypeModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_types: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_order_types, Unset):
            if self.purchase_order_types is None:
                purchase_order_types = None
            else:
                purchase_order_types = []
                for purchase_order_types_item_data in self.purchase_order_types:
                    purchase_order_types_item = purchase_order_types_item_data.to_dict()

                    purchase_order_types.append(purchase_order_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if purchase_order_types is not UNSET:
            field_dict["purchaseOrderTypes"] = purchase_order_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_purchase_order_type_model import GetPurchaseOrderTypeModel

        d = src_dict.copy()
        purchase_order_types = []
        _purchase_order_types = d.pop("purchaseOrderTypes", UNSET)
        for purchase_order_types_item_data in _purchase_order_types or []:
            purchase_order_types_item = GetPurchaseOrderTypeModel.from_dict(purchase_order_types_item_data)

            purchase_order_types.append(purchase_order_types_item)

        get_purchase_order_types_model = cls(
            purchase_order_types=purchase_order_types,
        )

        return get_purchase_order_types_model
