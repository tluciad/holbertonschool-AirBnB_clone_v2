#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
contents of the web_static folder"""
from datetime import datetime
from fabric.api import local
from os.path import isdir
from fabric.api import env, run, put
from os.path import exists


env.hosts = ['23.22.162.227', '3.80.117.130']
env.user = "ubuntu"


def deploy():
    """module to creates and distributes an
    archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_pack():
    """module to archive from the contents of the web_static
    folder of your AirBnB Clone repo"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(date)
        if isdir("versions") is False:
            local("mkdir -p versions")
        local("tar -czvf {} web_static".format(file))
        return file
    except Exception:
        return None


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
