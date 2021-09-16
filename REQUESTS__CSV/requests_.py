import requests

res = requests.get("https://docs.python.org/3.5/")

print(res.status_code)
print(res.headers['Content-Type'])
print("REQUEST CONTENT:", res.content)    # binary info
print("REQUEST TEXT:", res.text)     # text info


res_png = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res_png.status_code)
print(res_png.headers['Content-Type'])
print("REQUEST CONTENT:", res_png.content)   # binary info


with open("python_png.png", "wb") as f:
    f.write(res_png.content)

parameters = {
    "q": "python",
    "test": "test1",
    "name": "Name With Spaces",
    "list": ["test1", "test2"]
}
res_param = requests.get("https://www.google.com/search",
                         params=parameters)
print(res_param.status_code)
# 200
print()
print(res_param.headers['Content-Type'])
# text/html; charset=ISO-8859-1
print()
print("URL with params:", res_param.url)
# https://www.google.com/search?q=python&test=test1&name=Name+With+Spaces&list=test1&list=test2

print()
# print("REQUEST text CONTENT:", res_param.text)
