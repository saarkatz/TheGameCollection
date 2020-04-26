import re


def normalize(path):
    """
    Translate the path for the system
    """
    parts = re.split('[\\/]', path)

    # Windows
    if not parts[0]:
        parts = ['{}:'.format(parts[1].upper())] + parts[2:]
    return '\\'.join(parts)
