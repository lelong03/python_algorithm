def count_words(doc):
    doc_len = len(doc)-1
    i = 0
    count = 0
    while i < doc_len:
        if doc[i] == ' ' and doc[i+1] != ' ':
            count += 1
        i = i + 1
    return count


s = "df asdfdas fdsaf dsaf sdaf asdf sda fadsf sdf sdf sdf fdsf dsf as"
print count_words(s)
