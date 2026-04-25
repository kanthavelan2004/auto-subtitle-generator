@echo off
title Python Environment Setup
color 0B

echo ========================================
echo   Auto Subtitle Generator
echo   Python Environment Setup
echo ========================================
echo.

REM Check if Miniconda is installed
set "CONDA_PATH=%USERPROFILE%\miniconda3\condabin\conda.bat"
if not exist "%CONDA_PATH%" (
    set "CONDA_PATH=%USERPROFILE%\anaconda3\condabin\conda.bat"
)

if not exist "%CONDA_PATH%" (
    echo Anaconda/Miniconda not found!
    echo.
    echo Please install Miniconda first:
    echo https://docs.conda.io/en/latest/miniconda.html
    echo.
    echo After installation, run this script again.
    pause
    exit /b 1
)

echo Found Conda at: %CONDA_PATH%
echo.
echo Creating Python environment...
echo This may take 5-10 minutes.
echo.

REM Create conda environment
call "%CONDA_PATH%" create -n subtitle python=3.10 -y
if %errorlevel% neq 0 (
    echo ERROR: Failed to create environment!
    pause
    exit /b 1
)

echo.
echo Activating environment...
call "%CONDA_PATH%" activate subtitle

echo.
echo Installing PyTorch...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
if %errorlevel% neq 0 (
    echo ERROR: Failed to install PyTorch!
    pause
    exit /b 1
)

echo.
echo Installing Faster-Whisper...
pip install faster-whisper
if %errorlevel% neq 0 (
    echo ERROR: Failed to install Faster-Whisper!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo You can now run the application using 'run.bat'
echo.
pause