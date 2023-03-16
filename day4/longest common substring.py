import difflib
def get_overlap(s1, s2):
    s = difflib.SequenceMatcher(None, s1, s2)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2)) 
    return s1[pos_a:pos_a+size]
s1 = "pirate"
s2 = "teepee"
print(get_overlap(s1, s2))
