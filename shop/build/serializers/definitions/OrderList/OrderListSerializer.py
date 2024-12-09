from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class OrderListType(object):
    def __init__(self, orders=None, total=None, page=None, size=None,  **kwargs):
        self.orders = orders
        self.total = total
        self.page = page
        self.size = size

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class OrderListSerializer(serializers.Serializer):
    from shop.build.serializers.definitions.Order.OrderSerializer import OrderSerializer
    orders = OrderSerializer(required=False, many=True)
    total = serializers.IntegerField(required=False, allow_null=True)
    page = serializers.IntegerField(required=False, allow_null=True)
    size = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        from shop.build.serializers.definitions.Order.OrderSerializer import OrderSerializer
        orders_val = []
        orders_list_val = validated_data.pop("orders", [])
        for each_data in orders_list_val:
            each_obj, _ = deserialize(OrderSerializer, each_data, many=False, partial=True)
            orders_val.append(each_obj)
        
        return OrderListType(orders=orders_val, **validated_data)
