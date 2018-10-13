﻿# Test Site  

## Introduce

Developed for [UniqueStudio](https://hustunique.com/) Stayup test.

Based on Python3 Flask

`uploads` and `test` will be created automatically.

The server will scan the dir and show all the test file.

Upload File Type Limit is compress files like 7z, zip, or gz.

Upload File Size Limit is 1000M and can be edited.

## Usage

Clone it and install dependencies.
``` shell
git clone https://github.com/NekodRider/test-site
cd test-site
# (OPTIONAL) git checkout semantic-theme
# (You may install dependencies by yourself)
pip3 install -r requirement.txt
```

Modify the port in run.py and the admin config in app/views.py.

then
```
python3 run.py
```
or using gunicorn
```
pip3 install gunicorn
gunicorn -w {WORKER_NUM} --bind {IP}:{PORT} run:app
```
