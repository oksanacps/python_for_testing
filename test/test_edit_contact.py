from model.contact import Contact

#проверка на кнопку update сверху
def test_edit_contact_from_above(app):
    app.contact.edit_contact_from_above(Contact(firstname="Gavrilova", middlename="Oksana", lastname="Nikolaevna", company="CPS",
                               address="Tver", mobile="89301512526", byear="1993"))

#проверка на кнопку update снизу
def test_edit_contact_from_below(app):
    app.contact.edit_contact_from_below(Contact(firstname="234", middlename="Oksana", lastname="Nikolaevna", company="CPS",
                               address="Tver", mobile="89301512526", byear="1993"))