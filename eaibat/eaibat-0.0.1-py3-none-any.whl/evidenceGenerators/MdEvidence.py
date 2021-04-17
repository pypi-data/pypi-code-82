# -*- Product under GNU GPL v3 -*-
# -*- Author: E.Aivayan -*-
import os
import json

from logging import getLogger
from pathlib import Path
from shutil import move
from typing import TextIO
from xml.dom import minidom
from requests.models import Response

log = getLogger(__name__)


def generate_md_evidence(evidence_folder, evidence_filename, history):
    with open(f"{evidence_folder}/{evidence_filename}", "w", encoding="utf-8") as evidence:
        evidence.write(f"# {evidence_filename}\n")
        external_file = None
        for step, events in history.items():
            evidence.write(f"## {step[0]}: {step[1]}\n")
            for event in events:
                if isinstance(event, str):
                    evidence.write(f"{event}\n")
                elif isinstance(event, tuple):
                    if external_file is None:
                        external_file = Path(f"{evidence_folder}/"
                                             f"{evidence_filename.split('.')[0]}_file")
                        os.mkdir(external_file)

                    _file_to_evidence(evidence, event, external_file)
                elif isinstance(event, dict):
                    _dict_to_evidence(evidence, event)
                else:
                    _response_to_evidence(evidence, event)


def _file_to_evidence(file_stream: TextIO, event: tuple, destination_folder: Path):
    file_path = Path(f"{destination_folder.parent}/{event[0]}")
    if file_path.exists() and file_path.is_file():
        move(file_path, f"{destination_folder}/{file_path.name}")
        file_stream.write(f"{event[1]} file is located "
                          f"at {destination_folder}/{file_path.name}")
    else:
        file_stream.write(f"{event[1]} file is located at {event[0]} (but not found)")


def _dict_to_evidence(file_stream: TextIO, event: dict):
    for key, value in event.items():
        file_stream.write(f"### {key}\n")
        if isinstance(value, Response):
            _response_to_evidence(file_stream, value, sub_level=True)
        else:
            file_stream.write(f"{value}\n\n")


def _response_to_evidence(file_stream: TextIO,
                          event: Response,
                          sub_level: bool = False):

    section_number = "#### " if sub_level else "### "

    file_stream.write(f"{section_number}URL\n"
                      f"{event.url}\n"
                      f"{section_number}VERB\n"
                      f"{event.request.method}\n"
                      f"{section_number}Request headers\n"
                      f"{event.request.headers}\n")
    if event.request.body is not None:
        file_stream.write(f"{section_number}Body\n"
                          f"{event.request.body}\n")
    file_stream.write(f"{section_number}Response status code\n"
                      f"{event.status_code}\n")
    file_stream.write(f"{section_number}Response headers\n"
                      f"{event.headers}\n")
    try:
        response = json.dumps(event.json(), indent="  ")
        file_stream.write(f"{section_number} Response content\n\n"
                          f"~~~json\n{response}\n~~~\n\n")
        return
    except Exception as exception:
        log.info(f"Response is not a json.\n Get {exception.args[0]}")

    try:
        response = minidom.parseString(event.text).toprettyxml(indent="   ")
        file_stream.write(f"{section_number} Response content\n\n"
                          f"~~~xml\n{response}\n~~~\n\n")
        return
    except Exception as exception:
        log.info(f"Response is not a XML.\n Get {exception.args[0]}")

    file_stream.write(f"{section_number} Response content\n"
                      f"{event.text}\n")
