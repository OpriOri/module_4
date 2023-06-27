s = input()
def is_palindrome(s):
# Сравниваем строку с перевернутой строкой
    return s == s[::-1]
print(is_palindrome(s))
