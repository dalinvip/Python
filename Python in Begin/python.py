import math;
import re;
import random;
from datetime import date;
import zlib;
a = "tea for too";
print(a)
print(a.replace("too","two"));
print(math.pi);
print(math.log(1024,2));
print(random.sample(range(1000),10));
print(date.today());
s = b'witch which has which witches wrist watch';
print(len(s));
t = zlib.compress(s);
print(len(t));
print(zlib.decompress(t));