import common.helpers as helpers
import common.models as models
import common.validators as validators

validators.is_boolean("true")
validators.is_json("{}")
validators.is_numeric(10)
validators.is_date("2018-0101")


john_post = models.Post()
john_posts = models.Posts()
john = models.User()

print("\n\n***** self *****")
for k in dict(globals()).keys():
    print(k)


print("\n\n***** common *****")
for k in validators.__dict__.keys():
    print(k)

print("\n\n***** models *****")
for k in models.__dict__.keys():
    print(k)

calc = helpers.Calc()

print(helpers.say_hello("Rod"))
print(helpers.factorial(6))