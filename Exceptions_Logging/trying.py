# my_dict = {"Macbook" : "Pro", "Developer" : "Nick", "Iphone" : 1}
# print(my_dict.get("Developer"))
# print(my_dict.get("Key"))
# print(my_dict)
# print(my_dict.setdefault("Developer"))
# print(my_dict.setdefault("Key", 2))
# print(my_dict)

# my_dict={
#  "John" : {"Phone":"0678727361", "Instagram":"@johninst", "tiktok":"@john"},
#  "Sophia" : {"Phone":"0678727243", "Instagram":"@sophiainst", "tiktok":"@sophia"},
#  "Julia" : {"Phone":"0662327361", "Instagram":"@juliainst", "tiktok":"@julia"},
#  "Oleg" : {"Phone":"0678727362", "Instagram":"@oleginst", "tiktok":"@oleg"}
#   }
# user = my_dict[input("Enter name: ")][input("Phone, Instagram or Tiktok?: ")]
# print(user)
#

dictt = {}
dictt.setdefault(input("Your name: "), input("your things: ").split())
dictt.setdefault(input("Your name: "), input("your things: ").split())
dictt.setdefault(input("Your name: "), input("your things: ").split())
print(dictt)
print()
print("TEAM: ", dictt.keys())
print("THINGS: ", dictt.values())





