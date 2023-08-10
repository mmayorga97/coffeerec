@echo off
call conda activate base
call conda env remove --name coffeerec --yes
call conda create -n coffeerec python=3.10 --yes
call conda activate coffeerec
call pip install -r requirements.txt
