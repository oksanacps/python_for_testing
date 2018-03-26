from model.contact import Contact
import random


#проверка на кнопку update сверху
def test_edit_contact_from_above(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="1", lastname="1", company="1", address="1", mobile="1", byear="1"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.firstname = 'edit_contact'
    app.contact.edit_contact_from_above_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)


#проверка на кнопку update снизу
# def test_edit_contact_from_below(app, json_contacts):
#     contact = json_contacts
#     if app.contact.count()==0:
#         app.contact.create(contact)
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact.id = old_contacts[index].id
#     app.contact.edit_contact_from_below_by_index(contact, index)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)