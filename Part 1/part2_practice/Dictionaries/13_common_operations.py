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
