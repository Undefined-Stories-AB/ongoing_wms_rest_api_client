from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFileModel")


@attr.s(auto_attribs=True)
class GetFileModel:
    """
    Attributes:
        file_id (Union[Unset, int]):
        order_id (Union[Unset, None, int]):
        article_system_id (Union[Unset, None, int]):
        file_name (Union[Unset, None, str]):
        mime_type (Union[Unset, None, str]):
        file_data_base_64 (Union[Unset, None, str]):
        purchase_order_id (Union[Unset, None, int]):
    """

    file_id: Union[Unset, int] = UNSET
    order_id: Union[Unset, None, int] = UNSET
    article_system_id: Union[Unset, None, int] = UNSET
    file_name: Union[Unset, None, str] = UNSET
    mime_type: Union[Unset, None, str] = UNSET
    file_data_base_64: Union[Unset, None, str] = UNSET
    purchase_order_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file_id = self.file_id
        order_id = self.order_id
        article_system_id = self.article_system_id
        file_name = self.file_name
        mime_type = self.mime_type
        file_data_base_64 = self.file_data_base_64
        purchase_order_id = self.purchase_order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if file_data_base_64 is not UNSET:
            field_dict["fileDataBase64"] = file_data_base_64
        if purchase_order_id is not UNSET:
            field_dict["purchaseOrderId"] = purchase_order_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_id = d.pop("fileId", UNSET)

        order_id = d.pop("orderId", UNSET)

        article_system_id = d.pop("articleSystemId", UNSET)

        file_name = d.pop("fileName", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        file_data_base_64 = d.pop("fileDataBase64", UNSET)

        purchase_order_id = d.pop("purchaseOrderId", UNSET)

        get_file_model = cls(
            file_id=file_id,
            order_id=order_id,
            article_system_id=article_system_id,
            file_name=file_name,
            mime_type=mime_type,
            file_data_base_64=file_data_base_64,
            purchase_order_id=purchase_order_id,
        )

        return get_file_model
