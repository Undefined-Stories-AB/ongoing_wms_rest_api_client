from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_article_alternative_supplier import GetArticleAlternativeSupplier


T = TypeVar("T", bound="GetArticleSupplierInfo")


@attr.s(auto_attribs=True)
class GetArticleSupplierInfo:
    """
    Attributes:
        supplier_article_number (Union[Unset, None, str]):
        supplier_number (Union[Unset, None, str]):
        supplier_name (Union[Unset, None, str]):
        alternative_suppliers (Union[Unset, None, List['GetArticleAlternativeSupplier']]):
    """

    supplier_article_number: Union[Unset, None, str] = UNSET
    supplier_number: Union[Unset, None, str] = UNSET
    supplier_name: Union[Unset, None, str] = UNSET
    alternative_suppliers: Union[Unset, None, List["GetArticleAlternativeSupplier"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        supplier_article_number = self.supplier_article_number
        supplier_number = self.supplier_number
        supplier_name = self.supplier_name
        alternative_suppliers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alternative_suppliers, Unset):
            if self.alternative_suppliers is None:
                alternative_suppliers = None
            else:
                alternative_suppliers = []
                for alternative_suppliers_item_data in self.alternative_suppliers:
                    alternative_suppliers_item = alternative_suppliers_item_data.to_dict()

                    alternative_suppliers.append(alternative_suppliers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if supplier_article_number is not UNSET:
            field_dict["supplierArticleNumber"] = supplier_article_number
        if supplier_number is not UNSET:
            field_dict["supplierNumber"] = supplier_number
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if alternative_suppliers is not UNSET:
            field_dict["alternativeSuppliers"] = alternative_suppliers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_article_alternative_supplier import GetArticleAlternativeSupplier

        d = src_dict.copy()
        supplier_article_number = d.pop("supplierArticleNumber", UNSET)

        supplier_number = d.pop("supplierNumber", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        alternative_suppliers = []
        _alternative_suppliers = d.pop("alternativeSuppliers", UNSET)
        for alternative_suppliers_item_data in _alternative_suppliers or []:
            alternative_suppliers_item = GetArticleAlternativeSupplier.from_dict(alternative_suppliers_item_data)

            alternative_suppliers.append(alternative_suppliers_item)

        get_article_supplier_info = cls(
            supplier_article_number=supplier_article_number,
            supplier_number=supplier_number,
            supplier_name=supplier_name,
            alternative_suppliers=alternative_suppliers,
        )

        return get_article_supplier_info
