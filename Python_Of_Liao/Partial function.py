print(int('123', base=8)) # 83

import functools

int8 = functools.partial(int, base=8)
print(int8('123')) # 83

maxAdd10 = functools.partial(max, 10)
print(maxAdd10(2,5,7)) # 10