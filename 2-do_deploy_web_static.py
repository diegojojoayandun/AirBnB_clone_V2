#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web .
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.90.59.238', '54.197.203.132']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        without_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, without_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, without_ext))
        run('rm -rf /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, without_ext))
        # run('rm -rf {}{}/web_static'.format(path, without_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, without_ext))
        return True
    except Exception:
        return False
