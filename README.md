# 🔥🔥🔥 DJZ-PT-2-Safetensors 🔥🔥🔥

> 💯 Because file extensions shouldn't stop you from achieving GREATNESS! 💯

## 🤔 What is this? 🤔

This is a **REVOLUTIONARY** 🚀 Python utility that converts PyTorch model files (`.pt`/`.pth`) to the magnificent `.safetensors` format! 🎭 Specifically designed for AI upscalers like RealESRGAN and other PyTorch models when you need to upload them to platforms that don't accept `.pth` files! 🤦‍♂️

Created by the **LEGENDARY** 🏆 MushroomFleet 🍄 to solve real-world problems that nobody talks about but EVERYONE experiences! 😤

## 🎯 What does this do? 🎯

This tool performs the following **MIND-BLOWING** operations:

- 🔄 Converts PyTorch models (`.pth`/`.pt`) → `.safetensors` format
- 📊 Preserves ALL tensor data with ZERO loss of quality ✨
- 🧠 Intelligently handles various model architectures and state dict formats
- 📝 Provides DETAILED logging so you know EXACTLY what's happening
- 💾 Saves disk space (sometimes) because `.safetensors` can be more efficient
- 🛡️ Improves security since `.safetensors` doesn't execute arbitrary code
- 😎 Makes you look COOL when uploading to model distribution platforms

## 🔧 How does this work? 🔧

The conversion process is ***PURE TECHNICAL WIZARDRY*** 🧙‍♂️:

1. 📥 Your original `.pth` file contains tensors stored in PyTorch's native format
2. 🔍 Our script lovingly examines the model structure to identify the correct state dictionary
3. 🧮 It handles various model formats including:
   - Direct state dictionaries
   - Models with EMA parameters (`params_ema`)
   - Models with standard parameters (`params`)
   - Nested model structures 
4. 🔄 Each tensor is extracted and carefully preserved
5. 📦 The tensors are repackaged into the `.safetensors` format
6. 📤 A new `.safetensors` file is created, ready for GLORY! 🏅

💣 Under the hood, we're using the `safetensors` library which provides a more secure and efficient format for storing model weights without the security risks associated with pickle-based formats! 💣

## 🚀 Installation 🚀

### 💻 Prerequisites 💻

- Python 3.12+ (because we're NOT living in the STONE AGE! 🦖)
- Windows, macOS, or Linux (we don't discriminate! 🌈)
- PyTorch 2.5.1+ (or whatever version your model was trained with)
- A burning desire to CONVERT SOME MODELS! 🔥

### 🔽 Installation Steps 🔽

1. **Clone this MAGNIFICENT repository:**
```bash
git clone https://github.com/MushroomFleet/DJZ-PT-2-Safetensors.git
cd DJZ-PT-2-Safetensors
```

2. **Set up a virtual environment** (because we're PROFESSIONALS! 👔):
```bash
# For Windows 🪟
setup-script.bat

# For Linux/Mac 🐧🍎
chmod +x setup.sh
./setup.sh
```

3. **Activate the virtual environment:**
```bash
# Windows 🪟
call venv\Scripts\activate.bat

# Linux/Mac 🐧🍎
source venv/bin/activate
```

4. **Verify installation** (TRUST BUT VERIFY! 🕵️‍♂️):
```bash
python -c "import torch; import safetensors; print(f'PyTorch: {torch.__version__}, Safetensors: {safetensors.__version__}')"
```

If you see version numbers and not errors, you're READY TO ROCK! 🎸

## 🎮 How to Use It 🎮

### 🌟 Basic Usage 🌟

```bash
python convert_realesrgan.py --input your_amazing_model.pth --output your_even_more_amazing_model.safetensors
```

THIS IS NOT A DRILL! 🚨 It's really that simple! One command to RULE THEM ALL! 💍

### 🔬 Step-by-Step Example with RealESRGAN 4x+ 🔬

1. **Download a RealESRGAN model** you want to convert:
```bash
# Example: Getting RealESRGAN 4x+ model
curl -LO https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
```

2. **Place the model** in your project directory:
```bash
# You can do this manually or with this AMAZING command!
mv RealESRGAN_x4plus.pth /path/to/DJZ-PT-2-Safetensors/
```

3. **Run the conversion** (THE MOMENT OF TRUTH! 🎭):
```bash
python convert_realesrgan.py --input RealESRGAN_x4plus.pth --output RealESRGAN_x4plus.safetensors
```

4. **Watch the MAGIC happen** ✨:
```
2025-04-26 14:30:25 - RealESRGAN-Converter - INFO - Starting RealESRGAN .pth to .safetensors converter
2025-04-26 14:30:25 - RealESRGAN-Converter - INFO - Checking requirements...
2025-04-26 14:30:25 - RealESRGAN-Converter - INFO - PyTorch version: 2.5.1+cu121
2025-04-26 14:30:25 - RealESRGAN-Converter - INFO - safetensors version: 0.4.5
2025-04-26 14:30:25 - RealESRGAN-Converter - INFO - All requirements satisfied
2025-04-26 14:30:25 - RealESRGAN-Converter - INFO - Starting conversion of RealESRGAN_x4plus.pth
2025-04-26 14:30:28 - RealESRGAN-Converter - INFO - Loading PyTorch model...
2025-04-26 14:30:30 - RealESRGAN-Converter - INFO - Found EMA parameters, using those
2025-04-26 14:30:30 - RealESRGAN-Converter - INFO - Model loaded: 594 tensors, 16424398 parameters
2025-04-26 14:30:30 - RealESRGAN-Converter - INFO - Converting to .safetensors format and saving to RealESRGAN_x4plus.safetensors
2025-04-26 14:30:33 - RealESRGAN-Converter - INFO - Saved .safetensors file (size: 125.76 MB)
2025-04-26 14:30:33 - RealESRGAN-Converter - INFO - Conversion completed successfully in 7.89 seconds
2025-04-26 14:30:33 - RealESRGAN-Converter - INFO - Conversion successful
```

5. **Verify your STUNNING new `.safetensors` file** 🕵️‍♂️:
```bash
ls -lh RealESRGAN_x4plus.safetensors
```

BEHOLD! 👀 Your model is now in `.safetensors` format, ready for upload to ANY platform that accepts this format! 🚀

### 🧪 Advanced Usage (for POWER USERS ONLY! 💪)

For the BRAVE SOULS 🦸‍♂️ who need more control:

```bash
# Use custom logging location (FOR THE DETAIL-ORIENTED! 🔎)
python convert_realesrgan.py --input model.pth --output model.safetensors --log-file my_special_log.txt

# Convert and validate (TRUST ISSUES? WE GOT YOU! 🛡️)
python convert_realesrgan.py --input model.pth --output model.safetensors --validate

# Force conversion even with unknown model structure (LIVING DANGEROUSLY! 🏄‍♂️)
python convert_realesrgan.py --input model.pth --output model.safetensors --force
```

## 💪 Use Cases 💪

- 🖼️ Convert RealESRGAN upscaler models for ComfyUI
- 🎨 Convert Stable Diffusion models to `.safetensors`
- 🤖 Convert ANY PyTorch model for platforms that require `.safetensors`
- 🛡️ Convert your models to a more secure format
- 🚀 Look like a TECH GENIUS in front of your friends! 😎

## ⚠️ Troubleshooting ⚠️

| Problem | Solution |
|---------|----------|
| 😱 `ModuleNotFoundError: No module named 'torch'` | 🔧 Did you activate the virtual environment? Try `call venv\Scripts\activate.bat` (Windows) or `source venv/bin/activate` (Linux/Mac) |
| 🤔 `Error during conversion: Unknown model format` | 🧠 Your model structure is unique! Use `--force` option or create an issue on GitHub |
| 💥 `CUDA out of memory` | 🐢 Your model is TOO THICC! Try adding `--cpu-only` to use CPU instead |
| 🐌 Conversion is too slow | ⏱️ Patience, grasshopper! Big models take time. Get a ☕ while you wait |
| 🧨 Any other catastrophic error | 🆘 Create an issue on GitHub with your log file and we'll help! |

## 📜 License 📜

This project is licensed under the **MIT License** - see the LICENSE file for details. 📋

## 🙏 Acknowledgments 🙏

- 🍄 **MushroomFleet** - For being ABSOLUTELY LEGENDARY
- 👩‍💻 The **PyTorch Team** - For making amazing deep learning tools
- 🔒 The **safetensors Team** - For creating a more secure tensor format
- 🌟 **YOU** - For having EXCELLENT TASTE in GitHub repositories! 👏

---

## ⭐ If this tool saved your life (or just your model uploads), consider giving it a star! ⭐

### 🔮 Remember: Great models deserve great formats! 🔮

**Powered by the INCREDIBLE 🍄 MushroomFleet team**

*Last updated: April 26, 2025* 📅
