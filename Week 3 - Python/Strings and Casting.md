## **Strings and Variables**


**String:** A string is simply a series of characters.


This would be an example of a  string:

```name = "Mehdi Shamaa```



**What can we do with strings?:**

After having assigned a string to a variable, we can attach methods to a string.

For example:

```print(name.upper())``` 

would output:

```MEHDI SHAMAA```



Here is a table of methods we can use with strings:


| Function   | Description                                                             | Example                     |
|------------|-------------------------------------------------------------------------|-----------------------------|
| **len**        | Returns the length of a string                                          | len(string)                 |
| **count**      | Returns the amount of times a string appears in another string          | string.count('t')           |
| **lower**      | Converts a string to all lower case                                     | string.lower()              |
| **upper**      | Converts a string to all Upper case                                     | string.upper()              |
| **title**      | Converts the letter of each word in a string to a capital               | string.title()              |
| **capitalize** | Converts the first letter in a string to a capital                      | string.capitalize()         |
| **replace**    | Replace text in a string with the string specified                      | string.replace('text', 't') |
| **startswith** | Returns either True or False if the string starts with the given string | string.startswith('t')      |

###String Slicing:


```
hello = "Hello World!"

print(hello[10])

print(hello[6:11])
```

Take the above code. The first print command would print the the tenth indexed character in the string, which would be 'd'.

The second print command would the sixth character up to but not including the eleventh character, printing 'World' 




The count method can also be used in the following way:

```
dog = "the dog walked in the park with his friend the cat"

print(dog.count("the"))
```

The above command would ask the program to print the count of the amount of times the word "the" appears in the string, returning a value of 2.