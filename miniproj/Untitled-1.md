Data Type/Structure,Method,Description,Example
int,bit_length(),Returns the number of bits required to represent the integer in binary.,x = 5; x.bit_length() → 3
int,to_bytes(),Returns an array of bytes representing the integer.,x = 1024; x.to_bytes(2, byteorder='big') → b'\x04\x00'
float,is_integer(),Returns True if the float is an integer.,x = 5.0; x.is_integer() → True
float,hex(),Returns a hexadecimal string representation of the float.,x = 3.5; x.hex() → '0x1.c000000000000p+1'
str,upper(),Converts the string to uppercase.,"hello".upper() → "HELLO"
str,lower(),Converts the string to lowercase.,"HELLO".lower() → "hello"
str,strip(),Removes leading and trailing whitespace.,"  hello  ".strip() → "hello"
str,split(),Splits the string into a list based on a delimiter.,"hello world".split() → ['hello', 'world']
str,join(),Joins elements of an iterable into a single string.," ".join(['hello', 'world']) → "hello world"
str,replace(),Replaces a substring with another substring.,"hello".replace("h", "j") → "jello"
str,find(),Returns the index of the first occurrence of a substring.,"hello".find("e") → 1
list,append(),Adds an element to the end of the list.,lst = [1, 2]; lst.append(3); print(lst) → [1, 2, 3]
list,extend(),Adds elements from an iterable to the end of the list.,lst = [1, 2]; lst.extend([3, 4]); print(lst) → [1, 2, 3, 4]
list,insert(),Inserts an element at a specific index.,lst = [1, 2]; lst.insert(1, 1.5); print(lst) → [1, 1.5, 2]
list,remove(),Removes the first occurrence of a value.,lst = [1, 2, 3]; lst.remove(2); print(lst) → [1, 3]
list,pop(),Removes and returns the element at a specific index.,lst = [1, 2, 3]; lst.pop(1); print(lst) → 2 (list becomes [1, 3])
list,index(),Returns the index of the first occurrence of a value.,lst = [1, 2, 3]; lst.index(2) → 1
list,count(),Returns the number of occurrences of a value.,lst = [1, 2, 2, 3]; lst.count(2) → 2
list,sort(),Sorts the list in place.,lst = [3, 1, 2]; lst.sort(); print(lst) → [1, 2, 3]
list,reverse(),Reverses the list in place.,lst = [1, 2, 3]; lst.reverse(); print(lst) → [3, 2, 1]
tuple,index(),Returns the index of the first occurrence of a value.,tup = (1, 2, 3); tup.index(2) → 1
tuple,count(),Returns the number of occurrences of a value.,tup = (1, 2, 2, 3); tup.count(2) → 2
set,add(),Adds an element to the set.,s = {1, 2}; s.add(3); print(s) → {1, 2, 3}
set,remove(),Removes an element from the set. Raises an error if not found.,s = {1, 2}; s.remove(2); print(s) → {1}
set,discard(),Removes an element from the set if it exists.,s = {1, 2}; s.discard(2); print(s) → {1}
set,union(),Returns the union of two sets.,{1, 2}.union({2, 3}) → {1, 2, 3}
set,intersection(),Returns the intersection of two sets.,{1, 2}.intersection({2, 3}) → {2}
set,difference(),Returns the difference between two sets.,{1, 2}.difference({2, 3}) → {1}
set,symmetric_difference(),Returns the symmetric difference between two sets.,{1, 2}.symmetric_difference({2, 3}) → {1, 3}
dict,keys(),Returns a view of the dictionary's keys.,d = {'a': 1, 'b': 2}; d.keys() → dict_keys(['a', 'b'])
dict,values(),Returns a view of the dictionary's values.,d = {'a': 1, 'b': 2}; d.values() → dict_values([1, 2])
dict,items(),Returns a view of the dictionary's key-value pairs.,d = {'a': 1, 'b': 2}; d.items() → dict_items([('a', 1), ('b', 2)])
dict,get(),Returns the value for a key, or a default if the key is not found.,d = {'a': 1}; d.get('a', 0) → 1
dict,pop(),Removes and returns the value for a key.,d = {'a': 1}; d.pop('a'); print(d) → 1 (d becomes {})
dict,update(),Updates the dictionary with key-value pairs from another dictionary or iterable.,d = {'a': 1}; d.update({'b': 2}); print(d) → {'a': 1, 'b': 2}
dict,clear(),Removes all items from the dictionary.,d = {'a': 1}; d.clear(); print(d) → {}