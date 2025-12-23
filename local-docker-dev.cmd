@echo off
set PATH=^
C:\Program Files\Docker\Docker\resources\bin;
docker --version &&^
docker compose up --build && docker compose down
pause
