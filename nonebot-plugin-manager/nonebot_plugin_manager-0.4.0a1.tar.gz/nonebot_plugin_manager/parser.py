from nonebot.rule import ArgumentParser

from .handle import *

npm_parser = ArgumentParser("npm")

npm_subparsers = npm_parser.add_subparsers()

list_parser = npm_subparsers.add_parser("list", help="show plugin list")
list_group = list_parser.add_mutually_exclusive_group()
list_group.add_argument("-s", "--store", action="store_true")
list_group.add_argument("-gl", "--globally", action="store_true")
list_group.add_argument("-u", "--user", action="store", type=int)
list_group.add_argument("-g", "--group", action="store", type=int)
list_group.add_argument("-d", "--default", action="store_true")
list_parser.set_defaults(handle=handle_list)

block_parser = npm_subparsers.add_parser("block", help="block plugin")
block_parser.add_argument("plugins", nargs="*", help="plugins you want to block")
block_parser.add_argument("-a", "--all", action="store_true")
block_parser.add_argument("-r", "--reverse", action="store_true")
block_group = block_parser.add_mutually_exclusive_group()
block_group.add_argument("-gl", "--globally", action="store_true")
block_group.add_argument("-u", "--user", action="store", type=int)
block_group.add_argument("-g", "--group", action="store", type=int)
block_group.add_argument("-d", "--default", action="store_true")
block_parser.set_defaults(handle=handle_block)

unblock_parser = npm_subparsers.add_parser("unblock", help="unblock plugin")
unblock_parser.add_argument("plugins", nargs="*", help="plugins you want to unblock")
unblock_parser.add_argument("-a", "--all", action="store_true")
unblock_parser.add_argument("-r", "--reverse", action="store_true")
unblock_group = unblock_parser.add_mutually_exclusive_group()
unblock_group.add_argument("-gl", "--globally", action="store_true")
unblock_group.add_argument("-u", "--user", action="store", type=int)
unblock_group.add_argument("-g", "--group", action="store", type=int)
unblock_group.add_argument("-d", "--default", action="store_true")
unblock_parser.set_defaults(handle=handle_unblock)

info_parser = npm_subparsers.add_parser("info", help="show plugin info")
info_parser.add_argument("plugin", help="plugins you want to know about")
info_parser.set_defaults(handle=handle_info)

install_parser = npm_subparsers.add_parser("install", help="install plugin")
install_parser.add_argument("plugins", nargs="*", help="plugins you want to install")
install_parser.add_argument("-i", "--index", action="store", help="point to a mirror")
install_parser.set_defaults(handle=handle_install)

uninstall_parser = npm_subparsers.add_parser("uninstall", help="uninstall plugin")
uninstall_parser.add_argument(
    "plugins", nargs="*", help="plugins you want to uninstall"
)
uninstall_parser.set_defaults(handle=handle_uninstall)
