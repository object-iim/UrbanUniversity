from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count: int, file_name: str):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(1, word_count+1):
        file.write(f"Какое-то слово №{i}\n")
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start_1 = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_start_2 = datetime.now()
print(f'Работа потоков: {time_start_2 - time_start_1}')

thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end = datetime.now()
print(f'Работа потоков: {time_end - time_start_2}')