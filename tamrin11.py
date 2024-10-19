def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            lines = text.splitlines()
            word_list = text.split()
            
            num_lines = len(lines)
            num_words = len(word_list)
            
            return num_lines, num_words, text
    except FileNotFoundError:
        print("The file was not found.")
        return None, None, None

def count_word_occurrences(text, word):
    return text.lower().split().count(word.lower())

def save_report(report_path, num_lines, num_words, word, word_count):
    with open(report_path, 'w', encoding='utf-8') as report_file:
        report_file.write(f"Number of lines: {num_lines}\n")
        report_file.write(f"Number of words: {num_words}\n")
        report_file.write(f"Occurrences of the word '{word}': {word_count}\n")

def main():
    file_path = input("Enter the path of the text file: ")
    num_lines, num_words, text = analyze_file(file_path)




    
    
    if num_lines is not None and num_words is not None:
        word = input("Enter a word to count its occurrences: ")
        word_count = count_word_occurrences(text, word)
        
        report_path = 'txt.report'
        save_report(report_path, num_lines, num_words, word, word_count)



        
        print("\nReport:")
        with open(report_path, 'r', encoding='utf-8') as report_file:
            print(report_file.read())

if name == "main":
    main()
