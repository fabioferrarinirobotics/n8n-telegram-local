🤖 Telegram AI Bot - 100% Locale (n8n + Ollama + Docker)

Questo progetto implementa un Assistente AI completo su Telegram che gira interamente sul tuo computer (Windows 11).

🌟 Caratteristiche
- Privacy Totale: Nessun dato lascia la tua rete locale.
- Costo Zero: Nessuna API key a pagamento (niente OpenAI).
- AI Locale: Utilizza la potenza di Ollama (Llama 3, DeepSeek, Qwen).
- Architettura Docker: Tutto è containerizzato per una gestione pulita.
- Bridge Python: Script personalizzato per gestire la comunicazione con Telegram senza   necessità di HTTPS o certificati complessi.

🛠️ 1. Prerequisiti (Installazione da Zero)
Prima di iniziare, assicurati di avere installato i seguenti software sul tuo computer Windows 11.


🔹 A. Ollama (Il Cervello AI)
   Il software che esegue i modelli di linguaggio (LLM) in locale.

   Scarica e installa da: ollama.com

   Una volta installato, apri il Terminale (PowerShell o CMD) e scarica il modello:

   PowerShell
   ollama pull llama3.2
   (Puoi scaricare altri modelli, ma assicurati di aggiornare poi il nodo in n8n).

🔹 B. Docker Desktop (Il Motore)
   Necessario per eseguire n8n, il database e il bridge Python.

   Scarica e installa da: docker.com/products/docker-desktop

   Importante: Durante l'installazione, assicurati che sia selezionata l'opzione "Use WSL 2 instead of Hyper-V" (è lo standard per Windows 11).

   Dopo l'avvio, attendi che l'icona della balena in basso a destra diventi verde.

🔹 C. Visual Studio Code (Editor)
    L'ambiente di sviluppo consigliato.
    Scarica e installa da: code.visualstudio.com
 
    Durante l'installazione, spunta l'opzione "Add to PATH".



🚀 2. Installazione del Progetto


# Passo 1: Clona il Repository

Apri il terminale, naviga nella cartella dove vuoi salvare il progetto ed esegui:

```bash
git clone https://github.com/TUO_USERNAME/n8n-telegram-local.git
cd n8n-telegram-local
```

## Passo 2: Come ottenere il Token Telegram (Guida @BotFather)

Per far funzionare il tuo bot, devi registrarlo ufficialmente sui server di Telegram. Non preoccuparti, è gratis e richiede 30 secondi.

# 1. Trova il "Padre dei Bot"
Apri l'app di Telegram (sul telefono o sul PC).

Nella barra di ricerca in alto, scrivi: @BotFather.

Clicca sul primo risultato che ha la spunta blu ✅ di verifica (è il bot ufficiale di Telegram).

# 2. Crea il nuovo Bot
Una volta aperta la chat, clicca sul tasto Avvia (o Start) in basso.

Scrivi (o clicca) il comando:

Plaintext
/newbot
BotFather ti risponderà: "Alright, a new bot. How are we going to call it?".

# 3. Scegli il Nome (Display Name)
Cosa scrivere: Il nome che vuoi che le persone vedano nella lista chat (es. "Il Mio Assistente AI", "MarioGPT", "Jarvis").

Regole: Puoi usare spazi, emoji e lettere maiuscole.

Esempio: Super AI Locale 🤖

# 4. Scegli l'Username (ID Univoco)
BotFather ti chiederà ora un username.

Cosa scrivere: Un identificativo unico per il tuo bot (quello che si usa per cercarlo con la @).

Regole:
Deve essere tutto attaccato (niente spazi).
Deve finire obbligatoriamente con la parola bot.
Esempio valido: mio_super_ai_bot oppure MioAiLocalebOt.
Esempio non valido: mio super ai (ha spazi e manca 'bot').

Nota: Se l'username è già preso, BotFather ti dirà "Sorry, this username is already taken". Riprova aggiungendo dei numeri o cambiando nome (es. mio_super_ai_99_bot).

# 5. Copia il Token
Se tutto è andato a buon fine, BotFather ti scriverà un messaggio che inizia con "Done! Congratulations on your new bot".

Cerca la riga che dice: Use this token to access the HTTP API:

Sotto vedrai una stringa lunga di numeri e lettere, simile a questa: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz

Copia interamente questa stringa.

# 6. Incollala nel tuo file .env alla voce TELEGRAM_BOT_TOKEN.

⚠️ Attenzione alla Sicurezza
Non condividere mai questo token con nessuno. Chi possiede il token può controllare il tuo bot.

Se per sbaglio lo condividi, torna su BotFather e usa il comando /revoke per cancellarlo e ottenerne uno nuovo.



Passo 2: Configura le Variabili d'Ambiente (.env)
Crea un file chiamato .env nella cartella principale del progetto e incolla il seguente contenuto. NOTA: Devi inserire il tuo Token Telegram ottenuto da @BotFather.

Ini, TOML
# .env file configuration

# Credenziali Database (Default)
POSTGRES_USER=n8n
POSTGRES_PASSWORD=n8n_password
POSTGRES_DB=n8n

# Sicurezza n8n (Puoi generare stringhe casuali)
N8N_ENCRYPTION_KEY=chiave_segreta_molto_lunga_random
N8N_USER_MANAGEMENT_JWT_SECRET=altra_chiave_segreta_random

# IL TUO TOKEN TELEGRAM (Obbligatorio)
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz




▶️ 3. Avvio del Sistema
Assicurati che Docker Desktop sia aperto e in esecuzione.

Apri il terminale nella cartella del progetto.

Esegui il comando per costruire e avviare i container:

PowerShell
docker-compose up -d
Docker scaricherà le immagini necessarie (Postgres, n8n) e costruirà il container Python personalizzato. Attendi qualche minuto.

⚙️ 4. Configurazione Workflow (n8n)
Una volta avviato Docker, devi configurare il cervello del bot.

Apri il browser e vai su: http://localhost:5678

Crea il tuo account amministratore locale.

Importa il Workflow:

Clicca su "Add Workflow" (in alto a destra).

Clicca sui tre puntini ... -> Import from File.

Seleziona il file JSON del workflow incluso in questo progetto.

Configura il nodo Ollama (se necessario):

Assicurati che il Base URL sia impostato su: http://host.docker.internal:11434

Assicurati che il Model Name sia: llama3.2

⚠️ PASSAGGIO CRITICO: ATTIVAZIONE
Affinché il bot funzioni, DEVI ATTIVARE il workflow.

Clicca su Save (o Publish) in alto a destra.

Sposta l'interruttore Active su ON (Deve diventare VERDE).

Se l'interruttore non è verde, il bot risponderà con errore 404.

🐞 5. Comandi di Debug
Se il bot non risponde, usa questi comandi nel terminale per capire cosa succede.

A. Controllare se il messaggio arriva (Python Bridge)
Questo log ti mostra se Telegram sta comunicando con il tuo PC.

PowerShell
docker logs -f telegram-bridge
Cosa cercare:

📩 Nuovo messaggio: Il messaggio è arrivato.

✅ Risposta consegnata: Tutto ok.

Error 404: Il workflow su n8n è spento o l'URL è sbagliato.

Connection Refused: n8n non è raggiungibile.

B. Controllare perché l'AI non risponde (n8n Executions)
Se il messaggio arriva ma l'AI non risponde:

Vai su n8n (localhost:5678).

Clicca sull'icona Executions nella barra laterale sinistra.

Clicca sull'ultima esecuzione (quella rossa o verde) per vedere il percorso dei dati e l'errore specifico.

C. Riavvio forzato (in caso di aggiornamenti)
Se modifichi il codice Python o il file .env, devi ricreare i container:

PowerShell
docker-compose down
docker-compose up -d --build
📝 Note Tecniche
Rete Docker: Lo script Python utilizza http://host.docker.internal:5678 per comunicare con n8n. Questo permette al container di "uscire" e parlare con l'host Windows.

Persistenza: I dati di n8n e del database sono salvati in volumi Docker persistenti (n8n_data, postgres_storage), quindi non perderai i tuoi workflow riavviando il PC.

Modelli: Se n8n riporta "model not found", verifica di aver scaricato il modello corretto con ollama list nel terminale di Windows.