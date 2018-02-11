
def test_delete_contact_on_button(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact_on_button()
    app.session.logout()


def test_delete_contact_on_pencil(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact_on_pencil()
    app.session.logout()