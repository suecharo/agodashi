#!/usr/bin/env python3
# coding: utf-8
from pathlib import Path

RESOURCE_DIR: Path = Path(__file__).parent.joinpath("resources").resolve()
RESOURCE_DIR_URL: str = "https://raw.githubusercontent.com/suecharo/" +\
    "dashi/master/tests/resources/"

CWL_DIR: Path = RESOURCE_DIR.joinpath("cwl")
CWL_DIR_URL: str = RESOURCE_DIR_URL + "cwl/"

CWL_WF: Path = CWL_DIR.joinpath("trimming_and_qc.cwl")
CWL_WF_REMOTE: Path = CWL_DIR.joinpath("trimming_and_qc_remote.cwl")
CWL_WF_PACKED: Path = CWL_DIR.joinpath("trimming_and_qc_packed.cwl")

CWL_WF_URL: str = CWL_DIR_URL + "trimming_and_qc.cwl"
CWL_WF_REMOTE_URL: str = CWL_DIR_URL + "trimming_and_qc_remote.cwl"
CWL_WF_PACKED_URL: str = CWL_DIR_URL + "trimming_and_qc_packed.cwl"
