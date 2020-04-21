@echo off
set script_dir=%~dp0
echo %script_dir%

python -V
python %script_dir%/nj_ezpass_scrapper.py