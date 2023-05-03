from contextlib import contextmanager

# class OpenFile():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()

@contextmanager
def OpenFile(file,mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with OpenFile('textfile.txt','a') as f:
    f.write('Some more text\n')