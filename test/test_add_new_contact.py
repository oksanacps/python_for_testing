# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testinfo = [Contact(firstname="", middlename="", lastname="", company="", address="", mobile="", byear="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    company=random_string("company", 3), address=random_string("address", 5), mobile=random_string("mobile", 5), byear="1986")
            for i in range(4)
]

@pytest.mark.parametrize("contact", testinfo, ids = [repr(x) for x in testinfo])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



