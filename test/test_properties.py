import re
from random import randrange


def test_all_contact_ui_db(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    for contact_home in contact_from_home_page:
        for contact_db in contact_from_db:
            if contact_home.id == contact_db.id:
                assert contact_home.firstname == contact_db.firstname
                assert contact_home.lastname == contact_db.lastname
                assert contact_home.address == contact_db.address
                assert contact_home.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
                assert contact_home.all_email_from_home_page == merge_email_like_on_home_page(contact_db)
                return


# def test_phones_on_home_page(app):
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
#     assert clear(contact_from_home_page.firstname) == clear(contact_from_edit_page.firstname)
#     assert clear(contact_from_home_page.lastname) == clear(contact_from_edit_page.lastname)
#     assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)


# def test_phones_contact_view_page(app):
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact_from_view_page = app.contact.get_contact_from_view_page(index)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[()  -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.email_0, contact.email_1, contact.email_2]))))