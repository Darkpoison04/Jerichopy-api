from lib import SomeRandomApi


x = SomeRandomApi()
y = x.random({
    "category": "anime",
    "filters": ["link"]
})
print(y)
