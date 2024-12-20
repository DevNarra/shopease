from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class OrderType(object):
    def __init__(self, id=None, products=None, customer=None, payment=None, status=None, expected_delivery_date=None, order_datetime=None,  **kwargs):
        self.id = id
        self.products = products
        self.customer = customer
        self.payment = payment
        self.status = status
        self.expected_delivery_date = expected_delivery_date
        self.order_datetime = order_datetime

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class OrderSerializer(serializers.Serializer):
    id = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    from shop.build.serializers.definitions.Product.ProductSerializer import ProductSerializer
    products = ProductSerializer(required=False, many=True)
    from shop.build.serializers.definitions.Customer.CustomerSerializer import CustomerSerializer
    customer = CustomerSerializer(required=False, allow_null=True)
    from shop.build.serializers.definitions.Payment.PaymentSerializer import PaymentSerializer
    payment = PaymentSerializer(required=False, allow_null=True)
    status = serializers.ChoiceField(choices=(('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')), required=False, allow_blank=True, allow_null=True)
    expected_delivery_date = serializers.DateField(required=False, allow_null=True)
    order_datetime = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        from shop.build.serializers.definitions.Product.ProductSerializer import ProductSerializer
        products_val = []
        products_list_val = validated_data.pop("products", [])
        for each_data in products_list_val:
            each_obj, _ = deserialize(ProductSerializer, each_data, many=False, partial=True)
            products_val.append(each_obj)
        
        from shop.build.serializers.definitions.Customer.CustomerSerializer import CustomerSerializer
        customer_val, _ = deserialize(CustomerSerializer, validated_data.pop("customer", None), many=False, partial=True)
        
        from shop.build.serializers.definitions.Payment.PaymentSerializer import PaymentSerializer
        payment_val, _ = deserialize(PaymentSerializer, validated_data.pop("payment", None), many=False, partial=True)
        
        return OrderType(products=products_val, customer=customer_val, payment=payment_val, **validated_data)
