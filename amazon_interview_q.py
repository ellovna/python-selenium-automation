# """ HW 5
# Create a function that will take a string as an input and return the 1st unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?
#
# How to handle ""? => return Value Error
#
# """
#
# def unique(string: str):
#     # Google
#     string = string.lower()  # google
#
#     for l in string:  # 0(n)   # o => 2
#         if string.count(l) == 1:  # 0(n)
#             return l
#
#     # 0(n^2)
#



def unique(string: str):
    string = string.lower()  # amazon
    d = {}

    for letter in string:     # 0(n)
        if letter not in d:
            d[letter] = 1  # d = {'a': 1, 'm': 1}
        else:
            d[letter] += 1  # d = {'a': 2, 'm': 1}
    print(d)

    for k, v in d.items():   # 0(n)
        if v == 1:
            return k

print(unique('Google'))
print(unique('Amazon'))