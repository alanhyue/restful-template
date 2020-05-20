import datetime
import time
from pathlib import Path


class FileIO():
    @staticmethod
    def glob(pattern):
        '''Get a list of files that satisfy the given pattern. '''
        from glob import glob
        return glob(pattern, recursive=True)
    @staticmethod
    def exists(path):
        return Path(path).exists()
    @staticmethod
    def is_dir(path):
        return Path(path).is_dir()
    @staticmethod
    def is_file(path):
        return Path(path).is_file()
    @staticmethod
    def stat(path):
        return Path(path).stat()
    @staticmethod
    def get_folder(path):
        return Path(path).parent
    @staticmethod
    def resolve(path):
        """Resolve a relative path to an absolute path (e.g., ../file.txt -> D:/data/file.txt)."""
        return str(Path(path).resolve())
    @staticmethod
    def get_ext(path):
        "Return the extension of the file (e.g., C:/a/b/c.txt -> .txt)."
        return Path(path).suffix
    @staticmethod
    def with_ext(path, ext):
        "Return a path with file extension replaced (e.g., C:/a/b/c.txt -> C:a/b/c.log)."
        return str(Path(path).with_suffix(ext))
    @staticmethod
    def filename(path):
        "Return the filename of path (e.g., C:/a/b/c.txt -> c.txt)."
        return Path(path).name
    @staticmethod
    def makedirs(dirpath):
        '''Create (sub)directories in the path. Do nothing if exists.'''
        try:
            os.makedirs(dirpath)
        except OSError:
            pass
    @staticmethod
    def validate_filename(s):
        """
        Return the given string converted to a string that can be used for a clean
        filename. Remove leading and trailing spaces; convert other invalid chars to
        underscores; and remove anything that is not a ASCII char.

        Args:
            s (string): the file name, NOT the path of the file.
        
        Returns:
            string: validated file name for Windows system
        """
        s=s.strip()
        invalid_chars=['"', '\\', "'", ".", "/", " ", "?", ":", "<", ">", "|", "*"]
        for char in invalid_chars:
            s=s.replace(char,'_')
        s = ''.join((c for c in s if 0 < ord(c) < 127)) # remove non-ASCII chars
        return s

def user_confirm(msg="continue? (y/n)"):
    ans = input(msg + ": ")
    return ans.lower() in ['y', 'yes', '1']


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
