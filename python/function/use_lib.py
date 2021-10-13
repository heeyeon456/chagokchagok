# pythom -m py_compile mylib.py
import mylib as m
from mymath import mycircle
import sys
#from mylib import *

# 시스템 경로추가
#sys.path.append(r"d:\mytest")
print(sys.path)
rst = m.hap(10, 20)
print(rst)
rst = m.gop(10, 20)
print(rst)

rst = mycircle.cmToInch(3)
print(rst)

rst = mycircle.cone(3, 10)
print(rst)

rst = mycircle.cylinder(3, 10)
print(rst)

