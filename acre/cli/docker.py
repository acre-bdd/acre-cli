import os

from acre.cli import venv


class Docker:
    def __init__(self, image="base"):
        self.image = image

    def build(self, update=False):
        ip = _get_image(self.image)
        ec = venv.run(f"docker build -t acre-{self.image}1 -f {ip}/Dockerfile1 {ip}")
        if ec:
            return ec
        nocache = "--no-cache" if update else ""
        return venv.run(f"docker build {nocache} -t acre-{self.image} -f {ip}/Dockerfile2 {ip}")

    def run(self, command, cwd=".", mounts=[], interactive=False):
        portmap = "-p 9900:9900"
        it = "-it" if interactive else ""
        return venv.run(f"docker run {it} {portmap} {self._mapping(mounts)} acre-{self.image}"
                        f" /usr/local/bin/shell 'cd {cwd} && {command}'")

    def _mapping(self, mounts):
        map = ""
        for mount in mounts:
            (source, target) = mount.split(":")
            map += f'-v {os.path.abspath(source)}:{target} '
        return f"{map}-v {os.getcwd()}:/acre/testproject"


def _get_image(image):
    from acre.docker.path import get_docker_path
    return get_docker_path(image)
