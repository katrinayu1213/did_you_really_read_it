# INPUT: string as reference text 
# RETURN a list of words most common words
# only 3 right now 

import nltk
from stop_words import get_stop_words
from nltk.corpus import stopwords
from collections import Counter

def find_common_words_in_ref(ref_text): 
    # read in ref text and create list of words
    text = ref_text
    list_of_words = text.split()

    # remove stop words
    stop_words = list(get_stop_words('en'))         #About 900 stopwords
    nltk_words = list(stopwords.words('english')) #About 150 stopwords
    stop_words.extend(nltk_words)

    # list of core words
    meaningful_words = [w for w in list_of_words if not w in stop_words] 
    # print(meaningful_words)

    wordfreq = {}
    for word in meaningful_words:
        wordfreq[word] = wordfreq.setdefault(word, 0) + 1
    print (wordfreq)

    k = Counter(wordfreq) 

    # Finding 3 highest values 
    high = k.most_common(3)  

    top_one = (high[0])[0]
    top_two = (high[1])[0]
    top_three = (high[2])[0]
    
    ref_common = [top_one, top_two, top_three]
#     print("Common Words in Reference Text: ", ref_common)
    return (ref_common)

find_common_words_in_ref("here is ref text sample")
