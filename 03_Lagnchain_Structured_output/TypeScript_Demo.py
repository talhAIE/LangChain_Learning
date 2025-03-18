from typing import TypedDict
class Person(TypedDict):
    name: str
    age:int
    email: str

info: Person ={
    'name':'Talha Abbasi',
    'age':23,
    'email': None
}

print(info)