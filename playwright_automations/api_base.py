# from playwright.sync_api import Playwright
# from pytest_base_url.plugin import base_url
from pytest_playwright.pytest_playwright import Playwright

base_url = "https://rahulshettyacademy.com/"
header = {
    'Content-Type' : 'application/json'
}

class APIUtils:
    def get_token(self, Playwright):
        request_context = Playwright.request.new_context(base_url=base_url)
        response = request_context.post(url = "api/ecom/auth/login", headers=header,
                                        data={"userEmail": "supriyam@yopmail.com", "userPassword": "Iamking@000"})
        response = response.json()
        token = response['token']
        return token

    def add_to_cart(self, Playwright):
        data = {
            "_id": "6a2bd97f17ee3e78bad54f60",
            "product": {
                "_id": "6960eac0c941646b7a8b3e68",
                "productName": "ZARA COAT 3",
                "productCategory": "electronics",
                "productSubCategory": "mobiles"
            }
        }
        token = self.get_token(Playwright)
        print(token)
        header_test = {
            "Authorization" : token,
            'Content-Type': 'application/json'
        }
        request_context = Playwright.request.new_context(base_url=base_url)
        response = request_context.post(url='api/ecom/user/add-to-cart',data=data, headers=header_test)
        assert response.ok
        return response.json()
