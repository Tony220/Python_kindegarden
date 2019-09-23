"""
String methods and functions
"""
a = "howdy, children"
print(a)
a = a.capitalize() # make first character in up case
print(a)
a = a.upper() #make all txt bigger
print(a)
a = a.casefold() #make all txt lower
print(a)
a = a.center(4,"b") #center obj-s
print(a)
c  = a.count("h") #count accurate obj-s
print(c)
byte = a.encode() #code line in byte
print(byte)
bool = a.endswith("n") #reserch which symbol end the line
print(bool)
a = a.expandtabs(5) #share tab
print(a)
f = a.find("d") #return elem id
print(f)
sharestr = "In phrases '{}' are {} h"
print(sharestr.format(a, c)) # isn't easy format print(f"text {} {}") is easier
"""str = "howdy, children {pla}"
str.format_map(pla=" in tajikistan")
print(str) """ #TODO I don't know how it works
bool = isinstance(a, str) #check format of obj-t
print(bool)
f = a.index("h") #the same thng that (a.find)
print(f)
a = a.join(" 1")
print(a)
a = a.translate("russian")
print(a)
"""
List methods and functions
"""
my_list = ["Howdy", "children"]
my_list.append(". You are loozers!")
print(my_list)
my_list.reverse()
print(my_list)