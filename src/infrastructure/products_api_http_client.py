import requests
from tools.http_status_code import HttpStatusCode

BASE_URL = "http://challenge-api.luizalabs.com/api/product"


def exists_product(product_id):
    request = requests.get("%s/%s/" % (BASE_URL, product_id))
    return request.status_code == HttpStatusCode.OK.value
