#!/usr/bin/env python3
# coding: utf-8
from argparse import Namespace
from typing import Dict, Union

from flask import Flask
from flask.testing import FlaskClient
from flask.wrappers import Response

from agodashi.app import create_app, handle_default_params, parse_args
from agodashi.type import ErrorResponse, Type

from .resource_list import CWL_WF, CWL_WF_PACKED, CWL_WF_REMOTE


def test_wf(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    app.debug = params["debug"]  # type: ignore
    app.testing = True
    client: FlaskClient[Response] = app.test_client()
    with CWL_WF.open(mode="r") as f:
        wf_content: str = f.read()
    response: Response = \
        client.post("/inspect-workflow/parameters",
                    data={"wf_content": wf_content},
                    content_type="multipart/form-data")
    res_data: ErrorResponse = response.get_json()

    print(response)
    print(res_data)

    assert response.status_code == 400
    assert "cwltool ended with status 1" in res_data["msg"]


def test_wf_remote(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    app.debug = params["debug"]  # type: ignore
    app.testing = True
    client: FlaskClient[Response] = app.test_client()
    with CWL_WF_REMOTE.open(mode="r") as f:
        wf_content: str = f.read()
    response: Response = \
        client.post("/inspect-workflow/parameters",
                    data={"wf_content": wf_content},
                    content_type="multipart/form-data")
    res_data: Type = response.get_json()

    print(response)
    print(res_data)

    assert response.status_code == 200
    assert "wf_params" in res_data


def test_wf_packed(delete_env_vars: None) -> None:
    args: Namespace = parse_args([])
    params: Dict[str, Union[str, int]] = handle_default_params(args)
    app: Flask = create_app(params)
    app.debug = params["debug"]  # type: ignore
    app.testing = True
    client: FlaskClient[Response] = app.test_client()
    with CWL_WF_PACKED.open(mode="r") as f:
        wf_content: str = f.read()
    response: Response = \
        client.post("/inspect-workflow/parameters",
                    data={"wf_content": wf_content},
                    content_type="multipart/form-data")
    res_data: Type = response.get_json()

    print(response)
    print(res_data)

    assert response.status_code == 200
    assert "wf_params" in res_data
