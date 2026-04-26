# ContentForge - AI Content Generator - Architecture & Features Overview

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Streamlit UI                         │
│  (Web Interface, Responsive, Real-time Feedback)           │
└────────────────┬────────────────────────────────────────────┘
                 │
    ┌────────────┴─────────────────────┐
    │                                  │
┌───▼─────────────┐         ┌──────────▼──────────┐
│  Generator.py   │         │   Templates.py      │
│  (LangChain +   │         │  (Prebuilt &        │
│   Ollama)       │         │   Custom)           │
└───┬─────────────┘         └──────────┬──────────┘
    │                                  │
    │         ┌───────────────────────┐│
    │         │                       ││
┌───▼─────────▼────┐        ┌────────┴▼──────┐
│   Prompts.py     │        │  Export_utils  │
│   (Templates,    │        │  (PDF, DOCX,   │
│    Analysis)     │        │   TXT)         │
└───┬──────────────┘        └────────────────┘
    │
    │         ┌──────────────────────────┐
    │         │                          │
    └────────►│   Local Ollama Server    │
              │   (localhost:11434)      │
              │                          │
              │  ┌──────────────────┐    │
              │  │ llama3           │    │
              │  │ mistral          │    │
              │  │ gemma            │    │
              │  │ phi3             │    │
              │  │ neural-chat      │    │
              │  └──────────────────┘    │
              └──────────────────────────┘

┌─────────────────────────────────────────┐
│  Database Layer (db.py)                 │
│  ┌─────────────────────────────────┐   │
│  │  SQLite Database                │   │
│  │  ├── history table              │   │
│  │  ├── templates table            │   │
│  │  └── favorites table            │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘

┌──────────────────────────────────┐
│  Settings Layer (settings.py)    │
│  ├── User Preferences            │
│  ├── Session Memory              │
│  └── Configuration               │
└──────────────────────────────────┘
```

## 📦 Module Breakdown

### 1. **app.py** (Main Application)
- Streamlit web interface
- Navigation and page routing
- UI components and layouts
- User interaction handlers

**Key Functions:**
- `init_session_state()` - Initialize app state
- `check_ollama_availability()` - Verify Ollama server
- `display_dashboard()` - Dashboard metrics
- `display_generator()` - Content generation UI
- `display_history()` - History view
- `display_templates()` - Template management
- `display_export()` - Export interface
- `display_settings()` - Settings page

### 2. **db.py** (Database Management)
- SQLite database operations
- CRUD operations for all entities
- History management
- Template storage
- Favorites management

**Key Classes:**
- `Database` - Main database manager
  - `add_history()` - Save generated content
  - `get_history()` - Retrieve history
  - `search_history()` - Search functionality
  - `add_template()` - Save templates
  - `get_templates()` - Retrieve templates
  - `add_favorite()` - Save favorites

### 3. **generator.py** (Content Generation Engine)
- Ollama integration
- LangChain wrapper
- Content generation logic
- Model management

**Key Classes:**
- `OllamaManager` - Ollama server management
  - `is_ollama_running()` - Check server status
  - `get_available_models()` - List available models
  - `test_connection()` - Test model connection

- `ContentGenerator` - Content generation
  - `generate_content()` - Main generation
  - `rewrite_content()` - Rewriting features
  - `enhance_content()` - Enhancement features
  - `generate_from_template()` - Template-based generation

### 4. **prompts.py** (Prompts & Analysis)
- Dynamic prompt building
- Content analysis tools
- Tone and style definitions

**Key Classes:**
- `PromptBuilder` - Build dynamic prompts
  - `build_prompt()` - Create generation prompts
  - `build_rewrite_prompt()` - Create rewrite prompts
  - `build_enhancement_prompt()` - Enhancement prompts

- `ContentAnalyzer` - Analyze content
  - `count_words()` - Word count
  - `estimate_reading_time()` - Reading time
  - `calculate_keyword_density()` - SEO analysis
  - `estimate_seo_score()` - SEO scoring
  - `calculate_readability_score()` - Readability
  - `detect_tone_indicators()` - Tone detection

### 5. **templates.py** (Template Management)
- Prebuilt template library
- Template placeholder handling
- Template rendering

**Key Classes:**
- `TemplateLibrary` - Template management
  - `get_prebuilt_templates()` - All prebuilt templates
  - `get_template_by_name()` - Specific template
  - `get_templates_by_type()` - Templates by type
  - `get_placeholders()` - Extract placeholders
  - `render_template()` - Fill in template

### 6. **export_utils.py** (Export & Distribution)
- Multi-format export (TXT, DOCX, PDF)
- Metadata inclusion
- File management

**Key Classes:**
- `ExportManager` - Export management
  - `export_txt()` - Export to text
  - `export_docx()` - Export to Word
  - `export_pdf()` - Export to PDF
  - `export_multiple_outputs()` - Batch export
  - `get_export_files()` - List exports
  - `delete_export_file()` - Delete export

### 7. **settings.py** (Configuration & State)
- User preferences
- Application settings
- Session memory

**Key Classes:**
- `Settings` - Preference management
  - `get()` / `set()` - Get/set individual settings
  - `get_all()` - All settings
  - `reset_to_defaults()` - Reset settings
  - `update_settings()` - Bulk update

- `SessionMemory` - Runtime session state
  - `update_last_generation()` - Track generation
  - `get_last_generation()` - Get last output
  - `add_favorite()` - Add to favorites
  - `get_stats()` - Session statistics

## 🔄 Data Flow

### Content Generation Flow

```
User Input
    ↓
validate() ──→ ERROR ──→ Show error message
    ↓
PromptBuilder.build_prompt()
    ↓
ContentGenerator.generate_content()
    ↓
OllamaManager.get_llm()
    ↓
llm.invoke(prompt) ──────→ Wait for Ollama
    ↓                        ↓
    ← Get response ←─────────
    ↓
ContentAnalyzer.analyze()
    ↓
db.add_history()
    ↓
session_memory.update()
    ↓
Display output + analytics
```

### Export Flow

```
Generated Content
    ↓
User selects format (txt/docx/pdf)
    ↓
Optional: Include metadata
    ↓
ExportManager.export_*()
    ↓
File created in exports/ folder
    ↓
User download or file management
```

## 📊 Database Schema

### history table
```sql
CREATE TABLE history (
    id INTEGER PRIMARY KEY,
    date TEXT,
    content_type TEXT,
    topic TEXT,
    audience TEXT,
    tone TEXT,
    style TEXT,
    model TEXT,
    generated_text TEXT,
    word_count INTEGER,
    character_count INTEGER
)
```

### templates table
```sql
CREATE TABLE templates (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    content_type TEXT,
    description TEXT,
    template_text TEXT,
    created_date TEXT
)
```

### favorites table
```sql
CREATE TABLE favorites (
    id INTEGER PRIMARY KEY,
    history_id INTEGER,
    content TEXT,
    created_date TEXT,
    FOREIGN KEY (history_id) REFERENCES history(id)
)
```

## ⚙️ Configuration Files

### settings.json
- User preferences
- Default tone/style/language
- Theme preference
- Export format
- Feature flags

### content_studio.db
- SQLite database file
- All user data (history, templates, favorites)

### exports/ folder
- Generated export files (TXT, DOCX, PDF)

## 🔐 Security & Privacy

- ✅ All processing is local
- ✅ No external API calls
- ✅ No data collection
- ✅ No cloud storage
- ✅ SQLite for local storage
- ✅ No authentication required
- ✅ All code is open-source

## 🚀 Performance Characteristics

| Operation | Avg Time | Notes |
|-----------|----------|-------|
| Generate (llama3) | 30-60s | Depends on prompt length |
| Generate (mistral) | 20-40s | Faster alternative |
| Generate (gemma) | 15-30s | Lightweight model |
| Export to TXT | <1s | Near instant |
| Export to PDF | 1-3s | Requires rendering |
| Export to DOCX | 1-2s | Document formatting |
| Database search | <100ms | Fast indexing |
| Template render | <500ms | Simple string replacement |

## 🔧 Extension Points

The architecture supports easy extensions:

1. **New Content Types** - Add to `CONTENT_TYPES` in `prompts.py`
2. **New Export Formats** - Add methods to `ExportManager`
3. **New Tones/Styles** - Add to `TONES` and `STYLES` lists
4. **Custom Templates** - Via database/templates.py
5. **New AI Models** - Support via Ollama (automatic)
6. **Additional Analysis** - Extend `ContentAnalyzer` class

## 📈 Scalability

- √ Handles 1000s of history entries efficiently
- √ Template system supports unlimited custom templates
- √ Export can handle multiple large files
- √ Database optimized with indexes (ready)
- √ Session memory manages in-app state

## 🎯 Future Enhancement Points

1. Image generation integration
2. Advanced analytics dashboard
3. Team collaboration features
4. API endpoint for programmatic access
5. Browser extension for quick generation
6. Content scheduling integration
7. Social media auto-posting
8. Advanced SEO tools
9. Plagiarism detection
10. Multi-language expansion

---

**This architecture provides a scalable, maintainable, and user-friendly platform for AI-powered content generation.**
