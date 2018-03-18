# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import constant as testinfo

@pytest.mark.parametrize("contact", testinfo, ids = [repr(x) for x in testinfo])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



