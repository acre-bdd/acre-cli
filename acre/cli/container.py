import logging


class Container:
    def __init__(self, docker, args):
        self.docker = docker
        self.args = args

    def exec(self, **kwargs):
        self.start()
        self.docker.exec(**kwargs)
        self.stop()

    def stop(self, force=False):
        if not self.args.stop and not force:
            return
        if not self.docker.is_running():
            return
        self.docker.stop()

    def start(self):
        if self.args.rebuild or not self.docker.exists():
            if self.docker.is_running():
                logging.warning("stopping running container")
                self.docker.stop()
            self.docker.build(update=self.args.update)

        if self.docker.is_running():
            if not self.args.restart:
                return
            self.docker.stop()

        self.docker.remove()
        self.docker.run(mounts=self.args.mount)
