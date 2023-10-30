"""Internal IO functions for viper."""
import json
import tomllib
from pathlib import Path
from typing import Any

import yaml


def read_config(path: Path) -> dict[str, Any]:
    """Read a config file.

    This function supports configs from JSON, TOML, and YAML files.

    Parameters
    ----------
    path : Path
       Path to the config file.

    Returns
    -------
    dict[str, Any]
        Config

    Raises
    ------
    ValueError
        Raised if the config file extension is not supported.
    """
    file_extension = path.suffix if path.suffix else path.name

    if file_extension == ".json":
        return _read_json(path)
    elif file_extension == ".toml":  # noqa: RET505
        return _read_toml(path)
    elif file_extension in [".yml", "yaml"]:
        return _read_yaml(path)

    msg = f"Config file extension {file_extension} not supported."
    raise ValueError(msg)


def _read_json(path: Path) -> dict[str, Any]:
    """Read a JSON file.

    Parameters
    ----------
    path : Path
        Path to the JSON file.

    Returns
    -------
    dict[str, Any]
        JSON file contents.
    """
    with path.open() as stream:
        return json.load(stream)


def _read_toml(path: Path) -> dict[str, Any]:
    """Read a TOML file.

    Parameters
    ----------
    path : Path
        Path to the TOML file.

    Returns
    -------
    dict[str, Any]
        TOML file contents.
    """
    with path.open() as stream:
        tomllib.load(stream)


def _read_yaml(path: Path) -> dict[str, Any]:
    """Read a YAML file.

    Parameters
    ----------
    path : Path
        Path to the YAML file.

    Returns
    -------
    dict[str, Any]
        YAML file contents.
    """
    with path.open() as stream:
        return yaml.loads(stream)