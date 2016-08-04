Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dictionary_name = {} # syntax to create an empty dictionary in python
>>> class = {}
SyntaxError: invalid syntax
>>> sip_class = {}
>>> sip_class = {
	             "Liana" : 70, #item: associated data,
		     "Keisha": 56,
		     "Ciara": 89,
		     "Leah": 98,
		     "Nicole": 68,
		     "Indira": 88

	         }
>>> print(sip_class)
{'Keisha': 56, 'Indira': 88, 'Ciara': 89, 'Nicole': 68, 'Liana': 70, 'Leah': 98}
>>> print (dictionary_name)[key] #print the value for an associated key in a dictionary
{}
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print (dictionary_name)[key] #print the value for an associated key in a dictionary
NameError: name 'key' is not defined
>>> print (sip_class)[keisha]
{'Keisha': 56, 'Indira': 88, 'Ciara': 89, 'Nicole': 68, 'Liana': 70, 'Leah': 98}
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print (sip_class)[keisha]
NameError: name 'keisha' is not defined
>>> print(sip_class)["Keisha"]
{'Keisha': 56, 'Indira': 88, 'Ciara': 89, 'Nicole': 68, 'Liana': 70, 'Leah': 98}
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(sip_class)["Keisha"]
TypeError: 'NoneType' object is not subscriptable
>>> print(sip_class["Keisha"])
56
>>> sip_class["Christine"] = 92
>>> print(sip_class)
{'Keisha': 56, 'Indira': 88, 'Ciara': 89, 'Nicole': 68, 'Liana': 70, 'Leah': 98, 'Christine': 92}
>>> sip_class["Theresa"] = 43
>>> print(sip_class["Theresa"]
      )
43
>>> sip_class["Theresa"] = 72
>>> print(sip_class["Theresa"])
72
>>> sip_class["Keisha"] = 79
>>> print(sip_class["Keisha"])
79
>>> print(sip_class)
{'Keisha': 79, 'Indira': 88, 'Ciara': 89, 'Nicole': 68, 'Liana': 70, 'Leah': 98, 'Christine': 92, 'Theresa': 72}
>>> del sip_class["Nicole"]
>>> print (sip_class["Nicole"])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print (sip_class["Nicole"])
KeyError: 'Nicole'
>>> print(sip_class)
{'Keisha': 79, 'Indira': 88, 'Ciara': 89, 'Liana': 70, 'Leah': 98, 'Christine': 92, 'Theresa': 72}
>>> 
