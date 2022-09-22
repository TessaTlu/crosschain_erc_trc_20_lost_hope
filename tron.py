import ecdsa 
import base58
from Crypto.Hash import keccak


class Tron:
    @staticmethod
    def keccak256(data):
        hasher = keccak.new(digest_bits=256)
        hasher.update(data)
        return hasher.digest()

    @staticmethod
    def verifying_key_to_address(**kwargs):
        pub_key = kwargs["key"].to_string()
        primitive_address = b"\x41" + Tron.keccak256(pub_key)[-20:]
        # 0 (zero), O (capital o), I (capital i) and l (lower case L)
        address = base58.b58encode_check(primitive_address)
        return address
    
    @staticmethod
    def get_signing_key(raw_private):
        return ecdsa.SigningKey.from_string(raw_private, curve=ecdsa.SECP256k1)

    @staticmethod
    def generate_wallet():
        pass

    @staticmethod
    def generate_addres_from_private_string(private_key: str) -> str:
        raw = bytearray.fromhex(private_key)
        key = Tron.get_signing_key(raw_private=raw)
        tron_address = Tron.verifying_key_to_address(key=key.get_verifying_key()).decode()
        return tron_address
