import sys

import importer

module1 = importer.import_("module1", "module1_source.py", ".")

print(f"sys says: {sys.modules.get('module1', 'module1 not FOUND')}")

import module2

module2.hello()
