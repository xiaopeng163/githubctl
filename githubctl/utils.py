import csv
from typing import List
import sys
import json

from rich import print_json

from options import OutputOption


def print_beauty(list_of_dict: List[dict], output: OutputOption):
    if output == OutputOption.csv:
        fieldnames = list_of_dict[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(list_of_dict)

    elif output == OutputOption.json:
        print_json(json.dumps(list_of_dict))
