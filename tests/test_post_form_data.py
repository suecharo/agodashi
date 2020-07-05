#!/usr/bin/env python3
# coding: utf-8
from argparse import Namespace
from typing import Dict, Union

from flask import Flask
from flask.testing import FlaskClient
from flask.wrappers import Response

from agodashi.app import create_app, handle_default_params, parse_args
from agodashi.type import AllInformation

from .resource_list import CWL_WF_PACKED, CWL_WF_PACKED_URL


def test_post_wf_url(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    app.debug = params["debug"]  # type: ignore
    app.testing = True
    client: FlaskClient[Response] = app.test_client()
    response: Response = \
        client.post("/inspect-workflow", data={"wf_url": CWL_WF_PACKED_URL},
                    content_type="multipart/form-data")
    res_data: AllInformation = response.get_json()

    print(response)
    print(res_data)

    assert response.status_code == 200


def test_post_wf_url_failed(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    app.debug = params["debug"]  # type: ignore
    app.testing = True
    client: FlaskClient[Response] = app.test_client()
    response: Response = \
        client.post("/inspect-workflow",
                    data={"wf_url": "http://localhost:1234"},
                    content_type="multipart/form-data")
    res_data: AllInformation = response.get_json()

    print(response)
    print(res_data)

    assert response.status_code == 400


def test_post_wf_content(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    app.debug = params["debug"]  # type: ignore
    app.testing = True
    client: FlaskClient[Response] = app.test_client()
    with CWL_WF_PACKED.open(mode="r") as f:
        wf_content: str = f.read()
    response: Response = \
        client.post("/inspect-workflow", data={"wf_content": wf_content},
                    content_type="multipart/form-data")
    res_data: AllInformation = response.get_json()

    print(response)
    print(res_data)

    assert response.status_code == 200


def test_post_wf_file(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    app.debug = params["debug"]  # type: ignore
    app.testing = True
    client: FlaskClient[Response] = app.test_client()
    response: Response = \
        client.post("/inspect-workflow",
                    data={"wf_file": (CWL_WF_PACKED.open(
                        mode="rb"), CWL_WF_PACKED.name)},
                    content_type="multipart/form-data")
    res_data: AllInformation = response.get_json()

    print(response)
    print(res_data)

    assert response.status_code == 200
