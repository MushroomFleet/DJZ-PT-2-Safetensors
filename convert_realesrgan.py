"""
RealESRGAN .pth to .safetensors Converter
Converts RealESRGAN 4Xplus model from .pth to .safetensors format.

Requirements:
- Python 3.12.9
- PyTorch 2.5.1+cu121
- safetensors

Usage:
python convert_realesrgan.py --input model.pth --output model.safetensors
"""

import os
import sys
import time
import argparse
import logging
from pathlib import Path
import torch
from safetensors.torch import save_file

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("conversion.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("RealESRGAN-Converter")

def setup_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Convert RealESRGAN .pth model to .safetensors format")
    parser.add_argument("--input", "-i", type=str, required=True, help="Input .pth model path")
    parser.add_argument("--output", "-o", type=str, help="Output .safetensors model path")
    return parser.parse_args()

def check_requirements():
    """Check if all required packages are installed"""
    logger.info("Checking requirements...")
    try:
        import torch
        logger.info(f"PyTorch version: {torch.__version__}")
        
        import safetensors
        logger.info(f"safetensors version: {safetensors.__version__}")
        
        logger.info("All requirements satisfied")
        return True
    except ImportError as e:
        logger.error(f"Missing requirement: {e}")
        logger.error("Please install required packages: pip install torch==2.5.1+cu121 safetensors")
        return False

def convert_model(input_path, output_path):
    """Convert .pth model to .safetensors format"""
    start_time = time.time()
    logger.info(f"Starting conversion of {input_path}")
    
    # Check if input file exists
    if not os.path.exists(input_path):
        logger.error(f"Input file not found: {input_path}")
        return False
    
    # Generate output path if not specified
    if output_path is None:
        output_path = str(Path(input_path).with_suffix('.safetensors'))
    
    try:
        # Load the PyTorch model
        logger.info("Loading PyTorch model...")
        state_dict = torch.load(input_path, map_location="cpu")
        
        # Handle different model formats
        if isinstance(state_dict, dict):
            # If it's already a state dict
            if 'params_ema' in state_dict:
                logger.info("Found EMA parameters, using those")
                model_weights = state_dict['params_ema']
            elif 'params' in state_dict:
                logger.info("Using 'params' key for weights")
                model_weights = state_dict['params']
            elif 'model' in state_dict and 'state_dict' in state_dict['model']:
                logger.info("Using nested model state dict")
                model_weights = state_dict['model']['state_dict']
            else:
                logger.info("Using direct state dict")
                model_weights = state_dict
        else:
            logger.error("Unknown model format")
            return False
        
        # Log model information
        total_params = sum(p.numel() for p in [torch.tensor(v) for v in model_weights.values()])
        logger.info(f"Model loaded: {len(model_weights)} tensors, {total_params} parameters")
        
        # Convert and save to safetensors format
        logger.info(f"Converting to .safetensors format and saving to {output_path}")
        save_file(model_weights, output_path)
        
        # Verify the saved file
        file_size = os.path.getsize(output_path) / (1024 * 1024)  # Size in MB
        logger.info(f"Saved .safetensors file (size: {file_size:.2f} MB)")
        
        elapsed_time = time.time() - start_time
        logger.info(f"Conversion completed successfully in {elapsed_time:.2f} seconds")
        return True
    
    except Exception as e:
        logger.error(f"Error during conversion: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return False

def main():
    """Main function"""
    logger.info("Starting RealESRGAN .pth to .safetensors converter")
    
    # Parse arguments
    args = setup_args()
    
    # Check requirements
    if not check_requirements():
        return 1
    
    # Convert model
    result = convert_model(args.input, args.output)
    
    if result:
        logger.info("Conversion successful")
        return 0
    else:
        logger.error("Conversion failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
