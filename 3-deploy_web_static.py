#!/usr/bin/python3
"""
 creates and distributes an archive to your web servers,
 using the function deploy
"""

from datetime import datetime
from fabric.api import *
from os.path import exists, isdir
env.hosts = ['52.90.59.238', '54.197.203.132']


def do_pack():
    """
    packs files in a compressed tgz archive
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    deploy the content the packed file on do_pack function
    to the web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_no_ext = file_name.split(".")[0]
        path_files = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path_files, file_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path_files, file_no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path_files, file_no_ext))
        run('rm -rf {}{}/web_static'.format(path_files, file_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path_files, file_no_ext))
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """
    call do_pack and do_deploy
    to create and deploy an archive to the web servers"""
    try:
        archive_path = do_pack()
    except Exception:
        return False

    return do_deploy(archive_path)
