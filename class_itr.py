class FileIterator:

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file_obj = open(self.name, self.mode)
        return self.file_obj

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file_obj:
            yield line
        else:
            raise StopIteration

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


if __name__ == '__main__':
    with FileIterator('test.txt', 'r') as file:
        for line in file:
            print(line, end='')