# test_sort_words.py
import pytest
from sort_words import sort_words

def test_sort_words():
    words = ["apple", "banana", "cherry"]
    assert sort_words(words) == ["apple", "banana", "cherry"]

def test_sort_words_empty_list():
    words = []
    assert sort_words(words) == []

def test_sort_words_single_element():
    words = ["hello"]
    assert sort_words(words) == ["hello"]

def test_sort_words_duplicates():
    words = ["apple", "banana", "apple"]
    assert sort_words(words) == ["apple", "apple", "banana"]

def test_sort_words_non_ascii():
    words = ["apple", "banana", "çiçek"]
    assert sort_words(words) == ["apple", "banana", "çiçek"]

def test_sort_words_mixed_case():
    words = ["Apple", "banana", "CHERRY"]
    assert sort_words(words) == ["Apple", "banana", "CHERRY"]
