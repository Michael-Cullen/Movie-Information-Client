import omdb
from sys import stdin

omdb.set_default('apikey', '582f52b9')

def search_function():
    t = input("Enter film name:")
    res = omdb.search(t)
    print(res)

search_function()
