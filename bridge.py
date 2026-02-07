import os
import requests
import time
import sys

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
N8N_URL = os.getenv("N8N_WEBHOOK_URL")

def log(message):
    print(f"[DEBUG] {time.strftime('%H:%M:%S')} - {message}")
    sys.stdout.flush()

def send_to_telegram(chat_id, text):
    log(f"Inviando risposta a Telegram (Chat ID: {chat_id})...")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    res = requests.post(url, json={"chat_id": chat_id, "text": text})
    if res.status_code == 200:
        log("✅ Risposta consegnata con successo.")
    else:
        log(f"❌ Errore Telegram: {res.text}")

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        r = requests.get(url, params={"timeout": 10, "offset": offset}, timeout=15)
        return r.json()
    except Exception as e:
        log(f"❌ Errore Polling: {e}")
        return None

log("🚀 Bridge Python avviato. In attesa di messaggi...")

last_update_id = None
while True:
    updates = get_updates(last_update_id)
    if updates and "result" in updates:
        for update in updates["result"]:
            last_update_id = update["update_id"] + 1
            if "message" in update and "text" in update["message"]:
                chat_id = update["message"]["chat"]["id"]
                user_text = update["message"]["text"]
                
                log(f"📩 Nuovo messaggio da Telegram: '{user_text}'")

                try:
                    log(f"🔗 Chiamata a n8n in corso...")
                    res = requests.post(N8N_URL, json={"message": user_text, "chat_id": chat_id})
                    
                    if res.status_code == 200:
                        data = res.json()
                        # n8n restituisce spesso una lista, gestiamola
                        if isinstance(data, list): data = data[0]
                        
                        # Cerchiamo il campo 'output' che n8n deve restituire
                        bot_answer = data.get("output") or data.get("response") or "n8n ha risposto ma non trovo il testo."
                        log(f"🤖 Risposta ricevuta da n8n: '{bot_answer[:30]}...'")
                        
                        # REINVIA A TELEGRAM
                        send_to_telegram(chat_id, bot_answer)
                    else:
                        log(f"⚠️ Errore n8n (Codice {res.status_code}): {res.text}")
                except Exception as e:
                    log(f"❌ Errore nel bridge verso n8n: {e}")
    time.sleep(1)