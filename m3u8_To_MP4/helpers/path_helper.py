import datetime
import random

WINDOWS_BANNED_CHARACTERS = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']


def updated_resource_path(path, query):
    if query:
        path = f'{path}?{query}'
    return path


def resolve_file_name_by_uri(uri):
    name = uri.split('/')[-1]
    return calibrate_name(name)


def calibrate_mp4_file_name(mp4_file_name):
    mp4_file_name = calibrate_name(mp4_file_name)

    if not mp4_file_name.endswith('.mp4'):
        mp4_file_name += '.mp4'

    return mp4_file_name


def random_5_char():
    random_digits = [str(random.randint(0, 10)) for _ in range(5)]
    return ''.join(random_digits)


def random_name():
    dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    return 'm3u8_To_MP4' + dt_str + random_5_char()+'.mp4'


def calibrate_name(name):
    if len(name.strip()) == 0:
        return random_name()

    for ch in WINDOWS_BANNED_CHARACTERS:
        name = name.replace(ch, '')
    return name
