# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Gavrilov", middlename="Nikita", lastname="Romanovich", company="CPS",
                               address="Tver", mobile="89301512526", byear="1986"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname="", company="",
                               address="", mobile="", byear=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

