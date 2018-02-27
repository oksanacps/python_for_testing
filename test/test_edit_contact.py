from model.contact import Contact
from random import randrange

#проверка на кнопку update сверху
def test_edit_contact_from_above(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Test", middlename="", lastname="", company="",
                                   address="", mobile="", byear=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Gavrilova", middlename="Oksana", lastname="Nikolaevna", company="CPS",
                               address="Tver", mobile="89301512526", byear="1993")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_from_above_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#проверка на кнопку update снизу
def test_edit_contact_from_below(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Test", middlename="", lastname="", company="",
                                   address="", mobile="", byear=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="234", middlename="Oksana", lastname="Nikolaevna", company="CPS",
                               address="Tver", mobile="89301512526", byear="1993")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_from_below_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)