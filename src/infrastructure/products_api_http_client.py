import requests
from tools.http_status_code import HttpStatusCode
from domain.models.product import Product

BASE_URL = "http://challenge-api.luizalabs.com/api/product"


def exists_product(product_id):
    response = requests.get("%s/%s/" % (BASE_URL, product_id))
    return response.status_code == HttpStatusCode.OK.value


def get_product(product_id):
    response = requests.get("%s/%s/" % (BASE_URL, product_id))
    data = response.json()

    id = data['id']
    title = data['title']
    price = data['price']
    image = data['image']

    review_score = None

    try:
        review_score = data['reviewScore']
    except:
        review_score = None

    return Product(id, title, price, image, review_score)
