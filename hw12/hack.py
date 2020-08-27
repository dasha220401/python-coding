import random
import zipfile

PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):

    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False


def hack_archive(file_name):

    file_to_open = zipfile.ZipFile(file_name)
    wrong_passwords = []
    tries = 0

    def generate_num(num_start, num_end, row_length):
        str_result = ''
        list_singular = [str(v) for v in range(num_start, num_end)]
        for i in range(row_length):
            random_singular = random.sample(list_singular, 1)
            str_result += ''.join(random_singular)
        return str_result

    while True:
        password = generate_num(0, 10, PASSWORD_LENGTH)
        if password not in wrong_passwords:
            process_result = extract_archive(file_to_open, password)
            if process_result:
                break
            else:
                tries += 1
                wrong_passwords.append(password)

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')


filename = 'archive.zip'
hack_archive(filename)