from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
	class Meta:
		model = RickJamesOrder
		fields = '__all__'
		exclude = ['transaction_id']


class OrderItemsForm(ModelForm):
	class Meta:
		model = RickJamesOrderItem
		fields = '__all__'


class ShippingDetailsForm(ModelForm):
	class Meta:
		model = RickJamesShippingAddress
		fields = '__all__'


class ProductsForm(ModelForm):
	class Meta:
		model = RickJamesProduct
		fields = '__all__'

