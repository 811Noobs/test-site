from flask import Flask, request, redirect, url_for
import os

UPLOAD_FOLDER = './uploads/'
DOWNLOAD_FOLDER = './test'
STORAGE_FOLDER = './storage'

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
if not os.path.exists(DOWNLOAD_FOLDER):
    os.mkdir(DOWNLOAD_FOLDER)
if not os.path.exists(STORAGE_FOLDER):
    os.mkdir(STORAGE_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['STORAGE_FOLDER'] = STORAGE_FOLDER
app.config['SECRET_KEY'] = 'unique-studio'
app.config['MAX_CONTENT_LENGTH'] = 256 * 1024 * 1024

from app import views