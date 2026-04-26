# ContentForge - Quick Start Guide

## 🚀 Installation (5 minutes)

### Step 1: Download & Install Ollama
1. Go to https://ollama.com
2. Download and install for your OS
3. Once installed, download a model:
   ```
   ollama run llama3
   ```
   (This downloads ~4GB, so it may take a few minutes)

### Step 2: Install Python Dependencies
```bash
# Navigate to the project folder
cd "ContentForge"

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run the App
```bash
streamlit run app.py
```

The app opens automatically at http://localhost:8501

## 🎯 First Time Usage

1. **Dashboard** - See your stats and quick access buttons
2. **Generator** - Create your first piece of content
3. **Settings** - Configure your default model and preferences
4. **Templates** - Browse prebuilt templates
5. **History** - View all your generations
6. **Export** - Download your content in different formats

## 💡 Tips

- **Specific Prompts** = Better Content
  - Instead of "Blog about AI", try "A beginner's guide to machine learning for business owners"
  
- **Try Different Models** if results aren't good
  - llama3: Best quality (4.1GB)
  - mistral: Fast (4GB)
  - gemma: Lightweight (2.6GB)
  
- **Use Templates** for faster generation
  - Save time with prebuilt templates
  - Create custom templates for repeated use

- **Rewrite Features** to improve content
  - Make Shorter/Longer
  - Improve Grammar
  - SEO Optimize

## ⚠️ Troubleshooting

**"Ollama Server Not Running"**
- Make sure Ollama is installed and running
- Run `ollama serve` in a terminal

**"Model download failed"**
- Try: `ollama pull llama3`
- Or use a different model: `ollama pull mistral`

**"Streamlit command not found"**
- Try: `python -m streamlit run app.py`

**"Port 8501 already in use"**
- Use different port: `streamlit run app.py --server.port 8502`

## 📚 Supported Content Types

✓ Blog Posts
✓ Product Descriptions  
✓ Marketing Emails
✓ Cold Emails
✓ Social Media Posts (Instagram, LinkedIn, Facebook)
✓ Google Ads Copy
✓ SEO Descriptions
✓ YouTube Scripts

## 🎨 Customization

Edit `settings.json` to customize:
- Default model
- Default tone & style
- Default language
- Theme (light/dark)
- Export format

## 🔧 System Requirements

- Python 3.8+
- 8GB RAM (minimum)
- 10GB disk space for models
- Ollama installed

## 📞 Need Help?

1. Check README.md for detailed documentation
2. Ensure Ollama is running and has a model installed
3. Try a simpler model (gemma, phi3) if running slow
4. Check system resources (RAM, CPU)

## 🎉 Ready to Generate?

1. Make sure Ollama is running
2. Run: `streamlit run app.py`
3. Start creating amazing content!

**Happy generating! ✨**
