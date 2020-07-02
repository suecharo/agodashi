#!/usr/bin/env python3
# coding: utf-8
from argparse import Namespace
from typing import Dict, Union

from flask import Flask
from flask.testing import FlaskClient
from flask.wrappers import Response

from agodashi.app import create_app, handle_default_params, parse_args
from agodashi.type import ServiceInfo


def test_get_service_info(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    app.debug = params["debug"]  # type: ignore
    app.testing = True
    client: FlaskClient[Response] = app.test_client()
    response: Response = client.get("/service-info")
    res_data: ServiceInfo = response.get_json()

    print(response)
    print(res_data)

    assert response.status_code == 200
    assert "supported_languages" in res_data
    assert "workflow_engines" in res_data
