__doc__ = """
This file contains function that extracts keywords from text using the textRank algorithm.
"""

from gensim.summarization.keywords import keywords
from nltk.corpus import stopwords
from services.lemmatization import lemmatize_all_pos_text, lemmatize_all_pos_pair


def extract_keywords(text, lemmatizer):

    """
    extract keywords using textRank algorithm, lemmatize them and return the top n percent keywords
    :param text: string
    :param lemmatizer: nltk WordNetLemmatizer
    :return: dictionary {keyword:score, ...}
    """

    lemmatized_text = " ".join(lemmatize_all_pos_text(text, lemmatizer))

    # use gensim.summarization.keywords to extract keywords
    keywords_scores_pair = keywords(lemmatized_text, lemmatize=True, scores=True)

    # lemmatized the keywords
    lemmatized_keywords_mapping = lemmatize_all_pos_pair(keywords_scores_pair, lemmatizer)
    lemmatized_keywords = lemmatized_keywords_mapping.keys()

    # lemmatize stopwords
    stop_words = set(lemmatize_all_pos_text(stopwords.words('english'), lemmatizer, tokenize=False))

    # remove stopwords from keywords
    keywords_without_stopwords = [keyword for keyword in lemmatized_keywords if keyword not in stop_words]

    keywords_mapping = dict()
    for keyword in keywords_without_stopwords:
        keywords_mapping[keyword] = lemmatized_keywords_mapping[keyword]

    return keywords_mapping
