@echo off
REM Quick setup script for AI Content Generation Studio (Windows)

echo.
echo 🚀 AI Content Generation Studio - Windows Setup
echo ==============================================
echo.

REM Check Python version
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
echo ✓ Python version: %python_version%

REM Check pip
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip not found
    pause
    exit /b 1
)
echo ✓ pip is installed

REM Install requirements
echo.
echo 📦 Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed successfully

REM Check Ollama
echo.
echo 🤖 Checking Ollama...
where ollama >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Ollama not found in PATH
    echo    Please install from https://ollama.com
) else (
    echo ✓ Ollama found
)

REM Done
echo.
echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Make sure Ollama is running (download and install from https://ollama.com)
echo 2. Open PowerShell or CMD and run: ollama pull llama3
echo 3. Run the app: streamlit run app.py
echo.
echo The app will open at http://localhost:8501
echo.
pause
