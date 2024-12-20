from .user import User
from .order import Order
from .products import Product
from .order_item import OrderItem
from .payment import Payment
from .feedback import Feedback
from .customer import Customer

__all__ = [
  'User'
  'Product',
  'Order',
  'OrderItem',
  'Payment',
  "Feedback",
  "Customer"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
