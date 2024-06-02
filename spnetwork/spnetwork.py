# /modules/spnetwork.py

import functions

def substitute(block: bytes, table: bytes, reverse: bool = False) -> bytes:
	"""
	Perform byte substitution on a block of bytes in either direction.

	Args:
		block: A block of bytes to be substituted.
		table: A bytes object representing the substitution table.
		inverse: A boolean flag to determine the direction of substitution.

	Returns:
		A block of bytes resulting from the substitution.
	"""
	if not isinstance(block, bytes):
		raise ValueError("block argument must be a bytes object")

	if not isinstance(table, bytes):
		raise ValueError("table argument must be a bytes object")

	if len(set(table)) != len(table):
		raise ValueError("Each byte in the block must have a unique substitution in the table")

	if reverse:
		substituted_block = bytes(table.index(byte) for byte in block)
	else:
		substituted_block = bytes(table[byte] for byte in block)

	return substituted_block


def permute_bits(block: bytes, table: bytes, reverse: bool = False) -> bytes:
	"""
	Perform bit permutation on a block of bytes in either direction.

	Args:
		block: A block of bytes to be permuted.
		table: A bytes object representing the permutation table.
		reverse: A boolean flag to determine the direction of permutation.

	Returns:
		A block of bytes resulting from the permutation.
	"""
	if not isinstance(block, bytes):
		raise ValueError("block argument must be a bytes object")

	if not isinstance(table, bytes):
		raise ValueError("table argument must be a bytes object")

	if len(set(table)) != len(table):
		raise ValueError("Each bit in the block must have a unique permutation in the table")

	if len(table) // 8 != len(block):
		raise ValueError("The table must be able to accommodate all bits in the block")

	block_bits = functions.bytes_to_bits(block)

	if reverse:
		permuted_block_bits = ''.join( \
			block_bits[table.index(bit)] for bit in range(len(block_bits)))
	else:
		permuted_block_bits = ''.join(block_bits[idx] for idx in table)

	permuted_block = functions.bits_to_bytes(permuted_block_bits)

	return permuted_block
