from electrumx.lib.coins import Bitcoin
from electrumx.lib import tx as lib_tx

class Palladium(Bitcoin):
    NAME = "Palladium"
    SHORTNAME = "PLM"
    NET = "mainnet"

    # === Prefix address ===
    P2PKH_VERBYTE = bytes([0x00])
    P2SH_VERBYTE  = bytes([0x05])
    WIF_BYTE      = bytes([0x80])

    # === bech32 prefix ===
    HRP = "plm"

    # === Genesis hash (Bitcoin mainnet) ===
    GENESIS_HASH = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"

    # === Deserializer ===
    DESERIALIZER = lib_tx.DeserializerSegWit

