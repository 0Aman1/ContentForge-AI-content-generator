#!/bin/bash
# Quick setup script for AI Content Generation Studio

echo "🚀 AI Content Generation Studio - Setup Script"
echo "=============================================="
echo ""

# Check Python version
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip not found. Please install Python with pip."
    exit 1
fi

echo "✓ pip found"

# Install requirements
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Check Ollama
echo ""
echo "🤖 Checking Ollama..."
if command -v ollama &> /dev/null; then
    echo "✓ Ollama found: $(ollama --version)"
else
    echo "⚠️  Ollama not found in PATH"
    echo "   Please ensure Ollama is installed from https://ollama.com"
fi

# Start the app
echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Make sure Ollama is running: ollama serve"
echo "2. Install a model: ollama run llama3"
echo "3. Run the app: streamlit run app.py"
echo ""
echo "The app will open at http://localhost:8501"
