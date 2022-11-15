import subprocess
import os

from acre.cli import venv

dockerbin = "docker"


class Docker:
    def __init__(self, image="base", name=None):
        self.image = image
        self.name = name

    def build(self, update=False):
        ip = _get_image(self.image)
        ec = venv.run(f"docker build -t acre-{self.image}1 -f {ip}/Dockerfile1 {ip}")
        if ec:
            return ec
        nocache = "--no-cache" if update else ""
        return venv.run(f"docker build {nocache} -t acre-{self.image} -f {ip}/Dockerfile2 {ip}")

    def run(self, command, cwd=".", mounts=[], interactive=False, autoremove=True):
        portmap = "-p 9900:9900"
        it = "-it" if interactive else ""
        name = f"--name {self.name}" if self.name else ""
        if autoremove:
            self.remove()
        return venv.run(f"docker run {name} {it} {portmap} {self._mapping(mounts)} acre-{self.image}"
                        f" /usr/local/bin/shell 'cd {cwd} && {command}'")

    def remove(self):
        """ removes a container, if it exists """
        if self.name and self.exists():
            return subprocess.run(f'{dockerbin} rm {self.name}', shell=True, stdout=subprocess.PIPE).returncode

    def exists(self):
        """ returns true if this container already exists """
        return subprocess.run(f'{dockerbin} container ls --all | grep {self.name}',
                              shell=True, stdout=subprocess.PIPE).returncode == 0

    def _mapping(self, mounts):
        map = ""
        for mount in mounts:
            (source, target) = mount.split(":")
            map += f'-v {os.path.abspath(source)}:{target} '
        return f"{map}-v {os.getcwd()}:/acre/testproject"


def _get_image(image):
    from acre.docker.path import get_docker_path
    return get_docker_path(image)
