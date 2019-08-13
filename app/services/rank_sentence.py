__doc__ = """This file contains function that ranks sentences in text based on the occurrence of keywords."""

from nltk.tokenize import sent_tokenize
from services.lemmatization import lemmatize_all_pos_text
from collections import OrderedDict


def rank_sentences(text, lemmatizer, keyword_score_mapping):

    """
    Create a sentence-score mapping based on the occurrence of keywords
    :param text: string
    :param lemmatizer: nltk WordNetLemmatizer
    :param keyword_score_mapping: dictionary {keyword:score,...}
    :return: dictionary {sentence:score,...}
    """
    keywords = keyword_score_mapping.keys()
    sentences = sent_tokenize(text)
    lemmatized_sentence = [lemmatize_all_pos_text(sentence, lemmatizer) for sentence in sentences]
    scores = []

    for sentence_tokens in lemmatized_sentence:
        sentence_tokens = [token.lower() for token in sentence_tokens]
        sentence_score = 0
        for token in sentence_tokens:
            if token in keywords:
                sentence_score += keyword_score_mapping[token]
        scores.append(sentence_score)
    sentence_score_mapping = dict(zip(sentences, scores))

    sorted_scores = sorted(sentence_score_mapping.items(), key=lambda mapping: mapping[1], reverse=True)
    sorted_mapping = OrderedDict(sorted_scores)
    ranked_sentence = list(sorted_mapping.keys())

    return ranked_sentence



