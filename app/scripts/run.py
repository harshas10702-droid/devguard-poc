import subprocess
import yaml

def run(cmd):
    subprocess.call(cmd, shell=True)  # dangerous: command injection

def load(data):
    return yaml.load(data)  # unsafe loader

run("echo hello")
