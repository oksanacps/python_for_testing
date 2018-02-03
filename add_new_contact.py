# -*- coding: utf-8 -*-
from contact import Contact
from application_contact import Application_contact
import pytest


@pytest.fixture()
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Gavrilov", middlename="Nikita", lastname="Romanovich", company="CPS",
                       address="Tver", mobile="89301512526", byear="1986"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", company="",
                       address="", mobile="", byear=""))
    app.logout()

