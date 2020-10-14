# Slots
# https://stackoverflow.com/a/28059785/5841818

# ******************
# What problem solve
# ******************
# __slots__ allows to predefine set of attributes class instance will have. (avoid dynamically created attributes)
# Reason to use:
# 1. Faster attribute access
# 2. Space savings in memory

# ******************
# When not to use
# ******************
# does not work for classes derived from some built-in types such as int, bytes and tuple.
# better not to use in case of multiple inheritance - brings extra complexity.
# definitely should not be used if dynamical attribute assignment should be performed.

# ******************
# Syntax/example
# ******************
# ** but if slots attribute is set, __dict__ dictionary will be created - memory optimization
#
class SlotsClass:
    __slots__ = ('foo', 'bar')


obj = SlotsClass()
obj.foo = 5
obj.__slots__
# ('foo', 'bar')
# if slots attribute is set, __dict__ dictionary will not be created
obj.__dict__
# Traceback (most recent call last):
#   File "python", line 8, in <module>
# AttributeError: 'SlotsClass' object has no attribute '__dict__'
