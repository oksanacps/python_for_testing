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

