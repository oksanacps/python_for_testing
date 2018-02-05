# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application_group import Application_group
import pytest

@pytest.fixture()
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_grup(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create(Group(name ="grup", header ="GRUOGRUP", footer ="111"))
    app.session.logout()


def test_test_add_empty_grup(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create(Group(name ="", header ="", footer =""))
    app.session.logout()
