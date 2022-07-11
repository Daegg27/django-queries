from .models import Product 
from django.db.models import Q

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod 
    def find_by_model(cls, model):

        products = Product.objects.all()


        for product in products:
            if product.model == model:
                return product

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, rating):

        return Product.objects.filter(rating = rating)

    @classmethod
    def by_rating_range(cls, lower_range, higher_range):

        return Product.objects.filter(rating__range=(lower_range, higher_range))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        
        return Product.objects.filter(rating=rating).filter(color=color)

    @classmethod
    def by_rating_or_color(cls, rating, color):

        return Product.objects.filter(rating=rating)|Product.objects.filter(color=color)

    @classmethod
    def no_color_count(cls):

        return Product.objects.filter(color__isnull = True).count()

    @classmethod
    def below_price_or_above_rating(cls, price, r):
        return Product.objects.filter(rating__gt=r)|Product.objects.filter(price_cents__lt=price)

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category', '-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls, string):
        return Product.objects.filter(manufacturer__contains=string)
