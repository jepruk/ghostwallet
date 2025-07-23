import os
from eth_account import Account
from web3 import Web3
from typing import Optional

# Убедимся, что используем "небезопасный" режим
Account.enable_unaudited_hdwallet_features()

class GhostWallet:
    def __init__(self, mnemonic: Optional[str] = None):
        if mnemonic is None:
            self.mnemonic = Account.create().key.hex()  # Псевдо-entropy
            self.account = Account.create()
        else:
            self.mnemonic = mnemonic
            self.account = Account.from_mnemonic(mnemonic)

        self.address = self.account.address
        self.private_key = self.account.key

    def sign_message(self, message: str) -> str:
        signed = Account.sign_message(Web3.to_bytes(text=message), self.private_key)
        return signed.signature.hex()

    def get_address(self) -> str:
        return self.address

    def wipe(self):
        # Затираем чувствительные данные
        self.private_key = None
        self.mnemonic = None
        self.account = None
        self.address = None
