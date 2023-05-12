from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_proper_shipping_name_model import GetArticleProperShippingNameModel
    from ..models.get_article_un_number_model import GetArticleUnNumberModel


T = TypeVar("T", bound="GetArticleDangerousGoodsInfoModel")


@attr.s(auto_attribs=True)
class GetArticleDangerousGoodsInfoModel:
    """
    Attributes:
        un_number (Union[Unset, None, GetArticleUnNumberModel]):
        un_package_type (Union[Unset, None, str]):
        un_label_numbers (Union[Unset, None, str]):
        un_is_marine_hazard (Union[Unset, bool]):
        dangerous_goods_coefficient (Union[Unset, None, float]):
        ems_code (Union[Unset, None, str]):
        un_proper_shipping_names (Union[Unset, None, List['GetArticleProperShippingNameModel']]):
    """

    un_number: Union[Unset, None, "GetArticleUnNumberModel"] = UNSET
    un_package_type: Union[Unset, None, str] = UNSET
    un_label_numbers: Union[Unset, None, str] = UNSET
    un_is_marine_hazard: Union[Unset, bool] = UNSET
    dangerous_goods_coefficient: Union[Unset, None, float] = UNSET
    ems_code: Union[Unset, None, str] = UNSET
    un_proper_shipping_names: Union[Unset, None, List["GetArticleProperShippingNameModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        un_number: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.un_number, Unset):
            un_number = self.un_number.to_dict() if self.un_number else None

        un_package_type = self.un_package_type
        un_label_numbers = self.un_label_numbers
        un_is_marine_hazard = self.un_is_marine_hazard
        dangerous_goods_coefficient = self.dangerous_goods_coefficient
        ems_code = self.ems_code
        un_proper_shipping_names: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.un_proper_shipping_names, Unset):
            if self.un_proper_shipping_names is None:
                un_proper_shipping_names = None
            else:
                un_proper_shipping_names = []
                for un_proper_shipping_names_item_data in self.un_proper_shipping_names:
                    un_proper_shipping_names_item = un_proper_shipping_names_item_data.to_dict()

                    un_proper_shipping_names.append(un_proper_shipping_names_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if un_number is not UNSET:
            field_dict["unNumber"] = un_number
        if un_package_type is not UNSET:
            field_dict["unPackageType"] = un_package_type
        if un_label_numbers is not UNSET:
            field_dict["unLabelNumbers"] = un_label_numbers
        if un_is_marine_hazard is not UNSET:
            field_dict["unIsMarineHazard"] = un_is_marine_hazard
        if dangerous_goods_coefficient is not UNSET:
            field_dict["dangerousGoodsCoefficient"] = dangerous_goods_coefficient
        if ems_code is not UNSET:
            field_dict["emsCode"] = ems_code
        if un_proper_shipping_names is not UNSET:
            field_dict["unProperShippingNames"] = un_proper_shipping_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_proper_shipping_name_model import GetArticleProperShippingNameModel
        from ..models.get_article_un_number_model import GetArticleUnNumberModel

        d = src_dict.copy()
        _un_number = d.pop("unNumber", UNSET)
        un_number: Union[Unset, None, GetArticleUnNumberModel]
        if _un_number is None:
            un_number = None
        elif isinstance(_un_number, Unset):
            un_number = UNSET
        else:
            un_number = GetArticleUnNumberModel.from_dict(_un_number)

        un_package_type = d.pop("unPackageType", UNSET)

        un_label_numbers = d.pop("unLabelNumbers", UNSET)

        un_is_marine_hazard = d.pop("unIsMarineHazard", UNSET)

        dangerous_goods_coefficient = d.pop("dangerousGoodsCoefficient", UNSET)

        ems_code = d.pop("emsCode", UNSET)

        un_proper_shipping_names = []
        _un_proper_shipping_names = d.pop("unProperShippingNames", UNSET)
        for un_proper_shipping_names_item_data in _un_proper_shipping_names or []:
            un_proper_shipping_names_item = GetArticleProperShippingNameModel.from_dict(
                un_proper_shipping_names_item_data
            )

            un_proper_shipping_names.append(un_proper_shipping_names_item)

        get_article_dangerous_goods_info_model = cls(
            un_number=un_number,
            un_package_type=un_package_type,
            un_label_numbers=un_label_numbers,
            un_is_marine_hazard=un_is_marine_hazard,
            dangerous_goods_coefficient=dangerous_goods_coefficient,
            ems_code=ems_code,
            un_proper_shipping_names=un_proper_shipping_names,
        )

        return get_article_dangerous_goods_info_model
