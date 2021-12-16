from lib import SomeRandomApi

y = SomeRandomApi().raw({"category": "misc", "endpoint": "joke"})
print(y)
