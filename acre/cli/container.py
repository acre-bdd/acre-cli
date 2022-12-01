import time
from acrelib import log


class Container:
    def __init__(self, docker, args):
        self.docker = docker
        self.args = args

    def exec(self, **kwargs):
        self.start()
        ec = self.docker.exec(**kwargs)
        self.stop()
        return ec

    def run(self, **kwargs):
        self.build()
        if self.args.mount:
            kwargs['mounts'] = self.args.mount
        return self.docker.run(**kwargs)

    def do(self, **kwargs):
        if self.args.detach:
            self.exec(**kwargs)
        else:
            self.run(**kwargs)

    def build(self, force=False):
        if self.args.rebuild or force or not self.docker.exists() or self.args.update:
            self.stop(force=True)
            log.info("(re-)building docker image")
            self.docker.build(self.args.update)
            if 'nowait' in self.args:
                time.sleep(10)

    def stop(self, force=False):
        if not self.args.stop and not force:
            return
        if not self.docker.is_running():
            return
        log.warning("stopping running container")
        self.docker.stop()

    def start(self):
        self.build()

        if self.args.restart:
            self.stop(force=True)

        if self.docker.is_running():
            return

        self.docker.remove()
        logging.info("starting docker container")
        self.docker.run(mounts=self.args.mount)
