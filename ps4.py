# Practice Set 4
# INFO-I211 - Spring 2023

"""
Overview
========

Erika and Matt are planning a "cheeses of the world" lunch.

But oh no! Their `cheeses.txt` file was corrupted.
Cheeses were duplicated, and there appear to be tabs at the
beginning of most lines:

```
    roquefort, france
roquefort, france
        mozzarella, italy
epoisses, france
            mozzarella, italy
```

This will take hours to fix this by hand 😟

We need to know which cheeses come from each country.
While Matt drives to Jungle Jim's International Market,
help Erika read the file, process it, and print something
where the countries are in alphabetical order, and the
cheeses from each country are also in alphabetical order:

```
france:
    epoisses
    roguefort
italy:
    mozzarella
```

We will be tight on time, so we should also direct Matt
based on which countries have the most cheeses:

```
[('france', 2), ('italy', 1)]
```

Practice writing *functions* that take an input
and `return` an output. When completed, all of your functions
should work together to fix the input file.

What to submit
==============

Rename `ps4.py` to `{username}_ps4.py` and submit the
Python script on Canvas.

For example, Alexander would submit `hayesall_ps4.py` on Canvas.

Tips
====

1. Practice iterative development. If you see this:

```
# Implement `list_to_string()` which takes a list of integers
# like [1, 2, 3] and returns "1 2 3".
def list_to_string(input_list):
    pass
```

... then you might implement + test the function works like this:

```
def list_to_string(input_list):
    return str(input_list)[1:-1].replace(", ", " ")

print(list_to_string([1, 2, 3]))
```

2. Make sure to *return* values from your function,
   *printing* values is not the same as returning them!
3. When you're confident that your functions are correct,
   clean up any debugging code you wrote. Your final
   implementation should *only* print the result of PS 4.6
"""


# PS 4.1
# ------
# `safe_load_file` takes a string representing the name of a file
# as an input. If the file exists, return the file's contents as a string.
# If the file does not exist, return the empty string.
#
# Examples:
# >>> print(safe_load_file("cheeses.txt"))
# roquefort, french\nmozzarella, italy\nepoisses, france ...
#
# >>> print(safe_load_file("C:\\User\\notes.txt"))
#           <--- nothing shown because the empty string was printed
#
# Hint:
# - Use `try` and `except FileNotFoundError` to catch the error.
# - The `os` module is an alternative way to approach this.
from collections import OrderedDict

def safe_load_file(file_path):
    try:
        with open(file_path) as obj:
             contents = obj.read()
             return (contents)
    except FileNotFoundError:
        message = "Sorry, the file " + file_path + " does not exist."
        print(message)

    pass


# PS 4.2
# ------
# Implement `to_nested_list`, which takes a string as input and
# converts it to a list-of-lists. Assume the input is a
# newline-separated string, may contain tabs, and each line
# contains two values separated by a comma and a space (", ").
#
# Example:
# >>> to_nested_list("\t\troquefort, french\nroquefort, french")
# [['roquefort', 'french'], ['roquefort', 'french']]


def to_nested_list(string_data):
    res = string_data.split("\n")
    list1 = []
    for i in res:
        string = " ".join(i.split())
        s = string.split(',')
        list1.append(s)
    return (list1)
    pass


# PS 4.3
# ------
# Write `nested_lists_to_dict`, which takes a "list of list of strings"
# where each inner list has a (value, key) pair. Return a dictionary
# where each key maps to a list of *unique* values.
#
# Examples:
# >>> nested_lists_to_dict([["feta", "greece"], ["feta", "greece"]])
# {'greece': ['feta']}
# >>> nested_lists_to_dict([["roquefort", "france"], ["roquefort", "france"], ["feta", "greece"], ["brie", "france"]])
# {'france': ['roquefort', 'brie'], 'greece': ['feta']}


def nested_lists_to_dict(input_lol):
    my_dict = {}
    keys = []

    # To get the keys from the list
    for i in input_lol:
        if i[0] != '':
            keys.append(i[1])
            keys = sorted(list(set(keys)))  # to remove the duplicates and sorting the values alphabetically

    # To get the values from the list
    for i in keys:
        values = []
        for j in input_lol:
            if i in j and j[0] not in values:
                values.append(j[0])
        my_dict[i] = sorted(values)

    return (my_dict)

    pass


# PS 4.4
# ------
# Implement `format_dict_of_lists` which takes a dictionary of lists,
# sorts the keys in the dictionary, and returns a string. The
# keys should be sorted, and the values should be sorted.

#
# >>> print(format_dict_of_lists({'france': ['roquefort', 'brie'], 'greece': ['feta', 'halloumi']}))
# france:
#   brie
#   roquefort
# greece:
#   feta
#   halloumi
#
# Hint:
# You can use '\t' to create a tab, and a `\n` to create
# a newline. Make sure this function *returns* a string,
# *printing* the output directly will cause an error!


def format_dict_of_lists(input_dol):
    input_dol = OrderedDict(sorted(input_dol.items()))  # to sort the dictionary by key
    string = ''
    for key, value in input_dol.items():
        string = string + key + ": \t\n"
        for i in sorted(value):
            string = string + "\t" + i + "\n"
    return string

    pass


# PS 4.5
# ------
# Write `summarize_dict_of_lists`, which takes a dictionary mapping
# strings to lists, and returns a list of tuples representing the
# key and length of each list. The tuples be should be sorted from
# highest to lowest.
#
# Example:
# >>> summarize_dict_of_lists({'france': ['roquefort', 'brie'], 'greece': ['feta']})
# [('france', 2), ('greece', 1)]


def summarize_dict_of_lists(input_dol):
    list = []
    for key, value in input_dol.items():
        tup = (key, len(value))
        list.append(tup)

    list.sort(key = lambda x:x[1], reverse = True)
    return (list)

    pass


# PS 4.6
# ------
# Uncomment the following `if __name__ == "__main__` lines
# with CTRL + /        or        ⌘ + /
# Running this file using the "Run Python File" button
# (triangle in the top right), or invoking from the terminal
# with `python ps4.py` should now display the cheeses.
#
if __name__ == "__main__":
    cheeses = nested_lists_to_dict(to_nested_list(safe_load_file("/Users/nandhakumar/Downloads/cheeses-corrupted.txt")))
    # print(cheeses)
    print(format_dict_of_lists(cheeses))
    print(summarize_dict_of_lists(cheeses))
