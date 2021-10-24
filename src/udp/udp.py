from bitarray import bitarray
from bitarray.util import int2ba

class Udp:
    """
    UDP Segment.

    source_port: 16 bits
    destination_port: 16 bits
    length: 16 bits
    checksum: 16 bits
    data: maximum of 65,507 bytes
    """

    def __init__(self, source_port: int, destination_port: int, data: str):
        self.source_port = source_port
        self.destination_port = destination_port
        self.checksum = 0
        self.length = 0
        self.data_max_length = 65507
        self.is_valid = True
        self.set_data(data)

    def set_data(self, data: str):
        """ Sets data of Udp segment. """
        if data is None:
            raise TypeError(f"Data must not be None!")
        elif type(data) != str:
            raise TypeError(f"Data must be of type str!")
        elif len(data) > self.data_max_length:
            raise ValueError(f"Data must not be more than {self.data_max_length} characters!")
        self.data = data

    def get_length(self) -> int:
        """ Returns size of UDP segment in bytes. """
        return 64 + len(self.data)

    def get_checksum(self) -> int:
        """ Returns checksum of UDP segment. """
        return 0

    def is_checksum_valid(self) -> bool:
        return self.checksum == self.get_checksum()

    def get_bitarray(self) -> bitarray:
        """ Returns bitarray of UDP segment. """
        arr = bitarray()
        arr += int2ba(self.source_port, 16)
        arr += int2ba(self.destination_port, 16)
        arr += int2ba(self.get_length(), 16)
        arr += int2ba(self.get_checksum(), 16)

        # Convert data from string to byte array and then to bit array
        data_ba = bitarray()
        data_ba.frombytes(self.data.encode('utf-8'))
        arr += data_ba

        return arr

    def serialize(self) -> bytearray:
        """ Returns byte array of UDP segment. """
        s = bytearray()
        header = [self.source_port, self.destination_port, self.get_length(), self.get_checksum()]
        for h in header:
            s += h.to_bytes(2, 'big')
        s += bytearray(self.data.encode('utf-8'))
        return s

    def deserialize(self, b = bytearray):
        """ Update member variables from given bytearray. """
        self.source_port = b[0:2]
        self.destination_port = b[2:4]
        self.length = b[4:6]
        self.checksum = b[6:8] # need to validate if checksum is correct
        self.data = b[8:]
        self.is_valid = self.is_checksum_valid()

