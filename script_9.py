# 9. Requirements and Setup Files

# Requirements.txt
requirements_txt = '''
# Core dependencies
sqlalchemy>=1.4.0
python-magic>=0.4.24
python-magic-bin>=0.4.14  # For Windows

# PDF processing
pdfplumber>=0.7.0
pdf2image>=3.1.0

# Image processing and OCR
Pillow>=9.0.0
pytesseract>=0.3.10

# Office documents
python-docx>=0.8.11
pandas>=1.3.0
openpyxl>=3.0.9

# CAD files
ezdxf>=0.17.0

# Email processing
imapclient>=2.3.0
pyzmail36>=1.0.4

# File watching
watchdog>=2.1.0

# SharePoint (optional)
# Office365-REST-Python-Client>=2.3.11

# Utilities
requests>=2.25.0
'''

# Setup script
setup_py = '''
#!/usr/bin/env python3
"""
Setup script for KMRL Document Ingestion System
"""

import os
import sys
import subprocess

def install_requirements():
    """Install Python requirements"""
    print("Installing Python requirements...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def setup_tesseract():
    """Setup Tesseract OCR"""
    print("Setting up Tesseract OCR...")
    print("Please install Tesseract OCR manually:")
    print("- Ubuntu/Debian: sudo apt-get install tesseract-ocr tesseract-ocr-mal")
    print("- CentOS/RHEL: sudo yum install tesseract tesseract-langpack-mal")
    print("- Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
    print("- macOS: brew install tesseract tesseract-lang")

def setup_poppler():
    """Setup Poppler for PDF processing"""
    print("Setting up Poppler for PDF processing...")
    print("Please install Poppler manually:")
    print("- Ubuntu/Debian: sudo apt-get install poppler-utils")
    print("- CentOS/RHEL: sudo yum install poppler-utils")
    print("- Windows: Download from https://poppler.freedesktop.org/")
    print("- macOS: brew install poppler")

def create_directories():
    """Create necessary directories"""
    dirs = [
        'staging',
        'staging/email',
        'staging/file_watcher', 
        'staging/manual',
        'staging/sharepoint',
        'logs',
        'uploads',
        'watch_scans',
        'watch_uploads',
        'watch_cad'
    ]
    
    for dir_name in dirs:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Created directory: {dir_name}")

def create_env_file():
    """Create environment file template"""
    env_content = '''# KMRL Document Ingestion System Environment Variables

# Database
DATABASE_URL=sqlite:///kmrl_documents.db

# Email Configuration
IMAP_HOST=imap.gmail.com
EMAIL_USERNAME=your_email@example.com
EMAIL_PASSWORD=your_password

# SharePoint Configuration (optional)
SHAREPOINT_SITE_URL=https://yourcompany.sharepoint.com/sites/yoursite
SHAREPOINT_LIBRARY=Documents

# Logging
LOG_LEVEL=INFO
'''
    
    with open('.env.example', 'w') as f:
        f.write(env_content)
    print("Created .env.example file")

def main():
    print("Setting up KMRL Document Ingestion System...")
    print("="*50)
    
    # Install Python requirements
    try:
        install_requirements()
        print("✅ Python requirements installed")
    except Exception as e:
        print(f"❌ Failed to install requirements: {e}")
        return False
    
    # Create directories
    create_directories()
    print("✅ Directories created")
    
    # Create environment file
    create_env_file()
    print("✅ Environment template created")
    
    # Setup instructions for external dependencies
    print("\\n" + "="*50)
    print("MANUAL SETUP REQUIRED:")
    print("="*50)
    setup_tesseract()
    print()
    setup_poppler()
    
    print("\\n" + "="*50)
    print("SETUP COMPLETE!")
    print("="*50)
    print("Next steps:")
    print("1. Install Tesseract OCR and Poppler (see above)")
    print("2. Copy .env.example to .env and configure your settings")
    print("3. Test the system: python main.py test")
    print("4. Run the system: python main.py run")
    
    return True

if __name__ == "__main__":
    main()
'''

# Save files
with open('document_ingestion_system/requirements.txt', 'w') as f:
    f.write(requirements_txt)

with open('document_ingestion_system/setup.py', 'w') as f:
    f.write(setup_py)

print("✅ Requirements file created: document_ingestion_system/requirements.txt")
print("✅ Setup script created: document_ingestion_system/setup.py")