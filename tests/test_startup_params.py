#!/usr/bin/env python3
# coding: utf-8
from argparse import Namespace
from typing import Dict, Union

from _pytest.monkeypatch import MonkeyPatch
from flask import Flask
from flask.testing import FlaskClient
from flask.wrappers import Response

from agodashi.app import create_app, handle_default_params, parse_args
from agodashi.const import DEFAULT_HOST, DEFAULT_PORT


def test_default_params(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)

    assert params["host"] == DEFAULT_HOST
    assert params["port"] == DEFAULT_PORT
    assert params["debug"] is False


def test_env_vars(delete_env_vars: None, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("AGODASHI_HOST", "127.0.0.1")
    monkeypatch.setenv("AGODASHI_PORT", "8888")
    monkeypatch.setenv("AGODASHI_DEBUG", "True")
    monkeypatch.setenv("AGODASHI_CROS", "test_cros")

    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    client: FlaskClient[Response] = app.test_client()
    res: Response = client.get("/service-info")

    assert params["host"] == "127.0.0.1"
    assert params["port"] == 8888
    assert params["debug"] is True

    for header in res.headers:
        if header[0] == "Access-Control-Allow-Origin":
            assert header[1] == "test_cros"


def test_parse_args(delete_env_vars: None) -> None:
    args: Namespace = \
        parse_args(["--host", "127.0.0.1",
                    "--port", "8888",
                    "--debug",
                    ])
    params: Dict[str, Union[str, int]] = handle_default_params(args)

    assert params["host"] == "127.0.0.1"
    assert params["port"] == 8888
    assert params["debug"] is True
