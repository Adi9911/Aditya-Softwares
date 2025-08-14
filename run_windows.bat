@echo off
echo Starting Aditya Softwares Website...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt

REM Set environment variables
set FLASK_DEBUG=False
set PORT=8080

REM Start the application
echo.
echo Starting Flask application...
echo Website will be available at: http://localhost:8080
echo Press Ctrl+C to stop the server
echo.
python app.py

pause

