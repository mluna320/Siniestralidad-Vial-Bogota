@echo off
cd /d "%~dp0"
python -m pip install -r requirements.txt
if errorlevel 1 goto fallo
python -m streamlit run app\app.py --server.headless false --browser.gatherUsageStats false
exit /b 0
:fallo
echo Revise Python y las dependencias. Puede usar el HTML sin instalar nada.
pause
