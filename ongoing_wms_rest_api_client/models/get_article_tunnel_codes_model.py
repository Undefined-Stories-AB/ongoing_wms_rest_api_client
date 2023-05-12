from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticleTunnelCodesModel")


@attr.s(auto_attribs=True)
class GetArticleTunnelCodesModel:
    """
    Attributes:
        un_tunnel_code (Union[Unset, None, str]):
    """

    un_tunnel_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        un_tunnel_code = self.un_tunnel_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if un_tunnel_code is not UNSET:
            field_dict["unTunnelCode"] = un_tunnel_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        un_tunnel_code = d.pop("unTunnelCode", UNSET)

        get_article_tunnel_codes_model = cls(
            un_tunnel_code=un_tunnel_code,
        )

        return get_article_tunnel_codes_model
