from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="", footer=""))
    app.group.edit_first_group(Group(name ="123", header ="456", footer ="789"))