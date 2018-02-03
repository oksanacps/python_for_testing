# -*- coding: utf-8 -*-
from group import Group
from application_group import Application_group
import pytest

@pytest.fixture()
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_grup(app):
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "grup", header = "GRUOGRUP", footer = "111"))
    app.logout()


def test_test_add_empty_grup(app):
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "", header = "", footer = ""))
    app.logout()
