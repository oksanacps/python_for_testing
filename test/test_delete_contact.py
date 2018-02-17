from model.contact import Contact


def test_delete_contact_on_button(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Test", middlename="", lastname="", company="",
                                   address="", mobile="", byear=""))
    app.contact.delete_contact_on_button()


def test_delete_contact_on_pencil(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Test", middlename="", lastname="", company="",
                                   address="", mobile="", byear=""))
    app.contact.delete_contact_on_pencil()