# numpy provides function to perform log at base 2, e, 10

import numpy as np

# returns an array with integers starting from 1 (included) to 10 (not included)
arr = np.arange(1, 10)
# performs log at base 2
print(np.log2(arr))

arr = np.arange(1, 10)
# performs log at base 10
print(np.log10(arr))

arr = np.arange(1, 10)
# performs log at base e
print(np.log(arr))

# log at any base
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))