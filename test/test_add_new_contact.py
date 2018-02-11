# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Gavrilov", middlename="Nikita", lastname="Romanovich", company="CPS",
                               address="Tver", mobile="89301512526", byear="1986"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", company="",
                               address="", mobile="", byear=""))
    app.session.logout()

