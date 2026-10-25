#!/usr/bin/python3

"""
Development commands for Boring Gorilla.

"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(*args: str) -> None:
    """Execute a command from the project root."""
    subprocess.run(args, cwd=ROOT, check=True)


def launch() -> None:
    """Launch the Boring Gorilla application."""
    run(sys.executable, "BoringGorilla.py")


def design() -> None:
    """Generate Python files from Qt Designer UI files."""
    ui_files = (
        "BoringGorilla_design",
        "Preferences_design",
    )

    for name in ui_files:
        source = Path("ui_design") / f"{name}.ui"
        target = ROOT / f"{name}.py"

        run("pyuic6", str(source), "-o", str(target))
        print(f"Generated: {target.name}")

    print("All design files generated successfully.")


def build() -> None:
    """Build the executable."""
    run("cxfreeze", "build")
    print("Build finished.")


def clean_build() -> None:
    """Remove build subdirectories while preserving files in build dir."""
    build_dir = ROOT / "build"

    if not build_dir.is_dir():
        return

    for path in build_dir.iterdir():
        if path.is_dir():
            shutil.rmtree(path)
            print(f"Removed directory: {path.relative_to(ROOT)}")


def clean() -> None:
    """Remove build artifacts, cache files, and MANIFEST."""
    directories = (
        ROOT / "__pycache__",
        ROOT / "BoringGorilla.egg-info",
        ROOT / "dist",
    )

    files = (ROOT / "MANIFEST",)

    for path in directories:
        if path.is_dir():
            shutil.rmtree(path)
            print(f"Removed directory: {path.relative_to(ROOT)}")

    clean_build()

    for path in files:
        if path.is_file():
            path.unlink()
            print(f"Removed file: {path.relative_to(ROOT)}")

    print("Clean finished.")


def cleanall() -> None:
    """Remove build artifacts, generated design files, and config.ini."""
    clean()

    files = (
        ROOT / "BoringGorilla_design.py",
        ROOT / "Preferences_design.py",
        ROOT / "config.ini",
    )

    for path in files:
        if path.is_file():
            path.unlink()
            print(f"Removed file: {path.relative_to(ROOT)}")

    print("Cleanall finished.")


def main() -> None:
    """Display help or execute the requested development command."""
    commands = {
        "launch": launch,
        "design": design,
        "build": build,
        "clean": clean,
        "cleanall": cleanall,
    }

    parser = argparse.ArgumentParser(
        description="Development commands for Boring Gorilla.",
        epilog="Available commands:",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
        metavar="<command>",
    )

    for name, func in commands.items():
        subparser = subparsers.add_parser(
            name,
            help=func.__doc__,
            description=func.__doc__,
        )
        subparser.set_defaults(func=func)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    args.func()


if __name__ == "__main__":
    main()
