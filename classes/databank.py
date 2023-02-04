import json
import os
from pathlib import Path

class DataBank():
    data = False

    def __init__(self, raw):
        if raw:
            self.data = json.loads(raw)

    def get(self, key, default=False):
        return self.data[key] if (self.data and key and self.data[key]) else default


def save(file, data, tojson=False):
    try:
        project_path = str(Path(__file__).parent.parent)
        if not os.path.exists(project_path + "/databank"):
            os.makedirs(project_path + "/databank")
        f = open(project_path + f"/databank/{file}", "w+")
        f.write(json.dumps(data, indent=4, sort_keys=True) if tojson else data)
        f.close()
        return True

    except Exception as err:
        print(f'Exception: {err}')
    return False


def load(file, isjson=False):
    try:
        project_path = str(Path(__file__).parent.parent)
        if not os.path.exists(project_path + "/databank"):
            os.makedirs(project_path + "/databank")

        if os.path.exists(project_path + "/databank"):
            f = open(project_path + f"/databank/{file}", "r")
            data = f.read()
            f.close()
            return DataBank(data) if isjson else data

    except Exception as err:
        print(f'Exception: {err}')

    return DataBank(False) if isjson else False
