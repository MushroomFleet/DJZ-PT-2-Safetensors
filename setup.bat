@echo off
echo Setting up environment for RealESRGAN conversion...

:: Create virtual environment
echo Creating Python virtual environment...
python -m venv venv

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Install dependencies
echo Installing required packages...
pip install torch==2.5.1+cu121 torchvision --index-url https://download.pytorch.org/whl/cu121
pip install safetensors

echo Environment setup complete!
echo.
echo To use the converter:
echo 1. Activate the virtual environment: call venv\Scripts\activate.bat
echo 2. Run: python convert_realesrgan.py --input your_model.pth --output your_model.safetensors
echo.
pause
