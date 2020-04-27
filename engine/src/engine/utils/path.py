import os
import re


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


def specify(path):
    """
    Translate a normalized path to system path
    """
    parts = re.split(r'[\\/]', path)

    if os.name == 'nt':  # Windows
        if not parts[0]:  # This will only happen when translating unix style
            parts.pop(0)
            parts[0] = '{}:'.format(parts[0])

    return '/'.join(parts)
