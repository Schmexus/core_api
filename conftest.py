import pytest
from client.api import ApiClient

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://reqres.in/api/")

@pytest.fixture(scope='session')
def api_client(request):
    url = request.config.getoption("--base_url")
    print(url)
    return ApiClient(url)
