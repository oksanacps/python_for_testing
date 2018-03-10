from model.contact import Contact
from random import randrange
import pytest
import random
import string



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testinfo = [Contact(firstname="", middlename="", lastname="", company="", address="", mobile="", byear="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    company=random_string("company", 3), address=random_string("address", 5), mobile=random_string("mobile", 5), byear="1986")
]

@pytest.mark.parametrize("contact", testinfo, ids = [repr(x) for x in testinfo])
def test_delete_contact_on_button(app, contact):
    if app.contact.count()==0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_on_button_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

@pytest.mark.parametrize("contact", testinfo, ids = [repr(x) for x in testinfo])
def test_delete_contact_on_pencil(app, contact):
    if app.contact.count()==0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_on_pencil_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts