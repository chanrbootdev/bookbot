def word_count(text):
    return(len(text.split()))

def count_chars(text):
    char_count = {}
    for c in text.lower():
        if not(c in char_count.keys()):
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        count = word_count(file_contents)
        my_dict = count_chars(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words found in the document")
        print()
        stop = len(my_dict)
        for i in range(1,stop-1):
            max_so_far = float("-inf")
            max_letter = ""
            for temp in my_dict:
                letter = temp
                if letter.isalpha():
                    occurances = my_dict[letter]
                    if occurances > max_so_far:
                        max_so_far = occurances
                        max_letter = letter    
            if not(max_so_far == float("-inf")):
                print(f"The '{max_letter}' character was found {max_so_far} times")
                del my_dict[max_letter]
        print("--- End report ---")

main()
