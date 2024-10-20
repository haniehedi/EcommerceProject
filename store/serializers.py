from string import digits
from django.utils.timezone import now
from rest_framework import serializers
from .models import Product, Category
from persiantools.jdatetime import JalaliDate
from persiantools import digits

class ProductSerializer(serializers.ModelSerializer):
    days_ago_created=serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_days_ago_created(self, obj):
        return f'{digits.to_word((now() - obj.created_at).days)} روز پیش '

    def get_date(self, obj):
        date = JalaliDate(obj.created_at, locale='fa')
        # return date.strftime('%d.%m.%Y')
        return date.strftime('%c')

class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'
    def get_products(self, obj):
        serializer = ProductSerializer(obj.products.all(), many=True)
        return serializer.data


