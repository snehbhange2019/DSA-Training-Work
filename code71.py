
def is_pangram(s):
    s = s.lower()
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    return alphabets.issubset(set(s))

text = "The quick brown fox jumps over the lazy dog"
if is_pangram(text):
    print("Pangram")
else:
    print("Not Pangram")