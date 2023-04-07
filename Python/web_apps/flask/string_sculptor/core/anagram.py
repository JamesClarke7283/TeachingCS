"""Module contains our anagram maker functions."""
import nltk
import itertools
from collections import defaultdict, Counter
from nltk.corpus import words

nltk.download('words')


def is_anagram(phrase1, phrase2):
    return sorted(phrase1.lower().replace(" ", "")) == sorted(phrase2.lower().replace(" ", ""))

def build_anagram_dict(word_list):
    anagram_dict = defaultdict(set)
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].add(word)
    return anagram_dict

def valid_combinations(input_counter, word_counters):
    for word_counter in word_counters:
        if all(input_counter[char] >= word_counter[char] for char in word_counter):
            yield word_counter


def anagram_phrases(input_phrase, max_length=5):
    input_letters = ''.join(sorted(input_phrase.lower().replace(" ", "")))
    input_counter = Counter(input_letters)
    nltk_words = set(word.lower() for word in words.words())
    anagram_dict = build_anagram_dict(nltk_words)

    valid_words = [word for word in nltk_words if set(word).issubset(set(input_letters))]
    word_counters = [Counter(word) for word in valid_words]
    
    for i in range(1, max_length + 1):
        for word_combination in itertools.combinations(valid_words, i):
            combined_counter = sum((word_counters[valid_words.index(word)] for word in word_combination), Counter())
            if input_counter == combined_counter:
                yield ' '.join(word_combination)


if __name__ == "__main__":
    # Example usage
    input_phrase = "silent"
    n = None
    a = anagram_phrases(input_phrase)
    while n != "listen":
        n = next(a)
        print(n)
