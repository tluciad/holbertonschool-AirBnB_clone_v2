#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
contents of the web_static folder"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


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
