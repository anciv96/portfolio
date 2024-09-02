class OrderTorFileNotFoundError(FileNotFoundError):
    pass


class OrderTorFilePermissionError(PermissionError):
    pass


class OrderTorFileIOError(IOError):
    pass
