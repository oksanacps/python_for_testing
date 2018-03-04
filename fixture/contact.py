from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def click_on_button_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.click_on_button_add_new()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_contact_on_button(self):
        self.delete_contact_on_button_by_index(0)

    def delete_contact_on_button_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_on_pencil(self):
        self.delete_contact_on_pencil_by_index(0)

    def delete_contact_on_pencil_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        str_table = list(wd.find_elements_by_name("entry"))
        str_table[index].find_element_by_xpath("./td[8]/a/img").click()
        wd.find_element_by_xpath("//div/div[4]/form[2]/input[2]").click()
        self.contact_cache = None

    def edit_contact_from_below(self, contact):
        self.edit_contact_from_below_by_index(contact, 0)

    def edit_contact_from_below_by_index(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        self.pencil_by_index(index)
        self.edit_contact(contact)
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_from_above(self, contact):
        self.edit_contact_from_above_by_index(contact, 0)

    def edit_contact_from_above_by_index(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        self.pencil_by_index(index)
        self.edit_contact(contact)
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def edit_contact (self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def pencil (self):
        # wd = self.app.wd
        # wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.pencil_by_index(0)

    def pencil_by_index(self, index):
        wd = self.app.wd
        str_table = list(wd.find_elements_by_name("entry"))
        # str_table[index].find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        str_table[index].find_element_by_xpath("./td[8]/a/img").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len (wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            str_table = list(wd.find_elements_by_name("entry"))
            for element in str_table:
                cells = list(element.find_elements_by_tag_name("td"))
                text_ln = cells[1].text
                text_fn = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname = text_fn, lastname = text_ln, id = id))
        return list(self.contact_cache)