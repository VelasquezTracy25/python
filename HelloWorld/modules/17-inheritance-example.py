from abc import ABC, abstractmethod


class InvalidOpetationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOpetationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOpetationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from File")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from Network")


class MemoryStream(Stream):


    # stream0 = Stream() #You should not be able to create a Stream object, only a FileStream, MemoryStream and NetworkStream
    # stream0.open()
    # stream0.open()
stream1 = FileStream()
stream1.read()

stream2 = MemoryStream()
stream2.read()
