import platform as pf
print(pf.platform())
print(pf.platform(0,1))
print(pf.platform(1))
print(pf.machine())
print(pf.processor())
print(pf.architecture())
print(pf.system())
print(pf.version())

import sys
print(*sys.builtin_module_names,sep="\n")
import pkgutil
print(*pkgutil.iter_modules(),sep="\n")
import os