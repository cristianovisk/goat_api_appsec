from fastapi import FastAPI, HTTPException
import io
from starlette.responses import StreamingResponse
import uuid
import os
import uvicorn
import requests
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
def epoch_converter(num=1686707709):
    proc = subprocess.Popen(f'date -d @{num}', stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return {"date": out}

@app.get('/hello_world')
def hello_world(msg="hello_world"):
    if msg == "hello_world":
        return {"msg": "hello_world"}
    else:
        return {"msg": msg, "error": "not_hello_world"}
    
@app.get('/return_photo')
def return_photo(filename):
    files_types = ['jpg', 'png', 'svg']
    if filename[-3:] == files_types[0] or filename[-3:] == files_types[1] or filename[-3:] == files_types[2]:
        ext = filename[-3:]
        with open(f'photos/{filename}', 'rb') as file:
            return StreamingResponse(io.BytesIO(file.read()), media_type=f"image/{ext}")
    else:
        return {"status": "error", "msg": "invalid format file", "files_types": files_types}
    
@app.get('/upload_photo')
def upload_photo(url):
    files_types = ['jpg', 'png', 'svg']

    if os.path.exists('photos') == False:
        os.mkdir('photos')

    if url[-3:] == files_types[0] or url[-3:] == files_types[1] or url[-3:] == files_types[2]:
        ext = url[-3:]
        random = uuid.uuid4()
        
        with open(f'photos/{random}.{ext}', 'wb') as file:
            file.write(requests.get(url=url).content)

        return {"status": "uploaded", "file_name": f"{random}.{ext}"}
    else:
        return {"status": "error", "msg": "invalid format file", "files_types": files_types}

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

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8081, log_level="info", timeout_keep_alive=500, timeout_graceful_shutdown=500, ws_ping_timeout=500)