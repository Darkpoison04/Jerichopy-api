from lib import SomeRandomApi

x = SomeRandomApi()
y = x.raw({
    "category":"animals",
    'endpoint': "dog"
})
print(y)
