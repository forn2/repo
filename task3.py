# TODO Найдите количество книг, которое можно разместить на дискете
# Данные задачи
diskette_size_mb = 1.44  # Объём дискеты в мегабайтах
pages_per_book = 100     # Количество страниц в книге
lines_per_page = 50      # Число строк на странице
chars_per_line = 25      # Количество символов в строке
bytes_per_char = 4       # Объём одного символа в байтах

# Расчёты
diskette_size_bytes = diskette_size_mb * 1024 * 1024
total_chars_per_book = pages_per_book * lines_per_page * chars_per_line
book_size_bytes = total_chars_per_book * bytes_per_char

# Количество книг, которые поместятся
books_fit = int(diskette_size_bytes // book_size_bytes)

# Результат
print(f"Количество книг, помещающихся на дискету: {books_fit}")

