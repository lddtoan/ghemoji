"""
Test GHEMoji command line interface
"""

import os
import tempfile
from pathlib import Path

from ghemoji import cli


def test_main_install():
    """
    Test install command
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        Path(os.path.join(temp_dir, ".git", "hooks")).mkdir(parents=True, exist_ok=True)
        cli.main([temp_dir, "-i"])
        assert os.path.isfile(
            os.path.join(temp_dir, ".git", "hooks", "prepare-commit-msg")
        )


def test_main_uninstall():
    """
    Test uninstall command
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        Path(os.path.join(temp_dir, ".git", "hooks")).mkdir(parents=True, exist_ok=True)
        cli.main([temp_dir, "-i"])
        cli.main([temp_dir, "-u"])
        with open(
            os.path.join(temp_dir, ".git", "hooks", "prepare-commit-msg"),
            "r",
            encoding="utf-8",
        ) as file:
            assert "ghemoji" not in file.read()


def test_main_commit_without_config():
    """
    Test user commit without custom config
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        message = os.path.join(temp_dir, "COMMIT_EDITMSG")
        with open(message, "w", encoding="utf-8") as file:
            file.write("init: repo")
        cli.main([temp_dir, "-c", "-m", message])
        with open(message, "r", encoding="utf-8") as file:
            assert "🎉 repo" in file.read()


def test_main_commit_with_correct_config():
    """
    Test user commit with correct config
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        message = os.path.join(temp_dir, "COMMIT_EDITMSG")
        with open(message, "w", encoding="utf-8") as file:
            file.write("init: repo")
        cli.main(
            [
                os.path.join(Path(__file__).parent, "config", "correct"),
                "-c",
                "-m",
                message,
            ]
        )
        with open(message, "r", encoding="utf-8") as file:
            assert "👌 repo" in file.read()


def test_main_commit_with_incorrect_config():
    """
    Test user commit with incorrect config
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        message = os.path.join(temp_dir, "COMMIT_EDITMSG")
        with open(message, "w", encoding="utf-8") as file:
            file.write("init: repo")
        cli.main(
            [
                os.path.join(Path(__file__).parent, "config", "incorrect"),
                "-c",
                "-m",
                message,
            ]
        )
        with open(message, "r", encoding="utf-8") as file:
            assert "🎉 repo" in file.read()
