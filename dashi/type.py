#!/usr/bin/env python3
# coding: utf-8
from sys import version_info

if version_info.minor < 8:
    from typing_extensions import TypedDict
else:
    from typing import TypedDict  # type: ignore


class ErrorResponse(TypedDict):
    """
    An object that can optionally include information about the error.
    msg:
        A detailed error message.
    status_code:
        The integer representing the HTTP status code (e.g. 200, 404).
    """
    msg: str
    status_code: int
