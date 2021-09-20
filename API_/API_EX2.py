import requests
import json

client_id = '5f79deb6f1a362cedc08'
client_secret = '0492bcc510eee5640bdaa05f9d0ce5b5'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
# j = json.loads(r.text)
j = r.json()
print(j)
# достаем токен
token = j["token"]
print("TOKEN:  ", token)

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
# инициируем запрос с заголовком
# example_ids = ['4d8b92b34eb68a1b2c0003f4', '537def3c139b21353f0006a6', '4e2ed576477cc70001006f99']
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
jj = json.loads(r.text)
print("JJ: ", jj)
print("sortable_name:  ", jj["sortable_name"])
print("birthday:  ", jj["birthday"])


print("------------------------------------------------------------------------")
# response = requests.get("https://api.artsy.net/api/artists", headers=headers)
# data = response.json()
# print("DATA:  ", data)
# print("List of artists:  ", data["_embedded"]["artists"])   # list_ = data["_embedded"]["artists"]
# print("LENGTH: ", len(data["_embedded"]["artists"]))
#
# with open("artists.json", 'w') as file:
#     json.dump(data, file, indent=4)

# list_ = data["_embedded"]["artists"]
# # print(list_)
# ids = []
# for i in list_:
#     # print("List ELEM: ", i)
#     # print("id:  ", i["id"])
#     ids.append(i["id"])
# print("ALL ids:", ids)

dict_ = {}
example_ids = ['4d8b92b34eb68a1b2c0003f4', '537def3c139b21353f0006a6', '4e2ed576477cc70001006f99']
for i in range(len(example_ids)):
    api_url = "https://api.artsy.net/api/artists/{}".format(example_ids[i])
    response = requests.get(api_url, headers=headers)
    data = response.json()
    print("data:  ", data)
    # print("sortable_name:  ", data["sortable_name"])
    # print("birthday:  ", data["birthday"])
    dict_[int(data["birthday"])] = data["sortable_name"]

print(dict_)
print(sorted(dict_.items(), key=lambda x: (x[0], x[1])))
