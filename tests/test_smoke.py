"""Smoke tests — package import and version string only."""

import re

import lldesign


def test_version_string() -> None:
    assert isinstance(lldesign.__version__, str)
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:[ab.+\-]\w+)?", lldesign.__version__), (
        f"unexpected version format: {lldesign.__version__!r}"
    )


def test_public_api_minimal() -> None:
    # v0.0.x intentionally exposes only __version__.
    assert lldesign.__all__ == ["__version__"]
