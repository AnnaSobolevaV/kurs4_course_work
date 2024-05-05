class RequestErrorException(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else 'Неизвестная ошибка.'

    def __str__(self):
        return self.message


# class FileFoundError(Exception):
#     pass


# def copy_from_to(from_path, to_path):
#     if os.path.exists(to_path):
#         raise FileFoundError
#
#     shutil.copy(from_path, to_path)


# def main():
#     copied = []
#
#     not_copied = []
#
#     from_path = os.path.abspath('dir1')
#
#     to_path = os.path.abspath('dir2')
#
#     files_to_copy = os.listdir(from_path)
#
#     for file_name in files_to_copy:
#
#         from_file_path = os.path.join(from_path, file_name)
#
#         to_file_path = os.path.join(to_path, file_name)
#
#         try:
#
#             copy_from_to(from_file_path, to_file_path)
#
#         except FileFoundError:
#
#             not_copied.append(file_name)
#
#         else:
#
#             copied.append(file_name)
#
#     print(f"Скопированы: {', '.join(copied)}")
#
#     print(f"Уже существуют: {', '.join(not_copied)}")


