from abc import ABC, abstractmethod


class InvalidOpetationError(Exception):
    pass

# Base Class


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

    @abstractmethod  # does not get implemented but is used to tell other classes that they require a read() method
    def read(self):
        pass

# Children


class FileStream(Stream):
    def read(self):
        print("Reading data from File")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from Network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from Memory")


def read(streams):
    for stream in streams:
        stream.read()

    # stream0 = Stream() #You should not be able to create a Stream object, only a FileStream, MemoryStream and NetworkStream AND you will not be able to create these if they don't have a read(method)
    # stream0.open()
    # stream0.open()
# stream1 = FileStream()
# stream1.read()

# stream2 = MemoryStream()
# stream2.read()


# Example of polymorphism would be to loop through a list of streams (different Classes),
# and tell them to use their version of the read() method
# They would all be done at the same time BUT print out something different because they're performing the function of their version of the read method
stream1 = FileStream()
stream2 = MemoryStream()
stream3 = NetworkStream()

read([stream1, stream2, stream3])
