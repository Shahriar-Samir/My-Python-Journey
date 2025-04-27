import requests as fetch

res = fetch.get("https://jsonplaceholder.typicode.com/posts")

print(res.json())

