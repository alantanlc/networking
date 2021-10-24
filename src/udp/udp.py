from bitarray import bitarray

class Udp:
    """
    UDP Segment.

    source_port: 16 bits, optional
    destination_port: 16 bits
    length: 16 bits
    checksum: 16 bits, optional
    """

    def __init__(self, source_port: int, destination_port: int, data: str):
        self.source_port = source_port
        self.destination_port = destination_port
        self.data = None
        self.length = 0

    def get_length() -> int:
        return 0

    def get_checksum():
        return 0

    def serialize() -> bitarray:
        arr = bitarray()
        return arr

