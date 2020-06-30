#!/usr/bin/env python3
# coding: utf-8
import itertools
from typing import List, Set

from dashi.cwl import get_cwltool_supported_languages, get_cwltool_version
from dashi.type import ServiceInfo, SupportedLanguage, WorkflowEngine


def generate_service_info() -> ServiceInfo:
    workflow_engines: List[WorkflowEngine] = []
    workflow_engines.append({
        "engine_name": "cwltool",
        "engine_version": get_cwltool_version(),
        "supported_languages": get_cwltool_supported_languages()
    })

    service_info: ServiceInfo = {
        "workflow_engines": workflow_engines,
        "supported_languages": generate_all_supported_languages()
    }

    return service_info


def generate_all_supported_languages() -> List[SupportedLanguage]:
    supported_languages: List[SupportedLanguage] = \
        [*get_cwltool_supported_languages()]
    unique_language_names: Set[str] = \
        {lang["language_name"] for lang in supported_languages}
    all_supported_languages: List[SupportedLanguage] = []
    for lang_name in unique_language_names:
        all_supported_languages.append({
            "language_name": lang_name,
            "language_versions": sorted(set(itertools.chain.from_iterable(
                [lang["language_versions"] for lang in supported_languages
                 if lang["language_name"] == lang_name]
            )))
        })

    return all_supported_languages
