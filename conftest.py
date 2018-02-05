from fixture.application_group import Application_group
import pytest

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture