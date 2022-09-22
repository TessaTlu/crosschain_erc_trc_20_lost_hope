from ethereum import EthereumWallet
from tron import Tron

private_key = input("Enter the private key: ")

ethereum_address = EthereumWallet.generate_address(private_key=private_key)
ethereum_address = EthereumWallet.checksum_address(address=ethereum_address)
print("Your address in ERC20 network", ethereum_address)

tron_address = Tron.generate_addres_from_private_string(private_key=private_key)
print("Your address in TRC20 network", tron_address)
