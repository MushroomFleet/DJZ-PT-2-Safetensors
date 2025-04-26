@echo off
echo Setting up environment for RealESRGAN conversion...

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat


echo Environment Active!
echo.

python convert_realesrgan.py --input K:\MACHINES14\ComfyUI_windows_portable_nvidia\ComfyUI_windows_portable\ComfyUI\models\upscale_models\djz4XlandscapesV1.pt --output djz4XlandscapesV1.safetensors