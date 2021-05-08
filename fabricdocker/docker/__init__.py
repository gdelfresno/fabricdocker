from fabric import task


@task
def login(c, user=None, password=None, registry=None):
    if user is None:
        user = c.docker.username

    if password is None:
        password = c.docker.password

    if not user or not password:
        raise ValueError('Docker user or password missing')

    c.run(
        f'docker login -u {user} -p {password} {registry if registry else ""}'
    )


@task
def logout(c, registry=None):
    c.run(f'docker logout {registry if registry else ""}')
