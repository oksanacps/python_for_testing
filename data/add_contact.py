from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", company="company1", address="address1", mobile="mobile1", byear="byear1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", company="company2", address="address2", mobile="mobile2", byear="byear")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testinfo = [Contact(firstname="", middlename="", lastname="", company="", address="", mobile="", byear="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    company=random_string("company", 3), address=random_string("address", 5), mobile=random_string("mobile", 5), byear="1986")
            for i in range(4)
]
