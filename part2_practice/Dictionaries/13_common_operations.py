d = dict(zip("abc", range(1, 4)))

print(d)
print(len(d), d["a"], d.get("Python"), d.get("python", "N/A"))

text = """
        Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt,
        explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem 
        ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis 
        nostrum exercitationem ullam corporis suscipit laboriosam,         nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae
        consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?
        """

counts = dict()


for c in text:
    counts[c] = counts.get(c, 0) + 1

print(counts)

counts = dict()

for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(c, 0) + 1

print("No SPACES", counts)

d = dict(a=1, b=2, c=3)
print(d)

for k in d:
    print(k)

print("'a' in d", "a" in d)
print("'z' not in d", "z" not in d)

d = dict.fromkeys("abcd", 0)
print(d)

del d["a"]
print(d)
# removing element form a dict

d = dict.fromkeys("abcd", 0)

print("d = dict('abcd',0)", d)

del d["a"]
print("del d['a']", d)

# del d["python"]

d = dict(a=1, b=2)

# d.pop("z") raise an error becuase the key "z" doesn't exist
result = d.pop("z", 100)
print(result)
result1 = d.pop("a")
print(result1)

d = dict({i: i**2 for i in range(1, 5)})
print(d)
result = d.popitem()
print(f"result: {result}, d: {d}")
d = {"a": 1, "b": 2, "c": 3}


def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]


print("Original d", d)
result = insert_if_not_present(d, "z", 100)
print(d, result)
result1 = insert_if_not_present(d, "a", 100)
print(d, result1)
d = dict(zip("abc", range(1, 4)))
print(d)
# setdefualt dict
result = d.setdefault("x", 100)
print(result, d)
result = d.setdefault("x", 100)
print(result, d)
import string

print(string.ascii_lowercase, string.ascii_uppercase)

categories = {}
for c in text:
    if c != " ":
        if c in string.ascii_lowercase:
            key = "lower"
        elif c in string.ascii_uppercase:
            key = "upper"
        else:
            key = "other"
        categories.setdefault(key, set()).add(c)

# print(categories)

for cat in categories:
    print(f"{cat}:", "".join(categories[cat]))


def cat_key(c):
    if c == " ":
        return None
    elif c in string.ascii_lowercase:
        return "lower"
    elif c in string.ascii_uppercase:
        return "upper"
    else:
        return "other"


categories = {}
print("-----------------------------\n\n")
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for k, v in categories.items():
    print(f"{k}: {''.join(v)}")


def cat_key(c):
    categories = {" ": None, string.ascii_lowercase: "lower", string.ascii_uppercase: "upper"}
    for key in categories:
        if c in key:
            return categories[key]
    else:
        return "other"


categories = {}
print("-----------------------------\n\n")
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for k, v in categories.items():
    print(f"{k}: {''.join(v)}")

from itertools import chain


def cat_key(c):
    cat_1 = {" ": None}
    cat_2 = dict.fromkeys(string.ascii_lowercase, "lower")
    cat_3 = dict.fromkeys(string.ascii_uppercase, "upper")
    categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))
    return categories.get(c, "others")


categories = {}
print("-----------------------------\n\n")
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for k, v in categories.items():
    print(f"{k}: {''.join(v)}")

print(categories)
print(categories.clear())
