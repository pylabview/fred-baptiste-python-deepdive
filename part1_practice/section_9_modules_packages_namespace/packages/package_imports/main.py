import common
import common.validators as validators

validators.is_boolean("true")
validators.is_json("{}")
validators.is_numeric(10)
validators.is_date("2018-0101")

print("*********** self **********")
for k in dict(globals()).keys():
    print(k)


print("*********** common **********")
for k in validators.__dict__.keys():
    print(k)


print("*********** validators **********")
for k in validators.__dict__.keys():
    print(k)


print("*********** numeric **********")
for k in validators.numeric.__dict__.keys():
    print(k)
