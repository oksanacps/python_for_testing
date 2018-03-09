from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, company=None, address=None, mobile=None, byear=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None,
                 all_email_from_home_page=None, email_0=None, email_1=None, email_2=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.byear = byear
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page
        self.email_0 = email_0
        self.email_1 = email_1
        self.email_2 = email_2

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int (self.id)
        else:
            return maxsize