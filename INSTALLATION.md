# Complete Installation & Setup Guide

![ContentForge - AI Content Generator](https://img.shields.io/badge/ContentForge-Production%20Ready-success)

This guide will walk you through setting up ContentForge from scratch.

## 📋 Prerequisites Checklist

Before starting, make sure you have:

- [ ] Windows 10/11, Mac OS, or Linux
- [ ] 2GB RAM minimum (8GB+ recommended)
- [ ] 10GB free disk space (for AI models)
- [ ] Stable internet connection (for initial setup only)
- [ ] Administrator access (for initial installation)

**Estimated Setup Time: 15-30 minutes**

---

## 🚀 Installation Steps

### STEP 1: Install Ollama (5-10 minutes)

Ollama provides the local AI models that power the content generation.

#### Windows:

1. Go to https://ollama.com
2. Click "Download for Windows"
3. Run the installer (OllamaSetup.exe)
4. Follow the installation wizard
5. Ollama will start automatically

**Verify installation:**
- Look for Ollama in your system tray (bottom right)
- You should see the Ollama icon

#### Mac:

1. Go to https://ollama.com
2. Click "Download for Mac"
3. Open the DMG file
4. Drag Ollama to Applications folder
5. Launch Ollama from Applications

**Verify installation:**
- Open Terminal
- Type: `ollama --version`
- Should show version number

#### Linux:

1. Open Terminal
2. Run this command:
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```
3. Installation completes automatically

**Verify installation:**
```bash
ollama --version
```

---

### STEP 2: Download an AI Model (5-10 minutes)

After Ollama is installed, you need to download an AI model.

#### For Windows Users:

1. Open Command Prompt or PowerShell
2. Type this command:
   ```
   ollama run llama3
   ```
3. Press Enter
4. Let it download (it's ~4.1GB, so 5-15 minutes depending on internet speed)
5. When it says ">>> Type /bye to exit", you can close it

**The model is now installed!**

#### For Mac/Linux Users:

1. Open Terminal
2. Run this command:
   ```bash
   ollama run llama3
   ```
3. Press Enter
4. Let it download (same as above)
5. When ready, type `/bye` and press Enter to close

---

### STEP 3: Install Python (2 minutes)

You need Python 3.8 or newer.

#### Check if Python is Already Installed:

**Windows:**
- Open Command Prompt
- Type: `python --version`
- If it shows version 3.8+, skip to Step 4
- If "not found" error, continue below

**Mac/Linux:**
- Open Terminal
- Type: `python3 --version`
- If it shows version 3.8+, skip to Step 4
- If "not found" error, continue below

#### Install Python:

1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12
3. Run the installer
4. **IMPORTANT for Windows**: Check "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete

**Verify:**
```bash
python --version
```

---

### STEP 4: Download the Application (1 minute)

You already have the project folder in:
```
D:\A\Projects\AI Content Generation Studio
```

This contains all the necessary files.

---

### STEP 5: Install Python Dependencies (2-3 minutes)

1. Open Command Prompt (Windows) or Terminal (Mac/Linux)

2. Navigate to the project folder:
   ```bash
   # Windows
   cd "D:\A\Projects\AI Content Generation Studio"
   
   # Mac/Linux
   cd ~/path/to/"AI Content Generation Studio"
   ```

3. Install all required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Wait for installation to complete
   - You'll see a lot of text scrolling
   - When done, you should see "Successfully installed..."

**What's being installed:**
- streamlit (web interface)
- langchain (AI framework)
- langchain-community (AI tools)
- python-docx (Word document export)
- reportlab (PDF export)
- requests (API calls)
- pandas (data handling)

---

### STEP 6: Start the Application (1 minute)

1. Make sure Ollama is still running
   - Windows: Check system tray for Ollama icon
   - Mac/Linux: Can run `ollama serve` in another terminal

2. In your Command Prompt/Terminal, run:
   ```bash
   streamlit run app.py
   ```

3. You should see output like:
   ```
   Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.
   
   You can now view your Streamlit app in your browser.
   
   Local URL: http://localhost:8501
   Network URL: http://192.168.1.100:8501
   ```

4. Your browser should open automatically. If not:
   - Go to http://localhost:8501 manually
   - You'll see ContentForge!

---

## ✅ First Time Setup Complete!

Congratulations! Your app is ready to use.

### Quick Test:

1. Go to **Settings** tab
2. Click **Test Connection**
3. Should show "✅ Connection successful!"

---

## 🎯 Your First Content Generation

1. Click on **Generator** in the sidebar
2. Fill in the form:
   - **Content Type:** "Blog Post"
   - **Topic:** "The Future of AI"
   - **Audience:** "General tech enthusiasts"
   - **Tone:** "Professional"
   - **Style:** "Storytelling"

3. Click **Generate Content**
4. Wait 30-60 seconds (first generation takes longer)
5. You'll see your generated content!

---

## 📖 Next Steps

Now that you're set up, try these:

1. **Explore Templates**
   - Generate from prebuilt templates
   - Save your own templates

2. **Experiment with Models**
   - Try different models in Settings
   - Compare speed and quality

3. **Export Content**
   - Export as PDF, DOCX, or TXT
   - Include metadata automatically

4. **Build Your Library**
   - Save favorite outputs
   - Organize your history
   - Search previous generations

---

## 🔧 Advanced Setup (Optional)

### Create a Virtual Environment (Recommended for Developers)

This keeps your Python packages isolated:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

After this, always activate the environment before running:
```bash
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
streamlit run app.py
```

---

## 🆘 Troubleshooting Setup Issues

### "Ollama not found"

**Solution:**
1. Restart your computer (sometimes needed for PATH updates)
2. Open new Command Prompt/Terminal
3. Try again: `ollama --version`

### "Python not found"

**Solution:**
1. Go to System Properties → Environment Variables
2. Make sure Python path is in PATH
3. Restart Command Prompt/Terminal
4. Try: `python --version`

### "Streamlit command not found"

**Solution:**
```bash
python -m pip install streamlit
python -m streamlit run app.py
```

### "Can't connect to Ollama"

**Solution:**
1. Make sure Ollama is running (see system tray on Windows)
2. Try running: `ollama serve` in a new terminal
3. Make sure model is downloaded: `ollama run llama3`

### "ModuleNotFoundError: No module named..."

**Solution:**
```bash
pip install -r requirements.txt --force-reinstall
```

---

## 🎲 Different Models Available

After installation, try other models:

```bash
ollama pull mistral      # Fast model
ollama pull gemma        # Lightweight
ollama pull phi3         # Ultra-fast
ollama pull neural-chat  # Conversational
```

Then select in app Settings.

---

## 📊 System Requirements by Use Case

### Light Use (Casual)
- CPU: Quad-core processor
- RAM: 4GB
- Storage: 8GB
- Model: gemma or phi3
- Expected speed: 15-30 seconds per generation

### Regular Use
- CPU: 6-core processor
- RAM: 8GB
- Storage: 12GB
- Model: mistral or neural-chat
- Expected speed: 20-45 seconds per generation

### Power Users
- CPU: 8+ core processor
- RAM: 16GB+
- Storage: 15GB+
- Model: llama3
- Expected speed: 30-60 seconds per generation

---

## 🎉 You're All Set!

Your ContentForge is ready to go.

### Quick Reminders:

✓ Keep Ollama running in background
✓ App opens at http://localhost:8501
✓ All content stays on your computer
✓ No API keys or subscriptions needed
✓ Fully offline after setup
✓ 100% free forever

### Useful Commands:

```bash
# Run the app
streamlit run app.py

# Run on different port
streamlit run app.py --server.port 8502

# Run in headless mode (no browser)
streamlit run app.py --logger.level=off

# Check installed packages
pip list

# Update all packages
pip install --upgrade -r requirements.txt
```

---

## 📚 Documentation

- **README.md** - Full project documentation
- **QUICK_START.md** - Quick reference guide
- **FAQ.md** - Frequently asked questions
- **ARCHITECTURE.md** - Technical architecture
- **SAMPLE_OUTPUTS.md** - Example outputs

---

## 🚨 Emergency: Help It's Not Working!

1. **Stop the app**
   - Press Ctrl+C in the terminal

2. **Check Ollama**
   - Is the Ollama process running?
   - Try: `ollama serve` in new terminal

3. **Check model installed**
   - Run: `ollama list`
   - Should show llama3 or other models

4. **Restart everything**
   - Close app, restart Ollama, start app

5. **Check logs**
   - Start with: `streamlit run app.py --logger.level=debug`

6. **Read FAQ.md**
   - Most issues are documented there

---

## 🎓 Learning Resources

- [Ollama Documentation](https://ollama.ai)
- [Streamlit Docs](https://docs.streamlit.io)
- [LangChain Guide](https://python.langchain.com)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

---

## 🎊 Congratulations!

You now have a powerful, free, local AI content generation tool!

**Start creating amazing content today! ✨**

---

**Questions? Check FAQ.md or QUICK_START.md**
