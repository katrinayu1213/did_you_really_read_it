# Purpose: creates a rubric with the 15 most common words in reference text and ouputs a common word score
# INPUT: reference text as a string, student response as a string
# RETURN number of matching words, list of matched words
# TODO: stemming 

import nltk
from stop_words import get_stop_words
from nltk.corpus import stopwords
from collections import Counter

def compare_ref_student_common_words(ref_text, student_response): 
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
#     print (wordfreq)

    k = Counter(wordfreq) 

    # Finding 15 highest values 
    high = k.most_common(15)  

    # list of words
    ref_word_list = []
    for i in high: 
        ref_word_list.append(i[0])
        
    # count the common words in student response 
    common_word_score = 0
    rubric_matched = []

    list_of_scores = []
    for item in ref_word_list:
        if item in student_response:
            rubric_matched.append(item)
            common_word_score += 1
            pass
    print(common_word_score, rubric_matched)
compare_ref_student_common_words("with one member trimming beef in a cannery and another working in a sausage factory the family had a firsthand knowledge of the great majority of packingtown swindles for it was the custom as they found whenever meat was so spoiled that it could not be used for anything else either to can it or else to chop it up into sausage with what had been told them by jonas who had worked in the pickle rooms they could now study the whole of the spoiledmeat industry on the inside and read a new and grim meaning into that old packingtown jestthat they use everything of the pig except the squeal jonas had told them how the meat that was taken out of pickle would often be found sour and how they would rub it up with soda to take away the smell and sell it to be eaten on freelunch counters also of all the miracles of chemistry which they performed giving to any sort of meat fresh or salted whole or chopped any color and any flavor and any odor they chose in the pickling of hams they had an ingenious apparatus by which they saved time and increased the capacity of the planta machine consisting of a hollow needle attached to a pump by plunging this needle into the meat and working with his foot a man could fill a ham with pickle in a few seconds and yet in spite of this there would be hams found spoiled some of them with an odor so bad that a man could hardly bear to be in the room with them to pump into these the packers had a second and much stronger pickle which destroyed the odora process known to the workers as giving them thirty per cent also after the hams had been smoked there would be found some that had gone to the bad formerly these had been sold as number three grade but later on some ingenious person had hit upon a new device and now they would extract the bone about which the bad part generally lay and insert in the hole a whitehot iron after this invention there was no longer number one two and three gradethere was only number one grade the packers were always originating such schemesthey had what they called boneless hams which were all the odds and ends of pork stuffed into casings and california hams which were the shoulders with big knuckle joints and nearly all the meat cut out and fancy skinned hams which were made of the oldest hogs whose skins were so heavy and coarse that no one would buy themthat is until they had been cooked and chopped fine and labeled head cheese it was only when the whole ham was spoiled that it came into the department of elzbieta cut up by the twothousandrevolutions aminute flyers and mixed with half a ton of other meat no odor that ever was in a ham could make any difference there was never the least attention paid to what was cut up for sausage there would come all the way back from europe old sausage that had been rejected and that was moldy and white it would be dosed with borax and glycerin and dumped into the hoppers and made over again for home consumption there would be meat that had tumbled out on the floor in the dirt and sawdust where the workers had tramped and spit uncounted billions of consumption germs there would be meat stored in great piles in rooms and the water from leaky roofs would drip over it and thousands of rats would race about on it it was too dark in these storage places to see well but a man could run his hand over these piles of meat and sweep off handfuls of the dried dung of rats these rats were nuisances and the packers would put poisoned bread out for them they would die and then rats bread and meat would go into the hoppers together this is no fairy story and no joke the meat would be shoveled into carts and the man who did the shoveling would not trouble to lift out a rat even when he saw one there were things that went into the sausage in comparison with which a poisoned rat was a tidbit there was no place for the men to wash their hands before they ate their dinner and so they made a practice of washing them in the water that was to be ladled into the sausage there were the buttends of smoked meat and the scraps of corned beef and all the odds and ends of the waste of the plants that would be dumped into old barrels in the cellar and left there under the system of rigid economy which the packers enforced there were some jobs that it only paid to do once in a long time and among these was the cleaning out of the waste barrels every spring they did it and in the barrels would be dirt and rust and old nails and stale water and cartload after cartload of it would be taken up and dumped into the hoppers with fresh meat and sent out to the public's breakfast some of it they would make into smoked sausage but as the smoking took time and was therefore expensive they would call upon their chemistry department and preserve it with borax and color it with gelatin to make it brown all of their sausage came out of the same bowl but when they came to wrap it they would stamp some of it special and for this they would charge two cents more a pound", "two cents more a pound for a meat. they make it into sausage.")
