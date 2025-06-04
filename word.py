import argparse
import re
import sys
from collections import Counter, namedtuple
from typing import List


WordFrequency = namedtuple('WordFrequency', ['word', 'frequency'])


def get_file_content_safe(input_path: str) -> str:
    """
    Safely reads and returns the content of a file as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: Contents of the file if it exists.

    Exits:
        Exits the program if the file is not found.
    """
    try:
        with open(input_path, 'r') as fin:
            return fin.read()
    except FileNotFoundError:
        print(f'Error: File "{input_path}" not found.')
        sys.exit(1)


def count_word_frequency(content: str) -> List[WordFrequency]:
    """
    Count the frequency of each unique word in the content.

    Args:
        content (str): Input text.

    Returns:
        List[WordFrequency]: List of WordFrequency namedtuples.
    """
    words = re.findall(r"\b\w+(?:[-']\w+)*\b", content)
    word_counts = Counter(words)
    return [WordFrequency(word, freq) for word, freq in word_counts.items()]


def sort_by_frequency_desc(
    word_frequencies: List[WordFrequency]
) -> List[WordFrequency]:
    """
    Sort words by frequency in descending order.

    Args:
        word_frequencies (List[WordFrequency]): List of word-frequency pairs.

    Returns:
        List[WordFrequency]: Sorted list.
    """
    return sorted(word_frequencies, key=lambda wf: wf.frequency, reverse=True)


def display(word_frequencies: List[WordFrequency]) -> None:
    """
    Display word frequencies in a formatted table.

    Args:
        word_frequencies (List[WordFrequency]): List of word-frequency pairs.
    """
    print('Word                 Frequency')
    print('-------------------------------')
    for wf in word_frequencies:
        print(f'{wf.word:<25} {wf.frequency}')
    print('-------------------------------')


def main(input_path: str) -> None:
    """
    Main function to process the file and display word frequencies.

    Args:
        input_path (str): Path to the input text file.
    """
    content = get_file_content_safe(input_path)
    word_frequencies = count_word_frequency(content)
    sorted_frequencies = sort_by_frequency_desc(word_frequencies)
    display(sorted_frequencies)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word Frequency Counter')
    parser.add_argument('input_file', type=str, help='Path to input text file')
    args = parser.parse_args()
    main(args.input_file)
