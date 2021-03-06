from fabric import task
from invoke import Collection


@task
def run_compose_command(c, command, **kwargs):
    compose_file = ':'.join(c.compose.file)
    command = f'COMPOSE_FILE={compose_file} docker-compose {command}'
    c.run(command, **kwargs)


# TODO Allow custom COMPOSE_FILE
@task
def build(c):
    c.run('docker-compose build')


@task
def up(c, services='', background=True):
    run_compose_command(c, f'up{" -d" if background else ""} {services}')


@task
def stop(c, services=''):
    run_compose_command(c, f'stop {services}')


@task
def start(c, services=''):
    run_compose_command(c, f'start {services}')


@task
def restart(c, services=''):
    run_compose_command(c, f'restart {services}')


@task
def logs(c, services=''):
    run_compose_command(c, f'logs {services}')


@task
def compose_info(c):
    display_compose_stats(c)


def display_compose_stats(c):
    run_compose_command(c, 'images')
    run_compose_command(c, 'ps')
    run_compose_command(c, 'logs --tail=20')


ns = Collection(compose_info)
ns.configure({'compose': {'file': []}})
