import sys
import re
from collections import Counter
import argparse 


def read_input_with_path_validation(input_path):
    """Read the file and return if the file path is correct.

    Args:
        file_path : To check the path.
    """
    try:
        with open(input_path, 'r') as fin:
            return fin.read()
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        sys.exit(1)


def main(input_path):
    """Receives input_file_path to check validation path and to call word frequency function.

    Args:
        text (file_path).
    """
    content = read_input_with_path_validation(input_path)
    count_word_frequency(content)


def display(word_frequency):
    """Display word frequencies in a formatted table.

    Args:
        word_frequency_counts (list): List of tuples containing (word, frequency).
    """
    print('Word                 Frequency')
    print('-------------------------------')
    for word, frequency in word_frequency:
        print(f'{word:<25} {frequency}')
    print('-------------------------------')


def sort_by_frequency_desc(word_frequency):
    """Changing the original order into Descending order.

    Args:
        word_frequency_counts (list): List of tuples containing (word, frequency).
    """
    word_frequency.sort(key=lambda x: x[1], reverse=True)
    
    display(word_frequency)


def count_word_frequency(content):
    """It computes the unique word frequency.

    Args:
        Text (string): string of input text.
    """
    words = re.findall(r'\b\w+\b', content)
    word_frequency = list(Counter(words).items())
    sort_by_frequency_desc(word_frequency)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Word Frequency Counter')
    parser.add_argument('input_file', type=str, help='Path to input text file')
    args = parser.parse_args()

    main(args.input_file)
