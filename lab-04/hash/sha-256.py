import hashlib

def caculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

data_to_hash = input("Nhap du lieu de hash bang SHA-256: ")
hash_value = caculate_sha256_hash(data_to_hash)
print("Gia tri cua hash SHA-256 la:", hash_value)