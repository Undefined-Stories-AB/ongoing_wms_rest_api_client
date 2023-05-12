from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.post_article_bar_code_info import PostArticleBarCodeInfo
    from ..models.post_article_free_values import PostArticleFreeValues
    from ..models.post_article_name_translation import PostArticleNameTranslation
    from ..models.post_article_storage_class import PostArticleStorageClass
    from ..models.post_article_storage_properties import PostArticleStorageProperties
    from ..models.post_article_structure_specification import PostArticleStructureSpecification
    from ..models.post_article_supplier_info import PostArticleSupplierInfo
    from ..models.post_article_taric_numbers_info import PostArticleTaricNumbersInfo


T = TypeVar("T", bound="PostArticleModel")


@attr.s(auto_attribs=True)
class PostArticleModel:
    """
    Attributes:
        goods_owner_id (int):
        article_number (str):
        article_group (Union[Unset, None, CodeNamePair]):
        article_category (Union[Unset, None, CodeNamePair]):
        article_color (Union[Unset, None, CodeNamePair]):
        article_size (Union[Unset, None, CodeNamePair]):
        article_name (Union[Unset, None, str]):
        product_code (Union[Unset, None, str]):
        unit_code (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        is_stock_article (Union[Unset, None, bool]):
        is_active (Union[Unset, None, bool]):
        supplier_info (Union[Unset, None, PostArticleSupplierInfo]):
        bar_code_info (Union[Unset, None, PostArticleBarCodeInfo]):
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
        article_name_translations (Union[Unset, None, List['PostArticleNameTranslation']]):
        stock_limit (Union[Unset, None, int]):
        minimum_reorder_quantity (Union[Unset, None, float]):
        net_weight (Union[Unset, None, float]):
        link_to_picture (Union[Unset, None, str]):
        structure_definition (Union[Unset, None, PostArticleStructureSpecification]):
        quantity_per_layer_on_pallet (Union[Unset, None, int]):
        sub_quantity_per_item (Union[Unset, None, float]):
        min_days_to_expiry_date_allowed_on_delivery (Union[Unset, None, int]):
        storage_properties (Union[Unset, None, PostArticleStorageProperties]):
        free_values (Union[Unset, None, PostArticleFreeValues]):
        storage_class (Union[Unset, None, PostArticleStorageClass]):
        customs_description (Union[Unset, None, str]):
        taric_numbers_info (Union[Unset, None, PostArticleTaricNumbersInfo]):
    """

    goods_owner_id: int
    article_number: str
    article_group: Union[Unset, None, "CodeNamePair"] = UNSET
    article_category: Union[Unset, None, "CodeNamePair"] = UNSET
    article_color: Union[Unset, None, "CodeNamePair"] = UNSET
    article_size: Union[Unset, None, "CodeNamePair"] = UNSET
    article_name: Union[Unset, None, str] = UNSET
    product_code: Union[Unset, None, str] = UNSET
    unit_code: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    is_stock_article: Union[Unset, None, bool] = UNSET
    is_active: Union[Unset, None, bool] = UNSET
    supplier_info: Union[Unset, None, "PostArticleSupplierInfo"] = UNSET
    bar_code_info: Union[Unset, None, "PostArticleBarCodeInfo"] = UNSET
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
    article_name_translations: Union[Unset, None, List["PostArticleNameTranslation"]] = UNSET
    stock_limit: Union[Unset, None, int] = UNSET
    minimum_reorder_quantity: Union[Unset, None, float] = UNSET
    net_weight: Union[Unset, None, float] = UNSET
    link_to_picture: Union[Unset, None, str] = UNSET
    structure_definition: Union[Unset, None, "PostArticleStructureSpecification"] = UNSET
    quantity_per_layer_on_pallet: Union[Unset, None, int] = UNSET
    sub_quantity_per_item: Union[Unset, None, float] = UNSET
    min_days_to_expiry_date_allowed_on_delivery: Union[Unset, None, int] = UNSET
    storage_properties: Union[Unset, None, "PostArticleStorageProperties"] = UNSET
    free_values: Union[Unset, None, "PostArticleFreeValues"] = UNSET
    storage_class: Union[Unset, None, "PostArticleStorageClass"] = UNSET
    customs_description: Union[Unset, None, str] = UNSET
    taric_numbers_info: Union[Unset, None, "PostArticleTaricNumbersInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        goods_owner_id = self.goods_owner_id
        article_number = self.article_number
        article_group: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_group, Unset):
            article_group = self.article_group.to_dict() if self.article_group else None

        article_category: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_category, Unset):
            article_category = self.article_category.to_dict() if self.article_category else None

        article_color: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_color, Unset):
            article_color = self.article_color.to_dict() if self.article_color else None

        article_size: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.article_size, Unset):
            article_size = self.article_size.to_dict() if self.article_size else None

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
        article_name_translations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.article_name_translations, Unset):
            if self.article_name_translations is None:
                article_name_translations = None
            else:
                article_name_translations = []
                for article_name_translations_item_data in self.article_name_translations:
                    article_name_translations_item = article_name_translations_item_data.to_dict()

                    article_name_translations.append(article_name_translations_item)

        stock_limit = self.stock_limit
        minimum_reorder_quantity = self.minimum_reorder_quantity
        net_weight = self.net_weight
        link_to_picture = self.link_to_picture
        structure_definition: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.structure_definition, Unset):
            structure_definition = self.structure_definition.to_dict() if self.structure_definition else None

        quantity_per_layer_on_pallet = self.quantity_per_layer_on_pallet
        sub_quantity_per_item = self.sub_quantity_per_item
        min_days_to_expiry_date_allowed_on_delivery = self.min_days_to_expiry_date_allowed_on_delivery
        storage_properties: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.storage_properties, Unset):
            storage_properties = self.storage_properties.to_dict() if self.storage_properties else None

        free_values: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.free_values, Unset):
            free_values = self.free_values.to_dict() if self.free_values else None

        storage_class: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.storage_class, Unset):
            storage_class = self.storage_class.to_dict() if self.storage_class else None

        customs_description = self.customs_description
        taric_numbers_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.taric_numbers_info, Unset):
            taric_numbers_info = self.taric_numbers_info.to_dict() if self.taric_numbers_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "goodsOwnerId": goods_owner_id,
                "articleNumber": article_number,
            }
        )
        if article_group is not UNSET:
            field_dict["articleGroup"] = article_group
        if article_category is not UNSET:
            field_dict["articleCategory"] = article_category
        if article_color is not UNSET:
            field_dict["articleColor"] = article_color
        if article_size is not UNSET:
            field_dict["articleSize"] = article_size
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
        if article_name_translations is not UNSET:
            field_dict["articleNameTranslations"] = article_name_translations
        if stock_limit is not UNSET:
            field_dict["stockLimit"] = stock_limit
        if minimum_reorder_quantity is not UNSET:
            field_dict["minimumReorderQuantity"] = minimum_reorder_quantity
        if net_weight is not UNSET:
            field_dict["netWeight"] = net_weight
        if link_to_picture is not UNSET:
            field_dict["linkToPicture"] = link_to_picture
        if structure_definition is not UNSET:
            field_dict["structureDefinition"] = structure_definition
        if quantity_per_layer_on_pallet is not UNSET:
            field_dict["quantityPerLayerOnPallet"] = quantity_per_layer_on_pallet
        if sub_quantity_per_item is not UNSET:
            field_dict["subQuantityPerItem"] = sub_quantity_per_item
        if min_days_to_expiry_date_allowed_on_delivery is not UNSET:
            field_dict["minDaysToExpiryDateAllowedOnDelivery"] = min_days_to_expiry_date_allowed_on_delivery
        if storage_properties is not UNSET:
            field_dict["storageProperties"] = storage_properties
        if free_values is not UNSET:
            field_dict["freeValues"] = free_values
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class
        if customs_description is not UNSET:
            field_dict["customsDescription"] = customs_description
        if taric_numbers_info is not UNSET:
            field_dict["taricNumbersInfo"] = taric_numbers_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.post_article_bar_code_info import PostArticleBarCodeInfo
        from ..models.post_article_free_values import PostArticleFreeValues
        from ..models.post_article_name_translation import PostArticleNameTranslation
        from ..models.post_article_storage_class import PostArticleStorageClass
        from ..models.post_article_storage_properties import PostArticleStorageProperties
        from ..models.post_article_structure_specification import PostArticleStructureSpecification
        from ..models.post_article_supplier_info import PostArticleSupplierInfo
        from ..models.post_article_taric_numbers_info import PostArticleTaricNumbersInfo

        d = src_dict.copy()
        goods_owner_id = d.pop("goodsOwnerId")

        article_number = d.pop("articleNumber")

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

        _article_color = d.pop("articleColor", UNSET)
        article_color: Union[Unset, None, CodeNamePair]
        if _article_color is None:
            article_color = None
        elif isinstance(_article_color, Unset):
            article_color = UNSET
        else:
            article_color = CodeNamePair.from_dict(_article_color)

        _article_size = d.pop("articleSize", UNSET)
        article_size: Union[Unset, None, CodeNamePair]
        if _article_size is None:
            article_size = None
        elif isinstance(_article_size, Unset):
            article_size = UNSET
        else:
            article_size = CodeNamePair.from_dict(_article_size)

        article_name = d.pop("articleName", UNSET)

        product_code = d.pop("productCode", UNSET)

        unit_code = d.pop("unitCode", UNSET)

        description = d.pop("description", UNSET)

        is_stock_article = d.pop("isStockArticle", UNSET)

        is_active = d.pop("isActive", UNSET)

        _supplier_info = d.pop("supplierInfo", UNSET)
        supplier_info: Union[Unset, None, PostArticleSupplierInfo]
        if _supplier_info is None:
            supplier_info = None
        elif isinstance(_supplier_info, Unset):
            supplier_info = UNSET
        else:
            supplier_info = PostArticleSupplierInfo.from_dict(_supplier_info)

        _bar_code_info = d.pop("barCodeInfo", UNSET)
        bar_code_info: Union[Unset, None, PostArticleBarCodeInfo]
        if _bar_code_info is None:
            bar_code_info = None
        elif isinstance(_bar_code_info, Unset):
            bar_code_info = UNSET
        else:
            bar_code_info = PostArticleBarCodeInfo.from_dict(_bar_code_info)

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

        article_name_translations = []
        _article_name_translations = d.pop("articleNameTranslations", UNSET)
        for article_name_translations_item_data in _article_name_translations or []:
            article_name_translations_item = PostArticleNameTranslation.from_dict(article_name_translations_item_data)

            article_name_translations.append(article_name_translations_item)

        stock_limit = d.pop("stockLimit", UNSET)

        minimum_reorder_quantity = d.pop("minimumReorderQuantity", UNSET)

        net_weight = d.pop("netWeight", UNSET)

        link_to_picture = d.pop("linkToPicture", UNSET)

        _structure_definition = d.pop("structureDefinition", UNSET)
        structure_definition: Union[Unset, None, PostArticleStructureSpecification]
        if _structure_definition is None:
            structure_definition = None
        elif isinstance(_structure_definition, Unset):
            structure_definition = UNSET
        else:
            structure_definition = PostArticleStructureSpecification.from_dict(_structure_definition)

        quantity_per_layer_on_pallet = d.pop("quantityPerLayerOnPallet", UNSET)

        sub_quantity_per_item = d.pop("subQuantityPerItem", UNSET)

        min_days_to_expiry_date_allowed_on_delivery = d.pop("minDaysToExpiryDateAllowedOnDelivery", UNSET)

        _storage_properties = d.pop("storageProperties", UNSET)
        storage_properties: Union[Unset, None, PostArticleStorageProperties]
        if _storage_properties is None:
            storage_properties = None
        elif isinstance(_storage_properties, Unset):
            storage_properties = UNSET
        else:
            storage_properties = PostArticleStorageProperties.from_dict(_storage_properties)

        _free_values = d.pop("freeValues", UNSET)
        free_values: Union[Unset, None, PostArticleFreeValues]
        if _free_values is None:
            free_values = None
        elif isinstance(_free_values, Unset):
            free_values = UNSET
        else:
            free_values = PostArticleFreeValues.from_dict(_free_values)

        _storage_class = d.pop("storageClass", UNSET)
        storage_class: Union[Unset, None, PostArticleStorageClass]
        if _storage_class is None:
            storage_class = None
        elif isinstance(_storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = PostArticleStorageClass.from_dict(_storage_class)

        customs_description = d.pop("customsDescription", UNSET)

        _taric_numbers_info = d.pop("taricNumbersInfo", UNSET)
        taric_numbers_info: Union[Unset, None, PostArticleTaricNumbersInfo]
        if _taric_numbers_info is None:
            taric_numbers_info = None
        elif isinstance(_taric_numbers_info, Unset):
            taric_numbers_info = UNSET
        else:
            taric_numbers_info = PostArticleTaricNumbersInfo.from_dict(_taric_numbers_info)

        post_article_model = cls(
            goods_owner_id=goods_owner_id,
            article_number=article_number,
            article_group=article_group,
            article_category=article_category,
            article_color=article_color,
            article_size=article_size,
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
            article_name_translations=article_name_translations,
            stock_limit=stock_limit,
            minimum_reorder_quantity=minimum_reorder_quantity,
            net_weight=net_weight,
            link_to_picture=link_to_picture,
            structure_definition=structure_definition,
            quantity_per_layer_on_pallet=quantity_per_layer_on_pallet,
            sub_quantity_per_item=sub_quantity_per_item,
            min_days_to_expiry_date_allowed_on_delivery=min_days_to_expiry_date_allowed_on_delivery,
            storage_properties=storage_properties,
            free_values=free_values,
            storage_class=storage_class,
            customs_description=customs_description,
            taric_numbers_info=taric_numbers_info,
        )

        return post_article_model
