# -*- coding: utf-8 -*-
from model.group import Group



def test_test_add_grup(app):
    app.group.create(Group(name ="grup", header ="GRUOGRUP", footer ="111"))


def test_test_add_empty_grup(app):
    app.group.create(Group(name ="", header ="", footer =""))
