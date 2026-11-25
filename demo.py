# New offline example of the original unsigned big-endian decoding convention.
import struct
packet = struct.pack('>4H', 0, 42, 1024, 65535)
values = [int.from_bytes(packet[i:i+2], 'big') for i in range(0, len(packet), 2)]
assert values == [0, 42, 1024, 65535]
print(values)
