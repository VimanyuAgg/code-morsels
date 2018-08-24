from collections import Counter

# Level 1 & Level 2
def count_words(st):
    return Counter(st.lower().split(" "))

# Level 3
def count_words_bonus(st):
    st = st.lower()
    if ord(st[0]) < 97 or ord(st[0]) > 122:
        st = st[1:]
    if ord(st[len(st)-1]) < 97 or ord(st[len(st)-1]) > 122:
        st = st[:-1]

    return Counter(st.split(" "))