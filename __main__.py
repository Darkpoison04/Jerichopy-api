from lib import SomeRandomApi


x = SomeRandomApi()
y = x.random({
    "category": "misc",
    "endpoint": "lyrics",
    "parameters":{
            "title" :"sakhiyaan"
          }
})
print(y)
