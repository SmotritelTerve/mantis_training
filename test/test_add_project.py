from model.project import Project
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project = Project(random_string("name_", 10), random_string("description_", 10))
    old_list = app.soap.get_project_list()
    if project in old_list:
        app.project.delete_project(project)
    old_list = app.soap.get_project_list()
    app.project.add_project(project)
    new_list = app.soap.get_project_list()
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
