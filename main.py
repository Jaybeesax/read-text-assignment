# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string

def read_file_content(filename):
    # [assignment] Add your code here
    f = open(filename,"r")
    data = f.read()
    f.close()
    return data.translate(str.maketrans("","",string.punctuation))


def count_words():
     # [assignment] Add your code here
    d = dict()
    text = read_file_content("./story.txt")
    new_text = text.strip()
    new_text = new_text.lower()

    for word in new_text.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
print(count_words())
   
   
   