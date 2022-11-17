import time
import subprocess
import os

from acre.cli import venv

dockerbin = "docker"


class DockerException(Exception):
    def __init__(self, message, exitcode):
        super().__init__(message)
        self.exitcode = exitcode

    def __str__(self):
        ret = super().__str__()
        ret += f", exitcode: {self.exitcode}"
        return ret


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
        args = f"--build-arg USER_ID={os.geteuid()}"
        ec = venv.run(f"docker build {nocache} {args} -t acre-{self.image} -f {ip}/Dockerfile2 {ip}")
        if ec != 0:
            raise DockerException("docker build failed", ec)

    def run(self, command="", mounts=[], autoremove=True):
        portmap = "-p 9900:9900"
        name = f"--name {self.name}" if self.name else ""
        if autoremove:
            self.remove()
        detach = "" if command else "--detach"
        ec = venv.run(f"docker run {detach} {name} {portmap} {self._mapping(mounts)} acre-{self.image} {command}")
        if ec == 0:
            time.sleep(10)
            return
        raise DockerException("docker run failed", ec)

    def exec(self, command, cwd=".", interactive=False):
        it = "-it" if interactive else ""
        cmd = f"{command}"
        return venv.run(f"docker exec --workdir {cwd} {it} {self.name} /bin/bash -c '{cmd}'")

    def remove(self):
        """ removes a container, if it exists """
        if self.name and self.exists():
            return subprocess.run(f'{dockerbin} rm {self.name}', shell=True, stdout=subprocess.PIPE).returncode

    def stop(self):
        """stops the running container"""
        return subprocess.run(f'{dockerbin} stop {self.name}',
                              shell=True, stdout=subprocess.PIPE).returncode == 0

    def is_running(self):
        """ returns true if this container is running """
        return subprocess.run(f'{dockerbin} container ls -f name={self.name} | grep {self.name}',
                              shell=True, stdout=subprocess.PIPE).returncode == 0

    def exists(self):
        """ returns true if this container already exists """
        return subprocess.run(f'{dockerbin} container ls --all -f name={self.name} | grep {self.name}',
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
