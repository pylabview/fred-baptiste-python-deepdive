import collections
import fractions
import importlib
import importlib.util
import os
import sys

mod_name = "math"
print(sys, collections, importlib)
print(importlib.import_module(mod_name))
print(f"is math in sys.modules? {'math' in sys.modules}")
# But math is not in globals
print(f"is math in globals? {'math' in globals()}")
# How we added
math2 = importlib.import_module(mod_name)
print(f"is math2 in globals? {'math2' in globals()}")
print(math2)
print(fractions.__spec__)
print(sys.meta_path)
importlib.util.find_spec("decimal")
print(importlib.util.find_spec("decimal"))
decimal = importlib.import_module("decimal")
print(f"Is decimal in globals: {'decimal' in globals()}")
# Let's see if importlib can fine the spec of module1
print(importlib.util.find_spec("module1"))
import module1

print(f"module1 a = {module1.a}")
# Loading a module from another location
ext_module_path = os.environ["HOME"]
file_abs_path = os.path.join(ext_module_path, "module2.py")
print(ext_module_path)
print(file_abs_path)
print(importlib.util.find_spec("module2") is None)
# Could not find module1
# We need to add it to the sys.path manually
# print(sys.path)
sys.path.append(ext_module_path)
# print(sys.path)
print(f"Is /Users/rod in syst.path: {ext_module_path in sys.path} ")
# print(importlib.util.find_spec("module2"))
print("Spec:", importlib.util.find_spec("module2"))
##### Nice and clean ######
# ext_module_path = os.environ["HOME"]
# file_abs_path = os.path.join(ext_module_path, "module2.py")
# print(ext_module_path)
# print(file_abs_path)

# # (optional but very useful sanity check)
# print("File exists:", os.path.isfile(file_abs_path))

# # ✅ Add path BEFORE searching
# if ext_module_path not in sys.path:
#     sys.path.append(ext_module_path)

# # ✅ Invalidate caches after sys.path changes
# importlib.invalidate_caches()

# print(f"Is /Users/rod in syst.path: {ext_module_path in sys.path} ")
# print("Spec:", importlib.util.find_spec("module2"))
####################################
import module2

print("module2 x:", module2.x)