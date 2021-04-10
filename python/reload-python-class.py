### Reload a python class

import sys
del sys.modules['target_class']
from target_class import TargetClass
instance_of_class = TargetClass()