import httpx

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, **kwargs):
        with httpx.Client() as client: # для того чтобы после вызова метода закрывать соединение и высвобождать память
            return client.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, **kwargs):
        with httpx.Client() as client:
            return client.post(f"{self.base_url}{endpoint}", **kwargs)

    def put(self, endpoint, **kwargs):
        with httpx.Client() as client:
            return client.put(f"{self.base_url}{endpoint}", **kwargs)

    def delete(self, endpoint, **kwargs):
        with httpx.Client() as client:
            return client.delete(f"{self.base_url}{endpoint}", **kwargs)

