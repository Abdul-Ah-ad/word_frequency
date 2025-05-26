import sys

def display(
    word_frequency_counts):
    """Display word frequencies in a formatted table.

    Args:
        word_frequency_counts (list): List of tuples containing (word, frequency).
    """
    print("Word                 Frequency")
    print("-------------------------------")
    for word, frequency in word_frequency_counts:
        print(f"{word:<25} {frequency}")
    print("-------------------------------")
        
def descending_order(
    word_frequency_counts):
    """Changing the orignal order into Descending order.

    Args:
        word_frequency_counts (list): List of tuples containing (word, frequency).
    """
    for i in range (len(word_frequency_counts)):
        for j in range(i,len(word_frequency_counts)-1):
            if word_frequency_counts[i][1]<word_frequency_counts[j][1]:
                temp=word_frequency_counts[i]
                word_frequency_counts[i]=word_frequency_counts[j]
                word_frequency_counts[j]=temp
    display(word_frequency_counts)
        
        
def word_frequency_counter(
    text):
    """Creating unique word list and word_frequency_count.

    Args:
        Text (list): List of input text.
    """
    words_list=text.split()
    word_frequency_counts=[]
    unique_word=[]
    for match in words_list:
        if match not in unique_word:
            counter=0
            unique_word.append(match)
            for other in words_list:
                if match==other :
                    counter+=1
            word_frequency_counts.append((match,counter))
    
    descending_order(word_frequency_counts)
        
        



if __name__ == "__main__":
    
    
    if len(sys.argv)!=2:
        print("Invalid Arguments!!!")
        sys.exit(1)

    input_file_path=sys.argv[1]
    
    try:
        with open(input_file_path,'r')as file:
            text=file.read()
        word_frequency_counter(text)
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1) 

    

              
    
    





