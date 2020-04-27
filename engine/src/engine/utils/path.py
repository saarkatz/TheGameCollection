import os
import re


def specify(path):
    """
    Translate a normalized path to system path
    """
    parts = path.split('/')

    if os.name == 'nt':  # Windows
        if not parts[0]:
            parts.pop(0)
            parts[0] = '{}:'.format(parts[0])

    return os.path.sep.join(parts)


def normalize(path):
    """
    Translate a system path to a normal form (Unix style)
    """
    parts = re.split(r'[\\/]', path)

    if os.name == 'nt':  # Windows
        if parts[0].endswith(':'):
            parts[0] = parts[0][:-1]
            parts.insert(0, '')

    return '/'.join(parts)
