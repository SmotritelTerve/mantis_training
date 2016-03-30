from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_manage_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        if not len(wd.find_elements_by_xpath("//input[@value='Create New Project']")) > 0:
            wd.find_element_by_link_text("Manage Projects").click()

    def add_project(self, project):
        wd = self.app.wd
        self.go_to_manage_project()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        if project.description is not None:
            wd.find_element_by_name("description").click()
            wd.find_element_by_name("description").clear()
            wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_css_selector("input.button").click()
        self.contact_cache = None

    def delete_project(self, project):
        wd = self.app.wd
        self.go_to_manage_project()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()
        self.contact_cache = None

    contact_cache = None

    def get_project_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_manage_project()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("table.width100 tr[class^='row']")[1:]:
                name = element.find_element_by_css_selector('a').text
                description = element.find_elements_by_css_selector('td')[4].text
                id = element.find_element_by_css_selector('a').get_attribute("href").split('=')[-1]
                self.contact_cache.append(Project(name=name, description=description, id=id))
        return list(self.contact_cache)

