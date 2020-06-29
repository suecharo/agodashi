#!/usr/bin/env python3
# coding: utf-8
from flask import Blueprint, Response, jsonify

from dashi.const import GET_STATUS_CODE
from dashi.type import AllInformation, Parameters, ServiceInfo, Type, Version

app_bp = Blueprint("dashi", __name__)


@app_bp.route("/service-info", methods=["GET"])
def get_service_info() -> Response:
    """
    Response to the name and version of workflow engines to be used inside the
    API Service. Also, it may be possible to extract the type, version and
    parameters of a workflow without using workflow engines. Therefore,
    workflow types and versions supported by this service are also responded
    to. The logic for determining workflow type and version is completely
    implementation-dependent.
    """
    res_body: ServiceInfo = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/all", methods=["GET"])
def get_all() -> Response:
    """
    This endpoint is used to extract all information. The parameter should be
    used one of wf_url, wf_content or wf_file.
    """
    res_body: AllInformation = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/type", methods=["GET"])
def get_type() -> Response:
    """
    This endpoint is used to extract workflow type. The parameter should be
    used one of wf_url, wf_content or wf_file.
    """
    res_body: Type = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/version", methods=["GET"])
def get_version() -> Response:
    """
    This endpoint is used to extract workflow version. The parameter should be
    used one of wf_url, wf_content or wf_file.
    """
    res_body: Version = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/parameters", methods=["GET"])
def get_parameters() -> Response:
    """
    This endpoint is used to extract workflow parameters. The parameter should
    be used one of wf_url, wf_content or wf_file.
    """
    res_body: Parameters = {}
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response
