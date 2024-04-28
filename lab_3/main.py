from HybridCryptography import HybridCryptography
from functions import json_reader, parse
from constants import PATHS


if __name__ == "__main__":
    paths = json_reader(PATHS)
    crypto_system = HybridCryptography(
        paths["sym_path"], paths["private_path"], paths["public_path"]
    )
    args = parse()
    if args.generation:
        crypto_system.generate_keys(int(args.len / 8))
    elif args.encryption:
        crypto_system.encrypt(args.pth, paths["encrypted_text"])
    else:
        crypto_system.decrypt(args.cpt, paths["decrypted_text"])
