import os


class WithCurrentDirectory:
    _current_directory: str = None

    @classmethod
    def current_directory(cls, dunder_file):
        if cls._current_directory:
            return cls._current_directory
        else:
            cls._current_directory = os.path.dirname(
                os.path.abspath(dunder_file)
            )
            return cls._current_directory
