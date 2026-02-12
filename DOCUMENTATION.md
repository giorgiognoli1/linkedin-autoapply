# 📋 LinkedIn AI Auto Job Applier - Documentazione Completa

> **Bot automatico per candidature LinkedIn** con supporto AI (Gemini, OpenAI, DeepSeek) per risposte intelligenti e generazione CV personalizzati.

---

## 📑 Indice

- [Panoramica](#panoramica)
- [Requisiti di Sistema](#requisiti-di-sistema)
- [Installazione](#installazione)
- [Struttura del Progetto](#struttura-del-progetto)
- [Configurazione](#configurazione)
  - [1. Credenziali LinkedIn (secrets.py)](#1-credenziali-linkedin-secretspy)
  - [2. Dati Personali (personals.py)](#2-dati-personali-personalspy)
  - [3. Risposte alle Domande (questions.py)](#3-risposte-alle-domande-questionspy)
  - [4. Parametri di Ricerca (search.py)](#4-parametri-di-ricerca-searchpy)
  - [5. Impostazioni Bot (settings.py)](#5-impostazioni-bot-settingspy)
- [Configurazione AI](#configurazione-ai)
  - [Gemini (Google)](#gemini-google)
  - [OpenAI](#openai)
  - [DeepSeek](#deepseek)
- [Utilizzo](#utilizzo)
- [Output e Log](#output-e-log)
- [Troubleshooting](#troubleshooting)
- [Disclaimer](#disclaimer)

---

## Panoramica

Questo bot automatizza il processo di candidatura su LinkedIn:

1. 🔍 **Cerca lavori** in base ai tuoi criteri
2. 📝 **Compila automaticamente** i moduli Easy Apply
3. 🤖 **Risponde alle domande** usando AI (opzionale)
4. 📄 **Genera CV personalizzati** per ogni candidatura (opzionale)
5. 📊 **Traccia tutte le candidature** in file Excel

**Capacità**: Può inviare 100+ candidature in meno di 1 ora.

---

## Requisiti di Sistema

| Requisito | Versione/Dettagli |
|-----------|-------------------|
| **Python** | 3.10 o superiore |
| **Google Chrome** | Ultima versione |
| **Sistema Operativo** | Windows, macOS, Linux |
| **RAM** | Minimo 4GB (8GB consigliato) |
| **Connessione Internet** | Stabile |

---

## Installazione

### 1. Installa Python

Scarica Python da [python.org](https://www.python.org/downloads/) e assicurati che sia aggiunto al PATH di sistema.

Verifica l'installazione:
```bash
python3 --version
```

### 2. Installa le Dipendenze

```bash
pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask google-generativeai
```

### 3. Installa Google Chrome

Scarica e installa dalla [pagina ufficiale](https://www.google.com/chrome).

### 4. Clona/Scarica il Progetto

```bash
git clone https://github.com/GodsScion/Auto_job_applier_linkedIn.git
cd Auto_job_applier_linkedIn
```

### 5. Configura i File

Modifica i file nella cartella `config/` come descritto nella sezione [Configurazione](#configurazione).

---

## Struttura del Progetto

```
Auto_job_applier_linkedIn/
├── config/                          # 📁 File di configurazione
│   ├── personals.py                 #    Dati personali (nome, telefono, etc.)
│   ├── questions.py                 #    Risposte alle domande comuni
│   ├── search.py                    #    Parametri di ricerca lavoro
│   ├── secrets.py                   #    Credenziali e API keys
│   ├── settings.py                  #    Impostazioni del bot
│   └── resume.py                    #    Configurazione CV
│
├── modules/                         # 📁 Moduli del bot
│   ├── ai/                          #    Integrazioni AI
│   │   ├── geminiConnections.py     #      Google Gemini
│   │   ├── openaiConnections.py     #      OpenAI
│   │   ├── deepseekConnections.py   #      DeepSeek
│   │   └── prompts.py               #      Prompt AI
│   ├── clickers_and_finders.py      #    Automazione click
│   ├── helpers.py                   #    Funzioni helper
│   ├── open_chrome.py               #    Gestione Chrome
│   └── validator.py                 #    Validazione config
│
├── all excels/                      # 📁 Storico candidature
├── all resumes/                     # 📁 CV (default + generati)
│   ├── default/                     #    CV predefinito
│   └── generated/                   #    CV generati dall'AI
├── logs/                            # 📁 File di log
│
├── runAiBot.py                      # 🚀 Script principale
├── app.py                           # 🌐 Interfaccia web (Flask)
└── README.md                        # 📄 Documentazione base
```

---

## Configurazione

### 1. Credenziali LinkedIn (`secrets.py`)

Percorso: `config/secrets.py`

```python
# Credenziali LinkedIn
username = "tua_email@gmail.com"       # Email LinkedIn
password = "tuaPassword123"             # Password LinkedIn

# Abilita AI
use_AI = True                          # True = usa AI, False = no AI

# Seleziona provider AI
ai_provider = "gemini"                 # "gemini", "openai", "deepseek"

# Configurazione API
llm_api_key = "LA_TUA_API_KEY"        # Chiave API del provider scelto
llm_model = "gemini-2.0-flash"        # Modello da usare

# Per OpenAI/compatibili
llm_api_url = "https://api.openai.com/v1/"
llm_spec = "openai"

# Streaming output
stream_output = False                  # True per vedere output in tempo reale
```

#### Provider AI Supportati

| Provider | `ai_provider` | `llm_model` esempi |
|----------|---------------|---------------------|
| **Google Gemini** | `"gemini"` | `"gemini-2.0-flash"`, `"gemini-1.5-flash"`, `"gemini-pro"` |
| **OpenAI** | `"openai"` | `"gpt-4o"`, `"gpt-3.5-turbo"`, `"gpt-4"` |
| **DeepSeek** | `"deepseek"` | `"deepseek-chat"`, `"deepseek-reasoner"` |

---

### 2. Dati Personali (`personals.py`)

Percorso: `config/personals.py`

```python
# Nome completo
first_name = "Giorgio"
middle_name = ""
last_name = "Gnoli"

# Contatti
phone_number = "+393334567890"

# Località
current_city = "Remote"               # Lascia vuoto per usare località del lavoro
street = "Via Roma 1"
state = "Marche"
zipcode = "60100"
country = "Italy"

# Equal Opportunity (USA)
ethnicity = "Decline"                 # Opzioni: "Decline", "Hispanic/Latino", "Asian", etc.
gender = "Decline"                    # "Male", "Female", "Other", "Decline"
disability_status = "Decline"         # "Yes", "No", "Decline"
veteran_status = "Decline"            # "Yes", "No", "Decline"
```

---

### 3. Risposte alle Domande (`questions.py`)

Percorso: `config/questions.py`

```python
# CV predefinito
default_resume_path = "all resumes/default/resume.pdf"

# Esperienza
years_of_experience = "15"            # Anni totali di esperienza

# Visto/Sponsorship
require_visa = "No"                   # "Yes" o "No"

# Link professionali
website = "https://www.linkedin.com/in/tuoprofilo/"
linkedIn = "https://www.linkedin.com/in/tuoprofilo/"

# Cittadinanza
us_citizenship = "Non-citizen allowed to work for any employer"

# Stipendio
desired_salary = 100000               # Stipendio desiderato (numero intero)
current_ctc = 90000                   # Stipendio attuale

# Preavviso
notice_period = 0                     # Giorni di preavviso (0 = disponibile subito)

# Profilo
linkedin_headline = "CRM & CX Leader | Salesforce Expert"

linkedin_summary = """
CRM & CX leader con 15+ anni di esperienza in programmi fedeltà,
trasformazione digitale e leadership di team globali.
"""

cover_letter = """
Gentile Responsabile,

Sono un leader CRM e Customer Experience con 15+ anni di esperienza...

Cordiali saluti,
Giorgio Gnoli
"""

# Informazioni per AI
user_information_all = """
Giorgio Gnoli - CRM & CX Leader con 15+ anni esperienza
Competenze: Salesforce Marketing Cloud, HubSpot, CDP, Loyalty Management
Settori: Automotive, Consumer Goods, Technology, Retail
Lingue: Italiano (madrelingua), Inglese (fluente)
"""

# Comportamento bot
pause_before_submit = False           # True = pausa prima di ogni invio
pause_at_failed_question = False      # True = pausa se non sa rispondere
overwrite_previous_answers = False    # True = sovrascrivi risposte salvate
```

---

### 4. Parametri di Ricerca (`search.py`)

Percorso: `config/search.py`

```python
# Termini di ricerca (lista)
search_terms = [
    "Salesforce contractor UK",
    "Salesforce developer contract UK",
    "Marketing Cloud consultant UK",
]

# Località
search_location = "United Kingdom"    # Paese/città per la ricerca

# Numero candidature per termine
switch_number = 30                    # Candidature prima di passare al prossimo termine

# Ordinamento
randomize_search_order = False        # True = ordine casuale dei termini
sort_by = ""                          # "", "Most recent", "Most relevant"
date_posted = "Past week"             # "", "Any time", "Past month", "Past week", "Past 24 hours"

# Filtri
easy_apply_only = True                # Solo Easy Apply
salary = ""                           # Filtro stipendio (opzionale)

# Tipo di lavoro
experience_level = ["Mid-Senior level", "Director", "Executive"]
job_type = ["Contract"]               # "Full-time", "Part-time", "Contract", etc.
on_site = []                          # "On-site", "Remote", "Hybrid"

# Filtri avanzati
companies = []                        # Lista aziende specifiche
location = []                         # Località aggiuntive
industry = []                         # Settori
job_function = []                     # Funzioni lavorative

# Esclusioni
bad_words = []                        # Parole da evitare nei titoli
about_company_bad_words = []          # Parole da evitare nelle descrizioni azienda
about_company_good_words = []         # Parole preferite

# Esperienza richiesta
current_experience = 15               # Salta lavori che richiedono più esperienza
did_masters = True                    # Hai un Master?
security_clearance = False            # Richiedi security clearance?
```

---

### 5. Impostazioni Bot (`settings.py`)

Percorso: `config/settings.py`

```python
# LinkedIn
close_tabs = False                    # Chiudi tab esterni automaticamente
follow_companies = False              # Segui aziende dopo candidatura

# Modalità continua
run_non_stop = False                  # Esegui fino a stop manuale
alternate_sortby = True               # Alterna ordinamento
cycle_date_posted = True              # Cicla filtro data
stop_date_cycle_at_24hr = True        # Ferma ciclo a 24h

# Percorsi file
generated_resume_path = "all resumes/generated/"
file_name = "all excels/all_applied_applications_history.csv"
failed_file_name = "all excels/all_failed_applications_history.csv"
logs_folder_path = "logs/"

# Performance
click_gap = 1                         # Secondi tra click (max)
run_in_background = False             # Esegui in background
disable_extensions = False            # Disabilita estensioni Chrome
smooth_scroll = False                 # Scroll fluido

# Sicurezza
safe_mode = False                     # Modalità sicura (profilo guest)
stealth_mode = False                  # Anti-bot detection
keep_screen_awake = True              # Mantieni schermo attivo

# AI
showAiErrorAlerts = False             # Mostra alert errori AI
```

---

## Configurazione AI

### Gemini (Google)

1. Vai su [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Crea una nuova API Key
3. Configura in `secrets.py`:

```python
use_AI = True
ai_provider = "gemini"
llm_api_key = "AIza...tua_chiave"
llm_model = "gemini-2.0-flash"        # o "gemini-1.5-flash", "gemini-pro"
```

**Modelli Gemini disponibili:**
| Modello | Descrizione |
|---------|-------------|
| `gemini-2.0-flash` | Veloce, consigliato |
| `gemini-1.5-flash` | Buon bilanciamento |
| `gemini-pro` | Più potente |

---

### OpenAI

1. Vai su [OpenAI Platform](https://platform.openai.com/api-keys)
2. Crea una nuova API Key
3. Configura in `secrets.py`:

```python
use_AI = True
ai_provider = "openai"
llm_api_url = "https://api.openai.com/v1/"
llm_api_key = "sk-...tua_chiave"
llm_model = "gpt-4o"                  # o "gpt-3.5-turbo", "gpt-4"
```

---

### DeepSeek

1. Vai su [DeepSeek Platform](https://platform.deepseek.com/)
2. Crea una nuova API Key
3. Configura in `secrets.py`:

```python
use_AI = True
ai_provider = "deepseek"
llm_api_url = "https://api.deepseek.com/v1"
llm_api_key = "tua_chiave"
llm_model = "deepseek-chat"           # o "deepseek-reasoner"
```

---

## Utilizzo

### Avvio del Bot

```bash
cd ~/Downloads/giorgio/Auto_job_applier_linkedIn
python3 runAiBot.py
```

### Procedura di Login

1. **Chrome si aprirà automaticamente**
2. **Fai login manualmente su LinkedIn** (se richiesto)
3. **Premi INVIO** nella console per continuare
4. **Il bot inizierà** a cercare e candidarsi

### Interfaccia Web (Storico Candidature)

```bash
python3 app.py
```

Apri il browser su `http://localhost:5000` per vedere lo storico.

---

## Output e Log

### File Generati

| File | Descrizione |
|------|-------------|
| `all excels/all_applied_applications_history.csv` | Storico candidature riuscite |
| `all excels/all_failed_applications_history.csv` | Candidature fallite |
| `logs/` | Log dettagliati delle sessioni |
| `all resumes/generated/` | CV generati dall'AI |

### Formato CSV Storico

```csv
Job Title, Company, Location, Applied Date, Job URL, Status
Salesforce Developer, ACME Corp, London, 2026-01-28, https://..., Applied
```

---

## Troubleshooting

### Errore: "Invalid input for ai_provider"

**Causa**: Il validatore non riconosce il provider AI configurato.

**Soluzione**: Assicurati che `ai_provider` in `secrets.py` sia uno di: `"openai"`, `"deepseek"`, `"gemini"`.

---

### Errore: Chrome non si apre

**Possibili cause**:
1. Chrome non installato nella posizione predefinita
2. ChromeDriver non compatibile

**Soluzioni**:
1. Reinstalla Chrome dalla [pagina ufficiale](https://www.google.com/chrome)
2. Imposta `stealth_mode = True` in `settings.py`

---

### Il bot non trova lavori

**Possibili cause**:
1. Filtri troppo restrittivi
2. Termini di ricerca troppo specifici

**Soluzioni**:
1. Amplia i `search_terms`
2. Rimuovi alcuni filtri da `search.py`
3. Cambia `date_posted` in "Any time"

---

### Errore API Gemini

**Possibili cause**:
1. API Key non valida
2. Quota esaurita
3. Modello non disponibile

**Soluzioni**:
1. Verifica la chiave su [Google AI Studio](https://aistudio.google.com/)
2. Controlla i limiti di utilizzo
3. Prova un modello diverso (es. `gemini-1.5-flash`)

---

### Il bot si blocca su una domanda

**Soluzioni**:
1. Imposta `pause_at_failed_question = True` per debug
2. Aggiungi la risposta specifica in `questions.py`
3. Abilita l'AI per risposte automatiche

---

## Disclaimer

> ⚠️ **IMPORTANTE**: Questo programma è solo per scopi educativi.

- Rispetta i [Termini di Servizio di LinkedIn](https://www.linkedin.com/legal/user-agreement)
- L'uso di web scraping potrebbe violare le policy di LinkedIn
- Usa a tuo rischio e pericolo
- Gli sviluppatori non sono responsabili per ban o conseguenze legali

---

## Crediti

- **Autore Originale**: Sai Vignesh Golla ([GitHub](https://github.com/GodsScion))
- **Licenza**: [GNU AGPL v3](LICENSE)
- **Fork/Modifiche**: Giorgio Gnoli (Integrazione Gemini, miglioramenti vari)

---

## Link Utili

- 📖 [README Originale](README.md)
- 💬 [Discord Community](https://discord.gg/fFp7uUzWCY)
- 🐛 [Segnala Bug](https://github.com/GodsScion/Auto_job_applier_linkedIn/issues)
- 🎥 [Video Tutorial](https://youtu.be/f9rdz74e1lM)

---

*Versione Documentazione: 1.0.0 | Ultimo aggiornamento: 28 Gennaio 2026*
