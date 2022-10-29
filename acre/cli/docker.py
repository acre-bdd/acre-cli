import os
import uuid

from acre.cli import venv


class Docker:
    def __init__(self, image="base"):
        self.image = image

    def build(self, update=False):
        update = _get_update(update)
        venv.run(f"docker build {update} -t acre-{self.image} {_get_image(self.image)}")

    def run(self, command, cwd=".", mounts=[], interactive=False):
        portmap = "-p 9900:9900"
        it = "-it" if interactive else ""
        venv.run(f"docker run {it} {portmap} {self._mapping(mounts)} acre-{self.image}"
                 f" /usr/local/bin/shell 'cd {cwd} && {command}'")

    def _mapping(self, mounts):
        map = ""
        for mount in mounts:
            map += f'-v {mount} '
        return f"{map}-v {os.getcwd()}:/acre/testproject"


def _get_update(force=False):
    if force:
        return f"--build-arg=ACRE_UPDATE_REQUIREMENTS={uuid.uuid4()}"
    return ""


def _get_image(image):
    from acre.docker.path import get_docker_path
    return get_docker_path(image)
