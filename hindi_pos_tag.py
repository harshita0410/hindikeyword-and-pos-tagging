from nltk.tag import tnt
from nltk.corpus import indian
import nltk

def hindi_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger

text = input()
model = hindi_model()
new_tagged = (model.tag(nltk.word_tokenize(text)))
print(new_tagged)

# with open("result/output.txt","a") as output_file:
#     output_file.write("\n[INPUT]\n")
#     output_file.write(text)
#     output_file.write("\n[OUTPUT]\n")
#     output_file.write(str(new_tagged))
