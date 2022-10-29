import os

from acre.cli import venv


class Docker:
    def __init__(self, image="base"):
        self.image = image

    def build(self):
        venv.run(f"docker build -t acre-{self.image} {_get_image(self.image)}")

    def run(self, command, cwd="."):
        venv.run(f"docker run -it {self._mapping()} acre-{self.image} bash -c 'cd {cwd} && {command}'")

    def _mapping(self):
        return f"-v {os.getcwd()}:/acre/testproject"


def _get_image(image):
    from acre.docker.path import get_docker_path
    return get_docker_path(image)
