import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('log_folder_path', help='Полный путь к файлу')
parser.add_argument('--text', type=str, help='Текст для поиска в файле')

args = parser.parse_args()
for file in os.listdir(args.log_folder_path):
    file_path = os.path.join(args.log_folder_path, file)
    with open(file_path) as log_file:
        log_data = log_file.readlines()
        for line_number, line in enumerate(log_data, start=1):
            if args.text in line:
                word_list = line.split(' ')
                text_index = word_list.index(args.text)
                five_words_after_search_text = word_list[text_index + 1:text_index + 6]
                five_words_before_search_text = word_list[:text_index] if text_index < 6 else word_list[
                                                                                              text_index - 5:text_index]
                print(f'text found in file name: {log_file}, in line_number {line_number}')
                print(f'five words before the searched text {five_words_before_search_text}')
                print(f'The searched text is {args.text}')
                print(f'five words after the searched text {five_words_after_search_text}')
                break
print('Search text is not found in log files')
