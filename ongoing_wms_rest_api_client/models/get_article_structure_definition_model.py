from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_structure_row_info_model import GetArticleStructureRowInfoModel


T = TypeVar("T", bound="GetArticleStructureDefinitionModel")


@attr.s(auto_attribs=True)
class GetArticleStructureDefinitionModel:
    """
    Attributes:
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        article_kind (Union[Unset, None, str]):
        rows (Union[Unset, None, List['GetArticleStructureRowInfoModel']]):
    """

    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    article_kind: Union[Unset, None, str] = UNSET
    rows: Union[Unset, None, List["GetArticleStructureRowInfoModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_system_id = self.article_system_id
        article_number = self.article_number
        article_kind = self.article_kind
        rows: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            if self.rows is None:
                rows = None
            else:
                rows = []
                for rows_item_data in self.rows:
                    rows_item = rows_item_data.to_dict()

                    rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if article_kind is not UNSET:
            field_dict["articleKind"] = article_kind
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_structure_row_info_model import GetArticleStructureRowInfoModel

        d = src_dict.copy()
        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        article_kind = d.pop("articleKind", UNSET)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = GetArticleStructureRowInfoModel.from_dict(rows_item_data)

            rows.append(rows_item)

        get_article_structure_definition_model = cls(
            article_system_id=article_system_id,
            article_number=article_number,
            article_kind=article_kind,
            rows=rows,
        )

        return get_article_structure_definition_model
