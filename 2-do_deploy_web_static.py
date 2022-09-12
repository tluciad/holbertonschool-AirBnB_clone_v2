#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""
from fabric.api import env, run, put
from os.path import exists


env.hosts = ['23.22.162.227', '3.80.117.130']
env.user = "ubuntu"


def do_deploy(archive_path):
    """module distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False

    try:
        file = archive_path.split("/")[-1]
        filename = file.split(".")[0]
        path = '/data/web_static/releases/web_static'

        put('archive_path', '/tmp/')
        run('mkdir -p {}{}/'.format(path, filename))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, filename))
        run('rm /tmp/{}'.format(file))
        run('mv {}{}/web_static/*{}{}'.format(path, filename))
        run('rm -rf {}{}/web_static/'.format(path, filename))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, filename))
        print('New version deployed!')
        return True
    except Exception:
        return False
