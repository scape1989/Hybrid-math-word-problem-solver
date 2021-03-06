from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from string import punctuation
import re

def text_to_wordlist(text, remove_stopwords=False, stem_words=False):
    # Clean the text, with the option to remove stopwords and to stem words.    
    # Convert words to lower case and split them
    text = text.split()
    # Optionally, remove stop words
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        text = [w for w in text if not w in stops]
    
    text = " ".join(text)
    # Clean the text
    text = re.sub(r"[^A-Za-z0-9^.,!\/'-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"ain't", "am not",text)
    text = re.sub(r"aren't","are not",text)
    text = re.sub(r"can't","cannot",text)
    text = re.sub(r"can't've","cannot have",text)
    text = re.sub(r"'cause","because",text)
    text = re.sub(r"could've","could have",text)
    text = re.sub(r"couldn't","could not",text)
    text = re.sub(r"couldn't've","could not have",text)
    text = re.sub(r"didn't","did not",text)
    text = re.sub(r"doesn't","does not",text)
    text = re.sub(r"don't","do not",text)
    text = re.sub(r"hadn't","had not",text)
    text = re.sub(r"hadn't've","had not have",text)
    text = re.sub(r"hasn't","has not",text)
    text = re.sub(r"haven't","have not",text)
    text = re.sub(r"he'd","he would",text)
    text = re.sub(r"he'd've","he would have",text)
    text = re.sub(r"he'll","he will",text)
    text = re.sub(r"he'll've","he will have",text)
    text = re.sub(r"he's","he is",text)
    text = re.sub(r"how'd","how did",text)
    text = re.sub(r"how'd'y","how do you",text)
    text = re.sub(r"how'll","how will",text)
    text = re.sub(r"how's","how is",text)
    text = re.sub(r"I'd","I would",text)
    text = re.sub(r"I'd've","I would have",text)
    text = re.sub(r"I'll","I will",text)
    text = re.sub(r"I'll've","I will have",text)
    text = re.sub(r"I'm","I am",text)
    text = re.sub(r"I've","I have",text)
    text = re.sub(r"isn't","is not",text)
    text = re.sub(r"it'd","it had",text)
    text = re.sub(r"it'd've","it would have",text)
    text = re.sub(r"it'll","it will",text)
    text = re.sub(r"it'll've","it will have",text)
    text = re.sub(r"it's","it is",text)
    text = re.sub(r"let's","let us",text)
    text = re.sub(r"ma'am","madam",text)
    text = re.sub(r"mayn't","may not",text)
    text = re.sub(r"might've","might have",text)
    text = re.sub(r"mightn't","might not",text)
    text = re.sub(r"mightn't've","might not have",text)
    text = re.sub(r"must've","must have",text)
    text = re.sub(r"mustn't","must not",text)
    text = re.sub(r"mustn't've","must not have",text)
    text = re.sub(r"needn't","need not",text)
    text = re.sub(r"needn't've","need not have",text)
    text = re.sub(r"o'clock","of the clock",text)
    text = re.sub(r"oughtn't","ought not",text)
    text = re.sub(r"oughtn't've","ought not have",text)
    text = re.sub(r"shan't","shall not",text)
    text = re.sub(r"sha'n't","shall not",text)
    text = re.sub(r"shan't've","shall not have",text)
    text = re.sub(r"she'd","she would",text)
    text = re.sub(r"she'd've","she would have",text)
    text = re.sub(r"she'll","she will",text)
    text = re.sub(r"she'll've","she will have",text)
    text = re.sub(r"she's","she is",text)
    text = re.sub(r"should've","should have",text)
    text = re.sub(r"shouldn't","should not",text)
    text = re.sub(r"shouldn't've","should not have",text)
    text = re.sub(r"so've","so have",text)
    text = re.sub(r"so's","so is",text)
    text = re.sub(r"that'd","that would",text)
    text = re.sub(r"that'd've","that would have",text)
    text = re.sub(r"that's","that is",text)
    text = re.sub(r"there'd","there had",text)
    text = re.sub(r"there'd've","there would have",text)
    text = re.sub(r"there's","there is",text)
    text = re.sub(r"they'd","they would",text)
    text = re.sub(r"they'd've","they would have",text)
    text = re.sub(r"they'll","they will",text)
    text = re.sub(r"they'll've","they will have",text)
    text = re.sub(r"they're","they are",text)
    text = re.sub(r"they've","they have",text)
    text = re.sub(r"to've","to have",text)
    text = re.sub(r"wasn't","was not",text)
    text = re.sub(r"we'd","we had",text)
    text = re.sub(r"we'd've","we would have",text)
    text = re.sub(r"we'll","we will",text)
    text = re.sub(r"we'll've","we will have",text)
    text = re.sub(r"we're","we are",text)
    text = re.sub(r"we've","we have",text)
    text = re.sub(r"weren't","were not",text)
    text = re.sub(r"what'll","what will",text)
    text = re.sub(r"what'll've","what will have",text)
    text = re.sub(r"what're","what are",text)
    text = re.sub(r"what's","what is",text)
    text = re.sub(r"what've","what have",text)
    text = re.sub(r"when's","when is",text)
    text = re.sub(r"when've","when have",text)
    text = re.sub(r"where'd","where did",text)
    text = re.sub(r"where's","where is",text)
    text = re.sub(r"where've","where have",text)
    text = re.sub(r"who'll","who will",text)
    text = re.sub(r"who'll've","who will have",text)
    text = re.sub(r"who's","who is",text)
    text = re.sub(r"who've","who have",text)
    text = re.sub(r"why's","why is",text)
    text = re.sub(r"why've","why have",text)
    text = re.sub(r"will've","will have",text)
    text = re.sub(r"won't","will not",text)
    text = re.sub(r"won't've","will not have",text)
    text = re.sub(r"would've","would have",text)
    text = re.sub(r"wouldn't","would not",text)
    text = re.sub(r"wouldn't've","would not have",text)
    text = re.sub(r"y'all","you all",text)
    text = re.sub(r"y'alls","you alls",text)
    text = re.sub(r"y'all'd","you all would",text)
    text = re.sub(r"y'all'd've","you all would have",text)
    text = re.sub(r"y'all're","you all are",text)
    text = re.sub(r"y'all've","you all have",text)
    text = re.sub(r"you'd","you had",text)
    text = re.sub(r"you'd've","you would have",text)
    text = re.sub(r"you'll","you you will",text)
    text = re.sub(r"you'll've","you you will have",text)
    text = re.sub(r"you're","you are",text)
    text = re.sub(r"you've","you have",text)
    text = re.sub(r'(?<!\d)\.(?!\d)', '.', text)
    text = re.sub(r"!", "", text)
    text = re.sub(r"\.\s*\.", " ", text)
    text = re.sub(r"'", "", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"/", " / ", text)
    text = re.sub(r"\(", " ( ", text)
    text = re.sub(r"\)", " ) ", text)
    text = re.sub(r"\[", " [ ", text)
    text = re.sub(r"\]", " ] ", text)
    text = re.sub(r"\$", " dollar ", text)
    text = re.sub(r"\s+", " ", text)
	
 
 
    # Optionally, shorten words to their stems
    if stem_words:
        text = text.split()
        stemmer = SnowballStemmer('english')
        stemmed_words = [stemmer.stem(word) for word in text]
        text = " ".join(stemmed_words)    
    # Return a list of words
    return(text)
