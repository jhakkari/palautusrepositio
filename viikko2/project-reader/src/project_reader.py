from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        toml_dict = tomli.loads(content)

        print(toml_dict["tool"])
        name = toml_dict["tool"]
        description = ""
        dependencies = ""
        dev_dependencies = ""

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, "", [], [])
