from .models import Product 

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
