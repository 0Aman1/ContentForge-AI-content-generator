# 🔥 ContentForge - AI Content Generator

**Forge your content with AI. Locally. Freely. Powerfully.**

ContentForge is a powerful, production-ready AI content generation platform using **only free and open-source tools**. Generate blogs, emails, ads, social media posts, and business content using local AI models powered by Ollama.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## 🌟 Features

### ✅ Content Generation
- **10+ Content Types**: Blog posts, emails, social media, ads, product descriptions, and more
- **7+ Tones**: Professional, Friendly, Persuasive, Casual, Funny, Technical, Inspirational
- **5+ Styles**: Concise, Detailed, Storytelling, Corporate, Emotional, and more
- **Multilingual**: English, Hindi, Marathi
- **Multiple Outputs**: Generate 1-3 versions of the same content
- **Keyword Optimization**: Include keywords naturally in generated content

### 📚 Template Library
- **6 Prebuilt Templates**: Ready-to-use templates for common content types
- **Custom Templates**: Create and save your own templates
- **Template Management**: Organize, edit, and delete templates

### 📜 History & Management
- **SQLite Database**: Persistent storage of all generated content
- **Full Search**: Search and filter by content type, topic, date
- **Quick Access**: Easy access to previously generated content
- **Bulk Operations**: Clear history, export to CSV

### 💾 Export Options
- **Multiple Formats**: Export as TXT, DOCX, PDF
- **Batch Export**: Export multiple versions at once
- **Metadata Inclusion**: Add author, title, date to exported files
- **File Manager**: Manage exported files from the app

### 🎯 Advanced Features
- **Content Analytics**: Word count, character count, reading time
- **SEO Scoring**: Estimate SEO score and keyword density
- **Readability Analysis**: Flesch-Kincaid readability calculations
- **Content Rewriting**: Make shorter/longer, improve grammar, SEO optimize
- **Session Favorites**: Mark favorite outputs for quick access
- **Tone Detection**: Automatic tone detection in generated content

### ⚙️ AI Model Management
- **Local Models**: Powered by Ollama (100% local, no API calls)
- **Multiple Models**: Support for llama3, mistral, gemma, phi3, neural-chat
- **Model Switching**: Change models on the fly
- **Connection Testing**: Test Ollama connection status
- **Auto-detection**: Detects available models automatically

### 🎨 Premium UI
- **Modern Design**: Professional SaaS-like interface
- **Dark/Light Theme**: Choose your preferred theme
- **Responsive Layout**: Works on desktop, tablet, mobile
- **Interactive Widgets**: Card-based layout with metrics
- **Real-time Feedback**: Loading spinners and success messages

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** - [Download](https://www.python.org/downloads/)
2. **Ollama** - [Download](https://ollama.com)

### Step 1: Install Ollama

1. Download Ollama from [https://ollama.com](https://ollama.com)
2. Install and follow the setup wizard
3. Run Ollama in your terminal:
   ```bash
   ollama run llama3
   ```
   
   This will download the llama3 model (about 4.1 GB)

4. Ollama will automatically start a local server at `http://localhost:11434`

### Step 2: Install Project Dependencies

```bash
# Navigate to the project folder
cd "ContentForge"

# Install Python dependencies
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 How to Use

### Basic Workflow

1. **Select Content Type** - Choose what you want to create (Blog, Email, Social Media, etc.)
2. **Enter Topic** - Provide the main subject
3. **Define Audience** - Specify who you're writing for
4. **Choose Tone & Style** - Select the voice and format
5. **Set Length** - Pick short, medium, or long
6. **Add Keywords** - Include SEO keywords (optional)
7. **Generate** - Click "Generate Content"
8. **Edit & Export** - Use advanced options or export

### Dashboard
- View total content generated
- See word count statistics
- Quick access to all tools
- Session statistics

### Content Generator
- 10+ content types to choose from
- Advanced settings for creativity control
- Real-time feedback and loading indicators
- Multiple output versions

### History
- View all generated content
- Search by topic or content type
- Filter by date and type
- Delete individual entries
- Export history as CSV

### Templates
- Browse 6 prebuilt templates
- Create custom templates with placeholders
- Use templates to generate content
- Save and reuse your best templates

### Export Center
- Export to TXT, DOCX, PDF
- Include metadata (author, date, etc.)
- Batch export multiple outputs
- File management interface

### Settings
- Change AI model
- Set default tone, style, language
- Enable/disable features
- Test Ollama connection
- Reset to defaults

## 🎯 Supported Content Types

1. **Blog Post** - Long-form articles (800-1500 words)
2. **Product Description** - Product features and benefits
3. **Marketing Email** - Promotional emails
4. **Cold Email** - Outreach emails
5. **Instagram Caption** - Social media captions
6. **LinkedIn Post** - Professional social posts
7. **Facebook Ad** - Facebook advertisement copy
8. **Google Ad Copy** - Google Ads text
9. **SEO Description** - Meta descriptions
10. **YouTube Script** - Video scripts

## 🎨 Tones

- Professional
- Friendly
- Persuasive
- Luxury
- Casual
- Funny
- Technical
- Inspirational
- Urgent
- Educational

## 🖋️ Styles

- Concise
- Detailed
- Storytelling
- Corporate
- Emotional
- Data-driven
- Question-based
- Bullet-points
- Narrative
- Comparative

## 🤖 Supported AI Models

### llama3 (Recommended)
- **Size**: 4.1 GB
- **Speed**: Fast
- **Quality**: Excellent
- **Best for**: General purpose
- ```bash
  ollama run llama3
  ```

### mistral
- **Size**: 4 GB
- **Speed**: Very Fast
- **Quality**: Good
- **Best for**: Fast generation
- ```bash
  ollama run mistral
  ```

### gemma
- **Size**: 2.6 GB (7B) / 5 GB (13B)
- **Speed**: Extra Fast
- **Quality**: Good
- **Best for**: Resource-constrained systems
- ```bash
  ollama run gemma
  ```

### phi3
- **Size**: 2.3 GB
- **Speed**: Ultra Fast
- **Quality**: Good
- **Best for**: Low-resource devices
- ```bash
  ollama run phi3
  ```

### neural-chat
- **Size**: 4.5 GB
- **Speed**: Fast
- **Quality**: Good
- **Best for**: Conversational content
- ```bash
  ollama run neural-chat
  ```

## 📦 File Structure

```
contentforge/
├── app.py                  # Main Streamlit application
├── db.py                   # SQLite database management
├── generator.py            # Content generation engine
├── prompts.py              # Prompt templates and analysis
├── templates.py            # Template library management
├── export_utils.py         # Export functionality (TXT, DOCX, PDF)
├── settings.py             # Settings and session management
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── content_studio.db       # SQLite database (auto-created)
├── settings.json           # App settings (auto-created)
└── exports/                # Generated export files
    ├── content_yyyymmdd_hhmmss.txt
    ├── content_yyyymmdd_hhmmss.docx
    └── content_yyyymmdd_hhmmss.pdf
```

## 🔧 Advanced Configuration

### Custom Settings

Edit `settings.json` to customize defaults:

```json
{
    "theme": "light",
    "default_model": "llama3",
    "default_tone": "Professional",
    "default_style": "Concise",
    "default_language": "English",
    "auto_save_history": true,
    "export_format": "txt"
}
```

### Database Backup

Backup your history:
```bash
cp content_studio.db content_studio.db.backup
```

### Ollama Configuration

For faster generation, increase context size in Ollama:
```bash
OLLAMA_NUM_THREAD=8 ollama run llama3
```

## 🐛 Troubleshooting

### Issue: "Ollama Server Not Running"

**Solution:**
```bash
# Make sure Ollama is running
ollama serve

# In another terminal, run the app
streamlit run app.py
```

### Issue: Model Download Fails

**Solution:**
```bash
# Manually pull the model
ollama pull llama3

# Or try a different model
ollama pull mistral
```

### Issue: Out of Memory

**Solution:**
1. Use a smaller model (gemma, phi3)
2. Increase system RAM
3. Close other applications

### Issue: Streamlit not found

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or run with Python module
python -m streamlit run app.py
```

### Issue: Port 8501 already in use

**Solution:**
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

## 📊 Performance Tips

1. **Model Selection**: Use `gemma` or `phi3` for faster generation on slower machines
2. **Creativity Level**: Lower creativity (0.3-0.5) = faster generation
3. **Content Length**: Shorter content = faster generation
4. **Number of Outputs**: Generate 1 output at a time for best performance
5. **System Resources**: Close unnecessary applications to free up RAM

## 🔐 Privacy & Security

- ✅ **100% Local**: All data stays on your machine
- ✅ **No Cloud**: No data sent to external servers
- ✅ **No Tracking**: No analytics or usage tracking
- ✅ **No API Keys**: No authentication required
- ✅ **Open Source**: Code is transparent and auditable

## 📝 License

MIT License - Free to use, modify, and distribute

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Share templates

## 📧 Support

Having issues? Check:
1. [Ollama Documentation](https://ollama.ai)
2. [Streamlit Docs](https://docs.streamlit.io)
3. [LangChain Documentation](https://python.langchain.com)

## 🎓 Learning Resources

- **LangChain**: [python.langchain.com](https://python.langchain.com)
- **Ollama**: [ollama.ai](https://ollama.ai)
- **Streamlit**: [docs.streamlit.io](https://docs.streamlit.io)
- **Python**: [python.org](https://python.org)

## ⚡ Comparison: Free vs Paid Alternatives

| Feature | This App | ChatGPT | Claude | Gemini Pro |
|---------|----------|---------|--------|-----------|
| Cost | FREE | $20/mo | $20/mo | $20/mo |
| Local Run | ✅ | ❌ | ❌ | ❌ |
| No API Key | ✅ | ❌ | ❌ | ❌ |
| Data Privacy | ✅ | ❌ | ❌ | ❌ |
| Templates | ✅ | ❌ | ❌ | ❌ |
| Export Options | ✅ | Limited | Limited | Limited |
| History | ✅ | ✅ | ✅ | ✅ |
| Offline Mode | ✅ | ❌ | ❌ | ❌ |

## 🚀 Roadmap

Planned features for v2.0:
- [ ] Image generation with Stable Diffusion
- [ ] Multi-language support expansion
- [ ] AI-powered SEO tools
- [ ] Plagiarism detection
- [ ] Content collaboration features
- [ ] Advanced analytics dashboard
- [ ] API endpoint for programmatic access
- [ ] Browser extension for quick generation

## 💡 Tips & Tricks

1. **Better Results**: Be specific in topic and audience descriptions
2. **Quick Generation**: Use prebuilt templates for faster content creation
3. **Batch Work**: Generate multiple outputs and choose the best
4. **Keyword Focus**: Add relevant keywords for better SEO content
5. **Rewriting**: Use rewrite options to improve generated content
6. **Favorites**: Save best outputs as session favorites for later
7. **Export Early**: Export important content immediately

## 🎉 Special Thanks

- **Ollama** - For making local models accessible
- **Streamlit** - For the amazing web framework
- **LangChain** - For the AI orchestration framework
- **Open Source Community** - For all the amazing tools

## 📄 Legal Notice

This project is for educational and personal use. Generated content is your responsibility. Always review and verify content before publishing.

---

**Made with ❤️ by the Open Source Community**

**Start forging amazing content today! 🔥**
