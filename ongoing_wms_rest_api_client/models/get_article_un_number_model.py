from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_tunnel_codes_model import GetArticleTunnelCodesModel


T = TypeVar("T", bound="GetArticleUnNumberModel")


@attr.s(auto_attribs=True)
class GetArticleUnNumberModel:
    """
    Attributes:
        un_number (Union[Unset, None, str]):
        un_tunnel_codes (Union[Unset, None, List['GetArticleTunnelCodesModel']]):
        un_class_number (Union[Unset, None, str]):
    """

    un_number: Union[Unset, None, str] = UNSET
    un_tunnel_codes: Union[Unset, None, List["GetArticleTunnelCodesModel"]] = UNSET
    un_class_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        un_number = self.un_number
        un_tunnel_codes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.un_tunnel_codes, Unset):
            if self.un_tunnel_codes is None:
                un_tunnel_codes = None
            else:
                un_tunnel_codes = []
                for un_tunnel_codes_item_data in self.un_tunnel_codes:
                    un_tunnel_codes_item = un_tunnel_codes_item_data.to_dict()

                    un_tunnel_codes.append(un_tunnel_codes_item)

        un_class_number = self.un_class_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if un_number is not UNSET:
            field_dict["unNumber"] = un_number
        if un_tunnel_codes is not UNSET:
            field_dict["unTunnelCodes"] = un_tunnel_codes
        if un_class_number is not UNSET:
            field_dict["unClassNumber"] = un_class_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_tunnel_codes_model import GetArticleTunnelCodesModel

        d = src_dict.copy()
        un_number = d.pop("unNumber", UNSET)

        un_tunnel_codes = []
        _un_tunnel_codes = d.pop("unTunnelCodes", UNSET)
        for un_tunnel_codes_item_data in _un_tunnel_codes or []:
            un_tunnel_codes_item = GetArticleTunnelCodesModel.from_dict(un_tunnel_codes_item_data)

            un_tunnel_codes.append(un_tunnel_codes_item)

        un_class_number = d.pop("unClassNumber", UNSET)

        get_article_un_number_model = cls(
            un_number=un_number,
            un_tunnel_codes=un_tunnel_codes,
            un_class_number=un_class_number,
        )

        return get_article_un_number_model
