from fastapi import FastAPI, HTTPException
import subprocess
import giturlparse

app = FastAPI(
    title="Goat API - AppSec Proof",
    version="0.0.1",
    description="Goat API AppSec Leveling Test",
    contact={
        "name": "Cristiano Henrique",
        "url": "https://github.com/cristianovisk",
        "email": "cristianovisk@gmail.com",
    }
    )

@app.get('/epoch')
def os(num):
    proc = subprocess.Popen(f'date -d @{num}', stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return {"date": out}

@app.get('/hello_world')
def hello(msg="hello_world"):
    if msg == "hello_world":
        return {"msg": "hello_world"}
    else:
        return {"msg": msg, "error": "not_hello_world"}

@app.get('/git_parse_url')
def git_parse(git_url='git@github.com:retr0h/ansible-etcd.git'):
    p = giturlparse.parse(git_url)
    tmp = {
        "owner": p.owner,
        "user": p.user,
        "path": p.pathname,
        "protocol": p.protocol,
        "name": p.name,
        "port": p.port,
        "resource": p.resource
    }
    return tmp