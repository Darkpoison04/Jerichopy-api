from lib import SomeRandomApi


x = SomeRandomApi()
y = x.random({
    "category": "Animals",
    "filters": ["image"]
})
print(y)
