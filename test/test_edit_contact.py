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
            for i in range(4)
]

@pytest.mark.parametrize("contact", testinfo, ids = [repr(x) for x in testinfo])
#проверка на кнопку update сверху
def test_edit_contact_from_above(app, contact):
    if app.contact.count()==0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_from_above_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@pytest.mark.parametrize("contact", testinfo, ids = [repr(x) for x in testinfo])
#проверка на кнопку update снизу
def test_edit_contact_from_below(app, contact):
    if app.contact.count()==0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_from_below_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)