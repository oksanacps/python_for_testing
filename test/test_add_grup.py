# -*- coding: utf-8 -*-
from model.group import Group



def test_test_add_grup(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create(Group(name ="grup", header ="GRUOGRUP", footer ="111"))
    app.session.logout()


def test_test_add_empty_grup(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create(Group(name ="", header ="", footer =""))
    app.session.logout()
