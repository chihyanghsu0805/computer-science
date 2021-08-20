# Data Structures

## Hash Table
Hash table use hash function to map keys to values to achieve efficient lookup, O(1).
Collisions happen when two keys have the same hash code.
There are severak ways to avoid collision,
- Chaining with Linked List or Binary Search Tree.
- Open Addressing with Linear Probing.

## Array List
Array list have dynamic size to overcome fixed array size in Java.

## String Builder
Concatenating strings in the syntax of

        s = ""
        for word in words:
            s1 = s1+word

requires O(xn<sup>2</sup>) with x being characters and n as the number of words.
String Builder act as an resizeble array to store all strings and join them when needed.

## LinkedList
Compared to array, LinkedList offers O(1) add and remove.
