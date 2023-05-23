"""
GHEmoji functions: install, uninstall and commit
"""

import os
import re
import stat
import sys

from yaml import Loader, YAMLError, load

EMOJI = {
    "feat:": "✨",
    "init:": "🎉",
    "fix:": "🚑️",
    "style:": "💄",
    "revert:": "⏪️",
    "pref:": "⚡️",
    "refactor:": "♻️",
    "test:": "✅",
    "ci:": "👷",
    "typo:": "✏️",
    "docs:": "📝",
}


def install(path: str):
    """
    Install GHEmoji to prepare-commit-msg
    """
    hooks_dir = os.path.join(path, ".git", "hooks")
    if not os.path.isdir(hooks_dir):
        sys.stderr.writelines(
            "cannot find prepare-commit-msg, check if directory is git repo"
        )
        return
    hook_file = os.path.join(hooks_dir, "prepare-commit-msg")
    if os.path.exists(hook_file):
        uninstall(path)
    with open(hook_file, "a", encoding="utf-8") as file:
        file.write(f'\nghemoji "{path}" -c -m $1\n')
    os.chmod(
        hook_file,
        stat.S_IRUSR
        | stat.S_IWUSR
        | stat.S_IXUSR
        | stat.S_IROTH
        | stat.S_IXOTH
        | stat.S_IRGRP
        | stat.S_IWGRP
        | stat.S_IXGRP,
    )


def uninstall(path: str):
    """
    Uninstall GHEmoji from prepare-commit-msg
    """
    hook_path = os.path.join(path, ".git", "hooks", "prepare-commit-msg")
    if not os.path.isfile(hook_path):
        sys.stderr.writelines(
            "cannot find prepare-commit-msg, check if directory is git repo"
        )
        return
    with open(hook_path, "r+", encoding="utf-8") as file:
        content = file.read()
        content = re.sub(r"ghemoji.*$", "", content)
        file.truncate(0)
        file.seek(0)
        file.write(content)


def commit(directory: str, path: str):
    """
    Process commit message after user commit
    """
    config_path = os.path.join(directory, "ghemoji.yaml")
    emoji = EMOJI.copy()
    if os.path.isfile(config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            try:
                config = load(file, Loader)
                for _emoji in config["replace"]:
                    emoji.update(_emoji)
            except (TypeError, YAMLError):
                sys.stderr.write("ghemoji.yaml may misconfiguration")
    with open(path, "r+", encoding="utf-8") as file:
        content = file.read()
        for key, value in emoji.items():
            content = content.replace(key, value)
        file.truncate(0)
        file.seek(0)
        file.write(content)
