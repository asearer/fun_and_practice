from nltk.corpus import stopwords
import string

def filter_content(content):
    if not isinstance(content, str):
        raise ValueError("Input content must be a string.")
    
    # Prepare stopwords and a translation table for punctuation removal
    english_stopwords = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove punctuation, convert to lower case, and split into words
    words = content.lower().translate(translator).split()
    filtered_words = [word for word in words if word.isalpha() and word not in english_stopwords]
    
    return ' '.join(filtered_words)


