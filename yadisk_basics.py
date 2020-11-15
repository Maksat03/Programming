import yadisk

disk = yadisk.YaDisk(token="AgAAAAA9Kp7DAAZQm0kQAq_bWESMmyN16Oc7lzw")

# Проверяет, валиден ли токен
print(disk.check_token())

# Получает общую информацию о диске
print(disk.get_disk_info())

# Выводит содержимое "/some/path"
print(list(disk.listdir("/some/path")))

# Загружает "file_to_upload.txt" в "/destination.txt"
disk.upload("file_to_upload.txt", "/destination.txt")

# То же самое
with open("file_to_upload.txt", "rb") as f:
    disk.upload(f, "/destination.txt")

# Скачивает "/some-file-to-download.txt" в "downloaded.txt"
disk.download("/some-file-to-download.txt", "downloaded.txt")

# Безвозвратно удаляет "/file-to-remove"
disk.remove("/file-to-remove", permanently=True)

# Создаёт новую папку "/test-dir"
print(disk.mkdir("/test-dir"))