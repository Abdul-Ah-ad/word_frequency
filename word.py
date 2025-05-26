import sys

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
    word_frequency_counter(text)


def display(word_frequency_counts):
    """Display word frequencies in a formatted table.

    Args:
        word_frequency_counts (list): List of tuples containing (word, frequency).
    """
    print('Word                 Frequency')
    print('-------------------------------')
    for word, frequency in word_frequency_counts:
        print(f'{word:<25} {frequency}')
    print('-------------------------------')
        
def descending_order(word_frequency_counts):
    """Changing the orignal order into Descending order.

    Args:
        word_frequency_counts (list): List of tuples containing (word, frequency).
    """
    for current in range (len(word_frequency_counts)):
        for next in range(current,len(word_frequency_counts) - 1):
            if word_frequency_counts[current][1] < word_frequency_counts[next][1]:
                word_frequency_counts[current], word_frequency_counts[next] = word_frequency_counts[next], word_frequency_counts[current]

    display(word_frequency_counts)
        
        
def word_frequency_counter(text):
    """Creating unique word list and word_frequency_count.

    Args:
        Text (list): List of input text.
    """
    words_list = text.split()
    word_frequency_counts = []
    unique_word = []
    for match in words_list:
        if match not in unique_word:
            counter = 0
            unique_word.append(match)
            for other in words_list:
                if match == other :
                    counter += 1
            word_frequency_counts.append((match,counter))
    
    descending_order(word_frequency_counts)
        
        



if __name__ == "__main__":
    
    
    if len(sys.argv) != 2:
        print('Invalid Arguments!!!')
        sys.exit(1)

    main(sys.argv[1])


    

              
    
    





