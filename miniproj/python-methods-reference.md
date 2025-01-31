# Python Data Types and Methods Reference

## Lists
| Method | Description | Example | Output |
|--------|-------------|---------|---------|
| `append(x)` | Adds element x to end of list | `lst = [1, 2]`<br>`lst.append(3)` | `[1, 2, 3]` |
| `extend(iterable)` | Adds all elements from iterable | `lst = [1, 2]`<br>`lst.extend([3, 4])` | `[1, 2, 3, 4]` |
| `insert(i, x)` | Inserts x at position i | `lst = [1, 2]`<br>`lst.insert(1, 'a')` | `[1, 'a', 2]` |
| `remove(x)` | Removes first occurrence of x | `lst = [1, 2, 1]`<br>`lst.remove(1)` | `[2, 1]` |
| `pop([i])` | Removes & returns item at i | `lst = [1, 2, 3]`<br>`lst.pop(1)` | Returns `2`<br>List becomes `[1, 3]` |
| `clear()` | Removes all items | `lst = [1, 2]`<br>`lst.clear()` | `[]` |
| `index(x)` | Returns index of first x | `lst = [1, 2, 1]`<br>`lst.index(1)` | `0` |
| `count(x)` | Counts occurrences of x | `lst = [1, 2, 1]`<br>`lst.count(1)` | `2` |
| `sort()` | Sorts list in place | `lst = [3, 1, 2]`<br>`lst.sort()` | `[1, 2, 3]` |
| `reverse()` | Reverses list in place | `lst = [1, 2, 3]`<br>`lst.reverse()` | `[3, 2, 1]` |
| `copy()` | Returns shallow copy | `lst = [1, 2]`<br>`new = lst.copy()` | `new = [1, 2]` |

## Strings
| Method | Description | Example | Output |
|--------|-------------|---------|---------|
| `upper()` | Converts to uppercase | `"hello".upper()` | `"HELLO"` |
| `lower()` | Converts to lowercase | `"HELLO".lower()` | `"hello"` |
| `strip()` | Removes leading/trailing whitespace | `" hello ".strip()` | `"hello"` |
| `replace(old, new)` | Replaces old with new | `"hello".replace('l','w')` | `"hewwo"` |
| `split([sep])` | Splits string on separator | `"a,b,c".split(',')` | `['a', 'b', 'c']` |
| `join(iterable)` | Joins iterable with string | `",".join(['a','b','c'])` | `"a,b,c"` |
| `startswith(prefix)` | Checks if starts with prefix | `"hello".startswith('he')` | `True` |
| `endswith(suffix)` | Checks if ends with suffix | `"hello".endswith('lo')` | `True` |
| `find(sub)` | Finds first occurrence of substring | `"hello".find('l')` | `2` |
| `count(sub)` | Counts occurrences of substring | `"hello".count('l')` | `2` |
| `isalpha()` | Checks if all chars are letters | `"hello".isalpha()` | `True` |
| `isdigit()` | Checks if all chars are digits | `"123".isdigit()` | `True` |
| `isalnum()` | Checks if all chars are alphanumeric | `"hello123".isalnum()` | `True` |

## Dictionaries
| Method | Description | Example | Output |
|--------|-------------|---------|---------|
| `get(key[,default])` | Returns value for key | `d = {'a':1}`<br>`d.get('b', 0)` | `0` |
| `keys()` | Returns view of keys | `d = {'a':1, 'b':2}`<br>`d.keys()` | `dict_keys(['a', 'b'])` |
| `values()` | Returns view of values | `d = {'a':1, 'b':2}`<br>`d.values()` | `dict_values([1, 2])` |
| `items()` | Returns view of key-value pairs | `d = {'a':1}`<br>`d.items()` | `dict_items([('a', 1)])` |
| `pop(key[,default])` | Removes key & returns value | `d = {'a':1}`<br>`d.pop('a')` | `1` |
| `update(other)` | Updates dict with other's pairs | `d = {'a':1}`<br>`d.update({'b':2})` | `{'a':1, 'b':2}` |
| `clear()` | Removes all items | `d = {'a':1}`<br>`d.clear()` | `{}` |
| `copy()` | Returns shallow copy | `d = {'a':1}`<br>`new = d.copy()` | `new = {'a':1}` |

## Sets
| Method | Description | Example | Output |
|--------|-------------|---------|---------|
| `add(x)` | Adds element x | `s = {1, 2}`<br>`s.add(3)` | `{1, 2, 3}` |
| `remove(x)` | Removes x, raises error if missing | `s = {1, 2}`<br>`s.remove(1)` | `{2}` |
| `discard(x)` | Removes x if present | `s = {1, 2}`<br>`s.discard(3)` | `{1, 2}` |
| `pop()` | Removes and returns arbitrary element | `s = {1, 2}`<br>`s.pop()` | Returns `1` or `2` |
| `clear()` | Removes all elements | `s = {1, 2}`<br>`s.clear()` | `set()` |
| `union(other)` | Returns union of sets | `{1,2}.union({2,3})` | `{1, 2, 3}` |
| `intersection(other)` | Returns intersection of sets | `{1,2}.intersection({2,3})` | `{2}` |
| `difference(other)` | Returns difference of sets | `{1,2}.difference({2,3})` | `{1}` |
| `issubset(other)` | Tests if set is subset | `{1,2}.issubset({1,2,3})` | `True` |
| `issuperset(other)` | Tests if set is superset | `{1,2,3}.issuperset({1,2})` | `True` |

## Tuples
Tuples are immutable, so they have fewer methods than lists. Their main methods are:
| Method | Description | Example | Output |
|--------|-------------|---------|---------|
| `count(x)` | Counts occurrences of x | `(1,2,1).count(1)` | `2` |
| `index(x)` | Returns index of first x | `(1,2,1).index(2)` | `1` |

## Numbers (int/float)
| Method | Description | Example | Output |
|--------|-------------|---------|---------|
| `as_integer_ratio()` | Returns fraction tuple | `2.5.as_integer_ratio()` | `(5, 2)` |
| `is_integer()` | Checks if float is integer | `2.0.is_integer()` | `True` |
| `hex()` | Converts to hex string | `hex(16)` | `'0x10'` |
| `bin()` | Converts to binary string | `bin(4)` | `'0b100'` |
| `oct()` | Converts to octal string | `oct(8)` | `'0o10'` |
