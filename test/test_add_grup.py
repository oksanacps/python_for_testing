# -*- coding: utf-8 -*-
from model.group import Group



def test_test_add_grup(app):
    old_groups = app.group.get_group_list()
    group = Group(name ="group", header ="GRUOGRUP", footer ="111")
    app.group.create(group)
    assert len (old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def test_test_add_empty_grup(app):
    old_groups = app.group.get_group_list()
    group = Group(name ="", header ="", footer ="")
    app.group.create(group)
    assert len (old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)