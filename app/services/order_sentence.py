__doc__ = """This file contains function that orders a list of sentences 
based on their order of occurrence in the text."""

from nltk.tokenize import sent_tokenize


def order_sentences(text, selected_sentences):

    """
    Orders a list of sentences based on their order of occurrence in the text

    :param text: string
    :param selected_sentences: list of strings
    :return: list of strings (selected sentences in the correct order)
    """

    sentences = sent_tokenize(text)
    indices = []
    for selected_sentence in selected_sentences:
        indices.append(sentences.index(selected_sentence))

    # group the selected sentences and their order in the format of(sentence, indices)
    groups = zip(selected_sentences, indices)

    # sort the sentences by their indices
    ordered_sents = [group[0] for group in sorted(groups, key=lambda x: x[1])]

    return ordered_sents

