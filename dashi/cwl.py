#!/usr/bin/env python3
# coding: utf-8
from typing import List, cast

from cwltool.update import ALLUPDATES
from cwltool.utils import versionstring

from dashi.type import SupportedLanguage


def get_cwltool_version() -> str:
    version: str = cast(str, versionstring().split(" ")[1])
    return version


def get_cwltool_supported_languages() -> List[SupportedLanguage]:
    return [{
        "language_name": "CWL",
        "language_versions": sorted(ALLUPDATES)
    }]
