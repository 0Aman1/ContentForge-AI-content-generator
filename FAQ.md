# FAQ & Troubleshooting Guide

## ❓ Frequently Asked Questions

### General Questions

**Q: Is this really free?**
A: Yes, 100% free forever. No hidden costs, no API keys needed, no subscriptions. All the tools used (Streamlit, LangChain, Ollama) are open-source and free.

**Q: Do I need internet?**
A: Once everything is installed, you can work completely offline. No cloud connectivity required.

**Q: What data gets collected?**
A: None. Everything runs locally on your machine. Your content never leaves your computer.

**Q: Can I use this commercially?**
A: Yes! MIT License allows commercial use. Generated content is yours to use as you wish.

**Q: How much disk space do I need?**
A: Minimum 10GB for models. llama3 is 4.1GB, mistral is 4GB, gemma is 2.6GB, phi3 is 2.3GB.

**Q: Can I use multiple models?**
A: Yes! Switch models anytime in Settings. All models can coexist on your system.

---

### Installation Questions

**Q: Where do I download Ollama?**
A: [https://ollama.com](https://ollama.com) - Select your operating system and download.

**Q: How long does model download take?**
A: Depends on your internet speed and model size:
- llama3 (4.1GB): 5-15 minutes
- mistral (4GB): 5-15 minutes
- gemma (2.6GB): 3-10 minutes
- phi3 (2.3GB): 2-8 minutes

**Q: I'm on Windows, what's the command?**
A: Open PowerShell or Command Prompt and type:
```
ollama run llama3
```

**Q: I'm on Mac/Linux, what's the command?**
A: Open Terminal and type:
```
ollama run llama3
```

**Q: Do I need admin rights?**
A: For initial installation yes, but not for running the app.

---

### Usage Questions

**Q: Why is generation slow?**
A: Possible reasons:
1. Using llama3 on a slow machine (try mistral or gemma)
2. Low RAM available (close other applications)
3. Too much context in the prompt (shorten it)
4. Low CPU/GPU resources

**Q: Can I generate multiple outputs at once?**
A: Yes, use the "Number of Outputs" slider (1-3). All three versions are generated sequentially.

**Q: How long should the topic/audience be?**
A: Specific descriptions (2-5 sentences) work best. More specific = better results.

**Q: Can I customize the prebuilt templates?**
A: Yes! Create custom templates by saving your own with placeholders like {name}, {topic}, etc.

**Q: Does keyword density matter?**
A: Yes for SEO content. The app calculates keyword density (usually 1-3% is good).

**Q: Can I export multiple versions at once?**
A: Yes! In the Export Center, use "Export All Versions" to generate separate files.

---

### Model Questions

**Q: Which model should I use?**
A: 
- **llama3** (recommended): Best quality, ~4.1GB
- **mistral**: Good balance of speed/quality, ~4GB
- **gemma**: Fast, lightweight, ~2.6GB
- **phi3**: Ultra-fast, smallest, ~2.3GB

**Q: Can I use unsupported models?**
A: If they're in Ollama, yes! Install via:
```
ollama pull model_name
```
Then select in Settings.

**Q: Model gives bad output, what do I change?**
A: Try:
1. Lower creativity slider (0.3-0.5)
2. Be more specific in topic
3. Change tone/style
4. Try a different model
5. Adjust keywords

**Q: Can I switch models mid-task?**
A: Yes! Change in Settings anytime. Takes effect immediately.

---

## 🔧 Troubleshooting

### Issue 1: "Ollama Server Not Running"

**Error Message:**
```
❌ Ollama Server Not Running

ContentForge requires Ollama to be running locally.
```

**Solution:**

1. **Windows:**
   - Ollama runs automatically after installation
   - Check if Ollama is in system tray (right side of taskbar)
   - If not running, search for "Ollama" in Start menu and click it

2. **Mac:**
   - Look for Ollama in Applications
   - Click to launch it

3. **Linux:**
   - Open terminal and run:
   ```bash
   ollama serve
   ```
   - Leave this terminal open

4. **Verify it's running:**
   - Open browser: http://localhost:11434
   - Should show Ollama page

---

### Issue 2: Model Download Fails

**Error:**
```
Error downloading model: connection timeout
```

**Solutions:**

1. **Check internet connection**
   ```bash
   ping ollama.com
   ```

2. **Download manually:**
   ```bash
   ollama pull llama3
   ```

3. **Try different model:**
   ```bash
   ollama pull mistral
   ```

4. **Check available space:**
   - Need 10GB+ free disk space
   - Check with `df -h` (Mac/Linux) or Disk Management (Windows)

5. **Restart Ollama:**
   - Kill Ollama process
   - Restart by running `ollama serve`

---

### Issue 3: Streamlit Not Found

**Error:**
```
'streamlit' is not recognized as an internal or external command
```

**Solution 1: Reinstall requirements**
```bash
pip install -r requirements.txt
```

**Solution 2: Use Python module**
```bash
python -m streamlit run app.py
```

**Solution 3: Check Python PATH**
```bash
python -m pip show streamlit
```

**Solution 4: Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

### Issue 4: Port 8501 Already in Use

**Error:**
```
Address already in use
```

**Solutions:**

1. **Use different port:**
   ```bash
   streamlit run app.py --server.port 8502
   ```

2. **Kill process using port (Windows):**
   ```bash
   netstat -ano | findstr :8501
   taskkill /PID <process_id> /F
   ```

3. **Kill process using port (Mac/Linux):**
   ```bash
   lsof -i :8501
   kill -9 <process_id>
   ```

---

### Issue 5: Out of Memory / Generation Fails

**Error:**
```
CUDA out of memory or RuntimeError
```

**Solutions:**

1. **Use smaller model:**
   - Try `phi3` or `gemma` instead of `llama3`

2. **Close other applications:**
   - Free up RAM by closing browser tabs, IDEs, etc.

3. **Restart Ollama:**
   ```bash
   # Kill and restart
   killall ollama  # Mac/Linux
   ollama serve
   ```

4. **Check available memory:**
   - Windows: Task Manager → Performance
   - Mac: Activity Monitor
   - Linux: `free -h`

5. **Reduce prompt complexity:**
   - Shorter topics/descriptions
   - Fewer keywords
   - Lower creativity slider

---

### Issue 6: Database Locked / SQLite Error

**Error:**
```
sqlite3.OperationalError: database is locked
```

**Solutions:**

1. **Close all app instances:**
   - Make sure only one Streamlit window is running

2. **Close browser windows:**
   - If left open overnight, may cause issues

3. **Restart app:**
   ```bash
   # Stop current app (Ctrl+C)
   # Clear cache
   streamlit run app.py --logger.level=debug
   ```

4. **Reset database:**
   ```bash
   # Backup first!
   copy content_studio.db content_studio.db.backup
   
   # Delete database (app will recreate)
   del content_studio.db
   
   # Restart app
   streamlit run app.py
   ```

---

### Issue 7: Export File Not Found

**Error:**
```
File not found in exports folder
```

**Solutions:**

1. **Check exports folder location:**
   ```bash
   # Should be in same directory as app.py
   ls exports/  # Mac/Linux
   dir exports  # Windows
   ```

2. **Verify permissions:**
   - Make sure you have write permissions
   - Try creating a file manually

3. **Check disk space:**
   - Ensure you have space for export files

4. **Use absolute path:**
   - If relative path fails, modify `export_utils.py`:
   ```python
   EXPORT_DIR = "C:/full/path/to/exports"
   ```

---

### Issue 8: Unicode/Encoding Errors

**Error:**
```
UnicodeDecodeError or encoding issues
```

**Solutions:**

1. **For Hindi/Marathi content:**
   - Ensure file encoding is UTF-8
   - Python should handle this automatically

2. **Set environment variable:**
   ```bash
   # Windows
   set PYTHONIOENCODING=utf-8
   streamlit run app.py
   
   # Mac/Linux
   export PYTHONIOENCODING=utf-8
   streamlit run app.py
   ```

3. **Use Python 3.8+**
   - Older versions may have encoding issues

---

### Issue 9: Template Placeholder Issues

**Error:**
```
Placeholders not generating correct output
```

**Solutions:**

1. **Check placeholder syntax:**
   - Use `{placeholder}` format (curly braces)
   - No spaces: `{name}` not `{ name }`

2. **Verify all placeholders filled:**
   - Every `{...}` needs a value

3. **Special characters escaped:**
   - If value contains braces, escape them

---

### Issue 10: Content Quality Issues

**Problem:** Generated content is low quality

**Solutions:**

1. **More specific input:**
   - Bad: "Write about technology"
   - Good: "Write a beginner's guide to machine learning for non-technical entrepreneurs"

2. **Adjust creativity:**
   - For factual content: 0.3-0.5
   - For creative content: 0.7-0.9

3. **Try different model:**
   - llama3 for quality
   - mistral for balanced
   - gemma for lighter tasks

4. **Better keywords:**
   - Specific keywords work better
   - Include variations

5. **Different tone/style:**
   - Some combinations work better than others
   - Experiment with different options

6. **Smaller chunks:**
   - Generate shorter content
   - Regenerate multiple times
   - Pick best version

---

## 🆘 Getting Additional Help

### Resources

1. **Official Documentation**
   - Ollama: https://olivier.ai
   - Streamlit: https://docs.streamlit.io
   - LangChain: https://python.langchain.com

2. **Community Support**
   - GitHub Issues (for this project)
   - Stack Overflow (tag: streamlit, langchain)
   - Reddit: r/MachineLearning, r/Python

3. **System Info for Debugging**
   ```bash
   python --version
   streamlit --version
   ollama --version
   pip show langchain
   pip show langchain-community
   ```

4. **Enable Debug Logging**
   ```bash
   streamlit run app.py --logger.level=debug
   ```

---

## ✅ Checklist Before Reporting Issues

Before asking for help, verify:

- [ ] Ollama is installed and running
- [ ] A model is pulled (ollama run llama3)
- [ ] Python 3.8+ is installed
- [ ] All requirements installed: `pip install -r requirements.txt`
- [ ] Running latest version of files
- [ ] Tried restarting app and Ollama
- [ ] Checked disk space and available RAM
- [ ] Tried different model or settings
- [ ] No other instances of app running
- [ ] System requirements met

---

## 🎯 Performance Optimization

### Make Generation Faster

1. **Use lightweight model:**
   ```bash
   ollama pull gemma  # Fastest
   ollama pull phi3   # Very fast
   ```

2. **Lower creativity:**
   - Slider to 0.3-0.5 (default 0.7)
   - Lower = faster + more factual

3. **Shorter prompts:**
   - Less context = faster generation
   - More specific = better quality

4. **Generate one at a time:**
   - Single output faster than multiple

5. **Close other apps:**
   - Free up system resources

### Make Exports Faster

1. **Export as TXT:**
   - Fastest format (~100ms)

2. **Batch export during off-peak:**
   - Multiple PDFs take time

3. **Check disk speed:**
   - Fast SSD = faster exports

---

**Still stuck? Try the latest FAQ version or check GitHub Issues!**
