import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.get_article_bar_code_info import GetArticleBarCodeInfo
    from ..models.get_article_class import GetArticleClass
    from ..models.get_article_default_location import GetArticleDefaultLocation
    from ..models.get_article_free_values import GetArticleFreeValues
    from ..models.get_article_goods_owner import GetArticleGoodsOwner
    from ..models.get_article_inventory_info import GetArticleInventoryInfo
    from ..models.get_article_storage_properties import GetArticleStorageProperties
    from ..models.get_article_supplier_info import GetArticleSupplierInfo
    from ..models.get_article_taric_numbers_info import GetArticleTaricNumbersInfo


T = TypeVar("T", bound="GetArticleModel")


@attr.s(auto_attribs=True)
class GetArticleModel:
    """
    Attributes:
        goods_owner (Union[Unset, None, GetArticleGoodsOwner]):
        article_system_id (Union[Unset, int]):
        article_number (Union[Unset, None, str]):
        article_name (Union[Unset, None, str]):
        product_code (Union[Unset, None, str]):
        unit_code (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        is_stock_article (Union[Unset, None, bool]):
        is_active (Union[Unset, None, bool]):
        supplier_info (Union[Unset, None, GetArticleSupplierInfo]):
        bar_code_info (Union[Unset, None, GetArticleBarCodeInfo]):
        quantity_per_package (Union[Unset, None, int]):
        quantity_per_pallet (Union[Unset, None, int]):
        weight (Union[Unset, None, float]):
        length (Union[Unset, None, float]):
        width (Union[Unset, None, float]):
        height (Union[Unset, None, float]):
        volume (Union[Unset, None, float]):
        purchase_price (Union[Unset, None, float]):
        stock_valuation_price (Union[Unset, None, float]):
        customer_price (Union[Unset, None, float]):
        purcase_currency_code (Union[Unset, None, str]):
        country_of_origin_code (Union[Unset, None, str]):
        statistics_number (Union[Unset, None, str]):
        article_group (Union[Unset, None, CodeNamePair]):
        article_category (Union[Unset, None, CodeNamePair]):
        inventory_info (Union[Unset, None, GetArticleInventoryInfo]):
        article_data_last_updated (Union[Unset, None, datetime.datetime]):
        article_kind (Union[Unset, None, str]):
        stock_limit (Union[Unset, None, int]):
        minimum_reorder_quantity (Union[Unset, None, float]):
        net_weight (Union[Unset, None, float]):
        free_values (Union[Unset, None, GetArticleFreeValues]):
        sub_quantity_per_item (Union[Unset, None, float]):
        classes (Union[Unset, None, List['GetArticleClass']]):
        customs_description (Union[Unset, None, str]):
        taric_numbers_info (Union[Unset, None, GetArticleTaricNumbersInfo]):
        default_location_max_number_of_items (Union[Unset, None, float]):
        default_location_stock_limit (Union[Unset, None, float]):
        link_to_picture (Union[Unset, None, str]):
        storage_properties (Union[Unset, None, GetArticleStorageProperties]):
        default_location (Union[Unset, None, GetArticleDefaultLocation]):
    """

    goods_owner: Union[Unset, None, "GetArticleGoodsOwner"] = UNSET
    article_system_id: Union[Unset, int] = UNSET
    article_number: Union[Unset, None, str] = UNSET
    article_name: Union[Unset, None, str] = UNSET
    product_code: Union[Unset, None, str] = UNSET
    unit_code: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    is_stock_article: Union[Unset, None, bool] = UNSET
    is_active: Union[Unset, None, bool] = UNSET
    supplier_info: Union[Unset, None, "GetArticleSupplierInfo"] = UNSET
    bar_code_info: Union[Unset, None, "GetArticleBarCodeInfo"] = UNSET
    quantity_per_package: Union[Unset, None, int] = UNSET
    quantity_per_pallet: Union[Unset, None, int] = UNSET
    weight: Union[Unset, None, float] = UNSET
    length: Union[Unset, None, float] = UNSET
    width: Union[Unset, None, float] = UNSET
    height: Union[Unset, None, float] = UNSET
    volume: Union[Unset, None, float] = UNSET
    purchase_price: Union[Unset, None, float] = UNSET
    stock_valuation_price: Union[Unset, None, float] = UNSET
    customer_price: Union[Unset, None, float] = UNSET
    purcase_currency_code: Union[Unset, None, str] = UNSET
    country_of_origin_code: Union[Unset, None, str] = UNSET
    statistics_number: Union[Unset, None, str] = UNSET
    article_group: Union[Unset, None, "CodeNamePair"] = UNSET
    article_category: Union[Unset, None, "CodeNamePair"] = UNSET
    inventory_info: Union[Unset, None, "GetArticleInventoryInfo"] = UNSET
    article_data_last_updated: Union[Unset, None, datetime.datetime] = UNSET
    article_kind: Union[Unset, None, str] = UNSET
    stock_limit: Union[Unset, None, int] = UNSET
    minimum_reorder_quantity: Union[Unset, None, float] = UNSET
    net_weight: Union[Unset, None, float] = UNSET
    free_values: Union[Unset, None, "GetArticleFreeValues"] = UNSET
    sub_quantity_per_item: Union[Unset, None, float] = UNSET
    classes: Union[Unset, None, List["GetArticleClass"]] = UNSET
    customs_description: Union[Unset, None, str] = UNSET
    taric_numbers_info: Union[Unset, None, "GetArticleTaricNumbersInfo"] = UNSET
    default_location_max_number_of_items: Union[Unset, None, float] = UNSET
    default_location_stock_limit: Union[Unset, None, float] = UNSET
    link_to_picture: Union[Unset, None, str] = UNSET
    storage_properties: Union[Unset, None, "GetArticleStorageProperties"] = UNSET
    default_location: Union[Unset, None, "GetArticleDefaultLocation"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.goods_owner, Unset):
            goods_owner = self.goods_owner.to_dict() if self.goods_owner else None

        article_system_id = self.article_system_id
        article_number = self.article_number
        article_name = self.article_name
        product_code = self.product_code
        unit_code = self.unit_code
        description = self.description
        is_stock_article = self.is_stock_article
        is_active = self.is_active
        supplier_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_info, Unset):
            supplier_info = self.supplier_info.to_dict() if self.supplier_info else None

        bar_code_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.bar_code_info, Unset):
            bar_code_info = self.bar_code_info.to_dict() if self.bar_code_info else None

        quantity_per_package = self.quantity_per_package
        quantity_per_pallet = self.quantity_per_pallet
        weight = self.weight
        length = self.length
        width = self.width
        height = self.height
        volume = self.volume
        purchase_price = self.purchase_price
        stock_valuation_price = self.stock_valuation_price
        customer_price = self.customer_price
        purcase_currency_code = self.purcase_currency_code
        country_of_origin_code = self.country_of_origin_code
        statistics_number = self.statistics_number
        article_group: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_group, Unset):
            article_group = self.article_group.to_dict() if self.article_group else None

        article_category: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_category, Unset):
            article_category = self.article_category.to_dict() if self.article_category else None

        inventory_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_info, Unset):
            inventory_info = self.inventory_info.to_dict() if self.inventory_info else None

        article_data_last_updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.article_data_last_updated, Unset):
            article_data_last_updated = (
                self.article_data_last_updated.isoformat() if self.article_data_last_updated else None
            )

        article_kind = self.article_kind
        stock_limit = self.stock_limit
        minimum_reorder_quantity = self.minimum_reorder_quantity
        net_weight = self.net_weight
        free_values: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.free_values, Unset):
            free_values = self.free_values.to_dict() if self.free_values else None

        sub_quantity_per_item = self.sub_quantity_per_item
        classes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classes, Unset):
            if self.classes is None:
                classes = None
            else:
                classes = []
                for classes_item_data in self.classes:
                    classes_item = classes_item_data.to_dict()

                    classes.append(classes_item)

        customs_description = self.customs_description
        taric_numbers_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.taric_numbers_info, Unset):
            taric_numbers_info = self.taric_numbers_info.to_dict() if self.taric_numbers_info else None

        default_location_max_number_of_items = self.default_location_max_number_of_items
        default_location_stock_limit = self.default_location_stock_limit
        link_to_picture = self.link_to_picture
        storage_properties: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.storage_properties, Unset):
            storage_properties = self.storage_properties.to_dict() if self.storage_properties else None

        default_location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.default_location, Unset):
            default_location = self.default_location.to_dict() if self.default_location else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if goods_owner is not UNSET:
            field_dict["goodsOwner"] = goods_owner
        if article_system_id is not UNSET:
            field_dict["articleSystemId"] = article_system_id
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if article_name is not UNSET:
            field_dict["articleName"] = article_name
        if product_code is not UNSET:
            field_dict["productCode"] = product_code
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if description is not UNSET:
            field_dict["description"] = description
        if is_stock_article is not UNSET:
            field_dict["isStockArticle"] = is_stock_article
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if supplier_info is not UNSET:
            field_dict["supplierInfo"] = supplier_info
        if bar_code_info is not UNSET:
            field_dict["barCodeInfo"] = bar_code_info
        if quantity_per_package is not UNSET:
            field_dict["quantityPerPackage"] = quantity_per_package
        if quantity_per_pallet is not UNSET:
            field_dict["quantityPerPallet"] = quantity_per_pallet
        if weight is not UNSET:
            field_dict["weight"] = weight
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if volume is not UNSET:
            field_dict["volume"] = volume
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if stock_valuation_price is not UNSET:
            field_dict["stockValuationPrice"] = stock_valuation_price
        if customer_price is not UNSET:
            field_dict["customerPrice"] = customer_price
        if purcase_currency_code is not UNSET:
            field_dict["purcaseCurrencyCode"] = purcase_currency_code
        if country_of_origin_code is not UNSET:
            field_dict["countryOfOriginCode"] = country_of_origin_code
        if statistics_number is not UNSET:
            field_dict["statisticsNumber"] = statistics_number
        if article_group is not UNSET:
            field_dict["articleGroup"] = article_group
        if article_category is not UNSET:
            field_dict["articleCategory"] = article_category
        if inventory_info is not UNSET:
            field_dict["inventoryInfo"] = inventory_info
        if article_data_last_updated is not UNSET:
            field_dict["articleDataLastUpdated"] = article_data_last_updated
        if article_kind is not UNSET:
            field_dict["articleKind"] = article_kind
        if stock_limit is not UNSET:
            field_dict["stockLimit"] = stock_limit
        if minimum_reorder_quantity is not UNSET:
            field_dict["minimumReorderQuantity"] = minimum_reorder_quantity
        if net_weight is not UNSET:
            field_dict["netWeight"] = net_weight
        if free_values is not UNSET:
            field_dict["freeValues"] = free_values
        if sub_quantity_per_item is not UNSET:
            field_dict["subQuantityPerItem"] = sub_quantity_per_item
        if classes is not UNSET:
            field_dict["classes"] = classes
        if customs_description is not UNSET:
            field_dict["customsDescription"] = customs_description
        if taric_numbers_info is not UNSET:
            field_dict["taricNumbersInfo"] = taric_numbers_info
        if default_location_max_number_of_items is not UNSET:
            field_dict["defaultLocationMaxNumberOfItems"] = default_location_max_number_of_items
        if default_location_stock_limit is not UNSET:
            field_dict["defaultLocationStockLimit"] = default_location_stock_limit
        if link_to_picture is not UNSET:
            field_dict["linkToPicture"] = link_to_picture
        if storage_properties is not UNSET:
            field_dict["storageProperties"] = storage_properties
        if default_location is not UNSET:
            field_dict["defaultLocation"] = default_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.get_article_bar_code_info import GetArticleBarCodeInfo
        from ..models.get_article_class import GetArticleClass
        from ..models.get_article_default_location import GetArticleDefaultLocation
        from ..models.get_article_free_values import GetArticleFreeValues
        from ..models.get_article_goods_owner import GetArticleGoodsOwner
        from ..models.get_article_inventory_info import GetArticleInventoryInfo
        from ..models.get_article_storage_properties import GetArticleStorageProperties
        from ..models.get_article_supplier_info import GetArticleSupplierInfo
        from ..models.get_article_taric_numbers_info import GetArticleTaricNumbersInfo

        d = src_dict.copy()
        _goods_owner = d.pop("goodsOwner", UNSET)
        goods_owner: Union[Unset, None, GetArticleGoodsOwner]
        if _goods_owner is None:
            goods_owner = None
        elif isinstance(_goods_owner, Unset):
            goods_owner = UNSET
        else:
            goods_owner = GetArticleGoodsOwner.from_dict(_goods_owner)

        article_system_id = d.pop("articleSystemId", UNSET)

        article_number = d.pop("articleNumber", UNSET)

        article_name = d.pop("articleName", UNSET)

        product_code = d.pop("productCode", UNSET)

        unit_code = d.pop("unitCode", UNSET)

        description = d.pop("description", UNSET)

        is_stock_article = d.pop("isStockArticle", UNSET)

        is_active = d.pop("isActive", UNSET)

        _supplier_info = d.pop("supplierInfo", UNSET)
        supplier_info: Union[Unset, None, GetArticleSupplierInfo]
        if _supplier_info is None:
            supplier_info = None
        elif isinstance(_supplier_info, Unset):
            supplier_info = UNSET
        else:
            supplier_info = GetArticleSupplierInfo.from_dict(_supplier_info)

        _bar_code_info = d.pop("barCodeInfo", UNSET)
        bar_code_info: Union[Unset, None, GetArticleBarCodeInfo]
        if _bar_code_info is None:
            bar_code_info = None
        elif isinstance(_bar_code_info, Unset):
            bar_code_info = UNSET
        else:
            bar_code_info = GetArticleBarCodeInfo.from_dict(_bar_code_info)

        quantity_per_package = d.pop("quantityPerPackage", UNSET)

        quantity_per_pallet = d.pop("quantityPerPallet", UNSET)

        weight = d.pop("weight", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        volume = d.pop("volume", UNSET)

        purchase_price = d.pop("purchasePrice", UNSET)

        stock_valuation_price = d.pop("stockValuationPrice", UNSET)

        customer_price = d.pop("customerPrice", UNSET)

        purcase_currency_code = d.pop("purcaseCurrencyCode", UNSET)

        country_of_origin_code = d.pop("countryOfOriginCode", UNSET)

        statistics_number = d.pop("statisticsNumber", UNSET)

        _article_group = d.pop("articleGroup", UNSET)
        article_group: Union[Unset, None, CodeNamePair]
        if _article_group is None:
            article_group = None
        elif isinstance(_article_group, Unset):
            article_group = UNSET
        else:
            article_group = CodeNamePair.from_dict(_article_group)

        _article_category = d.pop("articleCategory", UNSET)
        article_category: Union[Unset, None, CodeNamePair]
        if _article_category is None:
            article_category = None
        elif isinstance(_article_category, Unset):
            article_category = UNSET
        else:
            article_category = CodeNamePair.from_dict(_article_category)

        _inventory_info = d.pop("inventoryInfo", UNSET)
        inventory_info: Union[Unset, None, GetArticleInventoryInfo]
        if _inventory_info is None:
            inventory_info = None
        elif isinstance(_inventory_info, Unset):
            inventory_info = UNSET
        else:
            inventory_info = GetArticleInventoryInfo.from_dict(_inventory_info)

        _article_data_last_updated = d.pop("articleDataLastUpdated", UNSET)
        article_data_last_updated: Union[Unset, None, datetime.datetime]
        if _article_data_last_updated is None:
            article_data_last_updated = None
        elif isinstance(_article_data_last_updated, Unset):
            article_data_last_updated = UNSET
        else:
            article_data_last_updated = isoparse(_article_data_last_updated)

        article_kind = d.pop("articleKind", UNSET)

        stock_limit = d.pop("stockLimit", UNSET)

        minimum_reorder_quantity = d.pop("minimumReorderQuantity", UNSET)

        net_weight = d.pop("netWeight", UNSET)

        _free_values = d.pop("freeValues", UNSET)
        free_values: Union[Unset, None, GetArticleFreeValues]
        if _free_values is None:
            free_values = None
        elif isinstance(_free_values, Unset):
            free_values = UNSET
        else:
            free_values = GetArticleFreeValues.from_dict(_free_values)

        sub_quantity_per_item = d.pop("subQuantityPerItem", UNSET)

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = GetArticleClass.from_dict(classes_item_data)

            classes.append(classes_item)

        customs_description = d.pop("customsDescription", UNSET)

        _taric_numbers_info = d.pop("taricNumbersInfo", UNSET)
        taric_numbers_info: Union[Unset, None, GetArticleTaricNumbersInfo]
        if _taric_numbers_info is None:
            taric_numbers_info = None
        elif isinstance(_taric_numbers_info, Unset):
            taric_numbers_info = UNSET
        else:
            taric_numbers_info = GetArticleTaricNumbersInfo.from_dict(_taric_numbers_info)

        default_location_max_number_of_items = d.pop("defaultLocationMaxNumberOfItems", UNSET)

        default_location_stock_limit = d.pop("defaultLocationStockLimit", UNSET)

        link_to_picture = d.pop("linkToPicture", UNSET)

        _storage_properties = d.pop("storageProperties", UNSET)
        storage_properties: Union[Unset, None, GetArticleStorageProperties]
        if _storage_properties is None:
            storage_properties = None
        elif isinstance(_storage_properties, Unset):
            storage_properties = UNSET
        else:
            storage_properties = GetArticleStorageProperties.from_dict(_storage_properties)

        _default_location = d.pop("defaultLocation", UNSET)
        default_location: Union[Unset, None, GetArticleDefaultLocation]
        if _default_location is None:
            default_location = None
        elif isinstance(_default_location, Unset):
            default_location = UNSET
        else:
            default_location = GetArticleDefaultLocation.from_dict(_default_location)

        get_article_model = cls(
            goods_owner=goods_owner,
            article_system_id=article_system_id,
            article_number=article_number,
            article_name=article_name,
            product_code=product_code,
            unit_code=unit_code,
            description=description,
            is_stock_article=is_stock_article,
            is_active=is_active,
            supplier_info=supplier_info,
            bar_code_info=bar_code_info,
            quantity_per_package=quantity_per_package,
            quantity_per_pallet=quantity_per_pallet,
            weight=weight,
            length=length,
            width=width,
            height=height,
            volume=volume,
            purchase_price=purchase_price,
            stock_valuation_price=stock_valuation_price,
            customer_price=customer_price,
            purcase_currency_code=purcase_currency_code,
            country_of_origin_code=country_of_origin_code,
            statistics_number=statistics_number,
            article_group=article_group,
            article_category=article_category,
            inventory_info=inventory_info,
            article_data_last_updated=article_data_last_updated,
            article_kind=article_kind,
            stock_limit=stock_limit,
            minimum_reorder_quantity=minimum_reorder_quantity,
            net_weight=net_weight,
            free_values=free_values,
            sub_quantity_per_item=sub_quantity_per_item,
            classes=classes,
            customs_description=customs_description,
            taric_numbers_info=taric_numbers_info,
            default_location_max_number_of_items=default_location_max_number_of_items,
            default_location_stock_limit=default_location_stock_limit,
            link_to_picture=link_to_picture,
            storage_properties=storage_properties,
            default_location=default_location,
        )

        return get_article_model
