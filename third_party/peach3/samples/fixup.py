
#
# Example Python fixup for Peach 3
#
# Authors:
#	Michael Eddingtion
#

# -- Example returning a string ---------------

class FixupReturningString:
	def __init__(self, parent):
		self._parent = parent
	
	def fixup(self, element):
		return "Hello from FixupReturningString"

# --------------------------------------------

# -- Example returning a byte array ----------

from System import Array
import System

class FixupReturningByteArray:
	def __init__(self, parent):
		self._parent = parent
	
	def fixup(self, element):
		byteArray = bytearray(b"FixupReturningByteArray")
		return Array[System.Byte](byteArray)

# --------------------------------------------
# end
