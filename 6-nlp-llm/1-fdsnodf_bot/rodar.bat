@echo off

chcp 65001 > nul

cd /d D:\phyton\fdsnodf_bot

C:\Users\henri\.local\bin\uv.exe run fdsnodf.py >> agendador_exec.log 2>&1