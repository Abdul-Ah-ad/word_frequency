import sys
from collections import Counter


def read_path_with_validation(input_path):
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
    """Recieves text to check validation path and to call word frequency function.

    Args:
        text (file_path).
    """
    text = read_path_with_validation(input_path)
    count_word_frequency(text)


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
        
def descending_order(word_frequency):
    """Changing the orignal order into Descending order.

    Args:
        word_frequency_counts (list): List of tuples containing (word, frequency).
    """
    for current in range (len(word_frequency)):
        for next in range(current,len(word_frequency) - 1):
            if word_frequency[current][1] < word_frequency[next][1]:
                word_frequency[current], word_frequency[next] = word_frequency[next], word_frequency[current]

    display(word_frequency)
        
        
def count_word_frequency(text):
    """It computes the unique word frequency.

    Args:
        Text (list): List of input text.
    """
    words = text.split()
    word_frequency= list(Counter(words).items())
    descending_order(word_frequency)
        
if __name__ == "__main__":    
    if len(sys.argv) != 2:
        print('Invalid Arguments!!!')
        sys.exit(1)

    main(sys.argv[1])
    