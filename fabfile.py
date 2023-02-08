from fabric.api import run, put, env

env.hosts = ['54.146.67.10', '52.91.144.238']
env.user='ubuntu'

def send_file():
    put('0-setup_web_static.sh', '~')
    run('ls')
