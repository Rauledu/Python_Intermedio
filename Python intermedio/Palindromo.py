# word = input("Introduce la palabra: ")
# if str(word) == str(word)[::-1]:
#     print(" Is Palindrome")
# else:
#     print("Not Palindrome")


# Palabra = input("Introduce la palabra: ")
# print(f"La palabra escrita de izquierda a derecha es:{Palabra}")

# print(f"La palabra escrita de derecha a izquierda es:{Palabra[::-1]} ")


def es_palindromo(word):
    return word == word[:: -1]
