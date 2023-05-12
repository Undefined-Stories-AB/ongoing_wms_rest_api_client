from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_return_cause_model import GetReturnCauseModel


T = TypeVar("T", bound="GetReturnCausesModel")


@attr.s(auto_attribs=True)
class GetReturnCausesModel:
    """
    Attributes:
        return_causes (Union[Unset, None, List['GetReturnCauseModel']]):
    """

    return_causes: Union[Unset, None, List["GetReturnCauseModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        return_causes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.return_causes, Unset):
            if self.return_causes is None:
                return_causes = None
            else:
                return_causes = []
                for return_causes_item_data in self.return_causes:
                    return_causes_item = return_causes_item_data.to_dict()

                    return_causes.append(return_causes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if return_causes is not UNSET:
            field_dict["returnCauses"] = return_causes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_return_cause_model import GetReturnCauseModel

        d = src_dict.copy()
        return_causes = []
        _return_causes = d.pop("returnCauses", UNSET)
        for return_causes_item_data in _return_causes or []:
            return_causes_item = GetReturnCauseModel.from_dict(return_causes_item_data)

            return_causes.append(return_causes_item)

        get_return_causes_model = cls(
            return_causes=return_causes,
        )

        return get_return_causes_model
