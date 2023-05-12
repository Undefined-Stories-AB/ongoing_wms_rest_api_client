from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_article_structure_kind import PostArticleStructureKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_article_structure_row import PostArticleStructureRow


T = TypeVar("T", bound="PostArticleStructureSpecification")


@attr.s(auto_attribs=True)
class PostArticleStructureSpecification:
    """
    Attributes:
        article_kind (Union[Unset, PostArticleStructureKind]):
        rows (Union[Unset, None, List['PostArticleStructureRow']]):
    """

    article_kind: Union[Unset, PostArticleStructureKind] = UNSET
    rows: Union[Unset, None, List["PostArticleStructureRow"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        article_kind: Union[Unset, str] = UNSET
        if not isinstance(self.article_kind, Unset):
            article_kind = self.article_kind.value

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
        if article_kind is not UNSET:
            field_dict["articleKind"] = article_kind
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_article_structure_row import PostArticleStructureRow

        d = src_dict.copy()
        _article_kind = d.pop("articleKind", UNSET)
        article_kind: Union[Unset, PostArticleStructureKind]
        if isinstance(_article_kind, Unset):
            article_kind = UNSET
        else:
            article_kind = PostArticleStructureKind(_article_kind)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = PostArticleStructureRow.from_dict(rows_item_data)

            rows.append(rows_item)

        post_article_structure_specification = cls(
            article_kind=article_kind,
            rows=rows,
        )

        return post_article_structure_specification
