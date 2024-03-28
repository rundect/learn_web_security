import hashlib


message = 'message'
print(hash(message))
print(hash('same message'))
print(hash('same message'))
print(bin(hash('a')))
print(bin(hash('b')))
print(bin(hash(0)))
print(bin(hash(1)))


print(sorted(hashlib.algorithms_guaranteed))

named = hashlib.sha256()
generic = hashlib.new('sha256')
print(named)
print(generic)
