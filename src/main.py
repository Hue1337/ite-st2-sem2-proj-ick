import argparse
import os
import yaml

from modules.crypto import operations
from modules.crypto.safe import Safe
from modules.crypto.key import Key
from modules.config.config import Config
from modules.crypto.key_manager import KeyManager

from colorama import Fore, Style

# For development purpose currently working with 2 global keys.

DEV_KEK_PATH = 'data/kek.key'
DEV_DEK_PATH = 'data/dek.key'

def run(args):
    # key_manager = KeyManager(DEV_KEK_PATH, DEV_DEK_PATH)

    with open('data/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
        f.close()

    if args.generate_kek:
        if not os.path.exists(DEV_KEK_PATH):
            with open(DEV_KEK_PATH, 'wb') as f:
                f.write(Key.gen_key())
                f.close()
        else:
            print(Fore.YELLOW, "[i] KEK already exists...", Style.RESET_ALL)
    # else:
    #     if os.path.exists(DEV_KEK_PATH):
    #         key_manager.load_kek()


    if args.generate_dek:
        if not os.path.exists(DEV_DEK_PATH):
            with open(DEV_DEK_PATH, 'wb') as f:
                f.write(Key.gen_key())
                f.close()
        else:
            print(Fore.YELLOW, "[i] DEK already exists...", Style.RESET_ALL)
    # else:
    #     if os.path.exists(DEV_DEK_PATH):
    #         key_manager.load_dek()

    # print(key_manager)

    safes = []

    for s in config.safe_paths:
        safes.append(Safe(s, DEV_KEK_PATH, DEV_DEK_PATH))

    safes[0].list_files(safes[0].path)

    # print(safes[0])

    if args.encrypt:
        safes[0].encrypt_safe()

    if args.decrypt:
        safes[0].decrypt_safe()

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(prog="ICK - Projekt")
    argument_parser.add_argument("--generate-kek", '-gk', action='store_true', required = False, help='Generate KEK.')
    argument_parser.add_argument("--generate-dek", '-gd', action='store_true', required = False, help='Generate DEK.')

    argument_parser.add_argument("--encrypt", "-e", action="store_true", required=False, help='Encrypt')
    argument_parser.add_argument("--decrypt", "-d", action="store_true", required=False, help='Decrypt')

    args = argument_parser.parse_args()

    run(args)
