from fixture.application_contact import Application_contact
import pytest


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture
