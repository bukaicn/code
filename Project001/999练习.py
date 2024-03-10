name="Ada Lovelace"
print(name.upper())#转大写
print(name.lower()) #转小写

first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"#f字符串
print(f"Hello,{full_name.title()}")

print("Python")
print("\tPython")#制表符

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language=' pynht ho n ono n onp'
favorite_language
#favorite_language.rstrip()# 删除右空格
#favorite_language.lstrip()# 删除左空格
favorite_language.strip(" on")# 删除所有空格

nostarch_url='abchttps://nostarch.com'# 要去除的不是前面不行
nostarch_url.removeprefix('https://')# 去除前缀

name="ErIc"
n=name.upper()# 全大写
print(f"Hello {n},would you like to learn some Python today?")
m=name.lower()# 全小写
print(f"Hello {m},would you like to learn some Python today?")
p=name.title()# 首大写
print(f"Hello {p},would you like to learn some Python today?")

message="一个从不犯错的人，也从未尝试过新事物"
famous_person=" 爱 因斯 坦 "
c=famous_person.replace(" ","")
print(f'{c}说过：\n\t\t"{message}"')

filename="python_notes.txt"
a=filename.removesuffix(".txt")
print(f"{a}")

print("python_notes.txt".removesuffix(".txt"))