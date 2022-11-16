# TODO решить с помощью list comprehension и распечатать его
dict = [{"bin": bin(i), "oct": oct(i), "hex": hex(i),"dec": (i)} for i in range(16)]
from pprint import pprint
pprint(dict)

