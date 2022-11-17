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
        logging.warning("stopping running container")
        self.docker.stop()

    def start(self):
        if self.args.rebuild or not self.docker.exists():
            self.stop(force=True)
            logging.info("(re-)building docker image")
            self.docker.build(update=self.args.update)

        if self.args.restart:
            self.stop(force=True)

        if self.docker.is_running():
            return

        self.docker.remove()
        logging.info("starting docker container")
        self.docker.run(mounts=self.args.mount)
