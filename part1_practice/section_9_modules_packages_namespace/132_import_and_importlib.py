import collections
import fractions
import importlib
import importlib.util
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
