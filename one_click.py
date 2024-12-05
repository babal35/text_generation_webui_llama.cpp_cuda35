import argparse
import os
import platform
import subprocess
import sys

# Command-line flags
flags = " ".join([arg for arg in sys.argv[1:]])

def get_user_choice(question, options_dict):
    print("\n" + question + "\n")
    for key, value in options_dict.items():
        print(f"{key}) {value}")
    print()
    choice = input("Input> ").upper()
    while choice not in options_dict.keys():
        print("Invalid choice. Please try again.")
        choice = input("Input> ").upper()
    return choice

def install_requirements():
    """Install all dependencies from requirements.txt, skipping llama-cpp-python and PyTorch."""
    print("\nInstalling dependencies from requirements.txt...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--no-deps"])
        print("\nDependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"\nFailed to install dependencies: {e}")
        sys.exit(1)

def use_existing_llama_cpp_python():
    """Configuration for using llama-cpp-python already installed."""
    print("\nUsing existing llama-cpp-python and PyTorch installations...")
    # Add any specific configuration or checks here if necessary
    print("Configuration complete. No additional installation needed.")

def main():
    choice = get_user_choice(
        "Select your GPU option:",
        {
            'A': 'NVIDIA (CUDA 12.1)',
            'B': 'NVIDIA (CUDA 3.5 - Use existing llama-cpp-python)',
            'N': 'None (CPU mode)'
        },
    )

    if choice == 'A':
        print("\nSetting up for NVIDIA CUDA 12.1...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "torch==2.4.1", "torchvision==0.19.1", 
            "torchaudio==2.4.1", "--index-url", "https://download.pytorch.org/whl/cu121"
        ])
    elif choice == 'B':
        print("\nSetting up for NVIDIA CUDA 3.5...")
        use_existing_llama_cpp_python()
    elif choice == 'N':
        print("\nSetting up for CPU mode...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "torch==2.4.1", "torchvision==0.19.1", 
            "torchaudio==2.4.1", "--index-url", "https://download.pytorch.org/whl/cpu"
        ])

    # Install the remaining dependencies
    install_requirements()

    # Launch the application (placeholder for actual launch command)
    print("\nSetup complete. You can now run the application.")

if __name__ == "__main__":
    main()
