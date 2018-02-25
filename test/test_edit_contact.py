from model.contact import Contact

#проверка на кнопку update сверху
def test_edit_contact_from_above(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Test", middlename="", lastname="", company="",
                                   address="", mobile="", byear=""))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Gavrilova", middlename="Oksana", lastname="Nikolaevna", company="CPS",
                               address="Tver", mobile="89301512526", byear="1993")
    contact.id = old_contacts[0].id
    app.contact.edit_contact_from_above(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# #проверка на кнопку update снизу
# def test_edit_contact_from_below(app):
#     if app.contact.count()==0:
#         app.contact.create(Contact(firstname="Test", middlename="", lastname="", company="",
#                                    address="", mobile="", byear=""))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_contact_from_below(Contact(firstname="234", middlename="Oksana", lastname="Nikolaevna", company="CPS",
#                                address="Tver", mobile="89301512526", byear="1993"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)