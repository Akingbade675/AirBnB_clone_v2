from fabric.api import run, put

def send_file():
    put('0-setup_web_static.sh', '~')
    run('ls')
