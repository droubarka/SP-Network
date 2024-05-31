# /modules/functions.py

def bytes_to_bits(bytes: bytes) -> str:
	"""
	Convert a sequence of bytes to a string of bits.

	Args:
		bytes: A sequence of bytes to be converted to bits.

	Returns:
		A string of bits, where each byte is represented as 8 binary digits.
	"""
	return ''.join(format(byte, '08b') for byte in bytes)

def bits_to_bytes(bits: str) -> bytes:
	"""
	Convert a string representing bits to bytes.

	Args:
		bits: A string representing bits.

	Returns:
		A bytes object representing the converted bits.
	"""
	return int(bits, 2).to_bytes((len(bits) + 7) // 8, byteorder='big')
