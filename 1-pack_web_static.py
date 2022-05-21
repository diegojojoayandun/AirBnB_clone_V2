#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone V2 repo
"""

from datetime import datetime
from fabric.api import local
import os.path


def do_pack():
    """generates a tgz archive"""
    try:
        if os.path.isdir("versions") is False:
            local("mkdir -p versions")

        targz_file_name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))

        result = local("tar -cvzf {} web_static".format(targz_file_name))
        return result
    except Exception:
        return None
