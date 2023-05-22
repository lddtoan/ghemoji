"""
Handle command line arguments
"""

import argparse
import pathlib

from ghemoji import hook


def main(sys_args):
    """
    Main function handle command line arguments
    """
    parser = argparse.ArgumentParser(description="😄 git hook emoji")
    parser.add_argument(
        "-i", "--install", action="store_true", help="👌 add git hook emoji to git repo"
    )
    parser.add_argument(
        "-u",
        "--uninstall",
        action="store_true",
        help="💀 remove git hook emoji from git repo",
    )
    parser.add_argument(
        "-c",
        "--commit",
        action="store_true",
        help="🤖 this option is used by hook, don't use it manually",
    )
    parser.add_argument(
        "-m", "--message", help="🤖 this option is used by hook, don't use it manually"
    )
    parser.add_argument("directory", help="📂 git repo directory", type=pathlib.Path)

    args = parser.parse_args(sys_args)

    if args.install:
        hook.install(args.directory)
    if args.uninstall:
        hook.uninstall(args.directory)
    if args.commit:
        hook.commit(args.directory, args.message)
