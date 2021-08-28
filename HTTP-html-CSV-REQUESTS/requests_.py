import requests

res = requests.get("https://docs.python.org/3.5/")


print(res.status_code)
print(res.headers['Content-Type'])
print("REQUEST CONTENT:", res.content)
print("REQUEST TEXT:", res.text)


res_png = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res_png.status_code)
print(res_png.headers['Content-Type'])
print("REQUEST CONTENT:", res_png.content)   # binary info

with open("python_png.png", "wb") as f:
    f.write(res_png.content)


res_param = requests.get("https://www.google.com/search",
                         params={
                             "q": "python",
                             "test": "test1",
                             "name": "Name With Spaces",
                             "list": ["test1", "test2"]
                         })
print(res_param.status_code)
# 200
print(res_param.headers['Content-Type'])
# text/html; charset=ISO-8859-1
print("URL:", res_param.url)

# https://www.google.com/search?q=python&test=test1&name=Name+With+Spaces&list=test1&list=test2
print("REQUEST CONTENT:", res_param.text)

if __name__ = "__main__":
    main()
