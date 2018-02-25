# -*- coding: utf-8 -*-
from model.group import Group



def test_test_add_grup(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name ="grup", header ="GRUOGRUP", footer ="111"))
    new_groups = app.group.get_group_list()
    assert len (old_groups) + 1 == len (new_groups)

def test_test_add_empty_grup(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name ="", header ="", footer =""))
    new_groups = app.group.get_group_list()
    assert len (old_groups) + 1 == len (new_groups)