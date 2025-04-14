#-----------------------------------------------------------------------------
# Name:        006_(advanced)_subsets_and_supersets
# Purpose:     Write a program using `.update()` and `.discard()` for bulk modifications.
# Author:      Harry Yang
# Created:     06-Apr-2025
#-----------------------------------------------------------------------------

# - Create a set `letters = {'a', 'b', 'c'}`.
letters = {"a","b","c"}
print("original letters : ", letters)

# - Add multiple elements: `'d'`, `'e'`, `'f'`.
letters.update({"d","e","f"})
print("after adding multiple elements , letters : ", letters)

# - Remove `'b'` using `.discard()`.
letters.discard("d")
print("after removing 'd' from the set , letters : ", letters)

# - Print the updated set.
print("the updated letters : ", letters)
