__doc__ = """This file contains functions that lemmatize different types of input."""

from nltk.tokenize import word_tokenize


def lemmatize_all_pos_pair(keyword_score_pair, lemmatizer):

    """
    lemmatize each word in text and return a list of lemmatized tokens
    :param keyword_score_pair: list of tuple, [(keyword, score), ...], where keyword is a string and score is a float
    :param lemmatizer: nltk WordNetLemmatizer
    :return: dictionary {keyword:score, ...}
    """

    # get the keywords in each pair
    tokens = [pair[0] for pair in keyword_score_pair]
    scores = [pair[1] for pair in keyword_score_pair]

    # lemmatize Verb (v), Noun (n), Adverb (r) and Adjective (a)
    lemmatized_tokens = [lemmatizer.lemmatize(t, pos='v') for t in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(t, pos='n') for t in lemmatized_tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(t, pos='r') for t in lemmatized_tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(t, pos='a') for t in lemmatized_tokens]

    # map the score back to keywords
    keyword_score_mapping = dict(zip(lemmatized_tokens, scores))
    return keyword_score_mapping


def lemmatize_all_pos_text(text, lemmatizer, tokenize=True):

    """
    lemmatize each word in text and return a list of lemmatized tokens
    :param text: string
    :param lemmatizer: nltk WordNetLemmatizer
    :param tokenize: boolean (whether the input string needs to be tokenized)
    :return: list of strings (the lemmatized tokens)
    """

    if tokenize:
        tokens = word_tokenize(text)
    else:
        tokens = text
    # lemmatize Verb (v), Noun (n), Adverb (r) and Adjective (a)
    lemmatized_tokens = [lemmatizer.lemmatize(t, pos='v') for t in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(t, pos='n') for t in lemmatized_tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(t, pos='r') for t in lemmatized_tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(t, pos='a') for t in lemmatized_tokens]

    return lemmatized_tokens

