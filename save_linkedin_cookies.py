"""
Script per salvare i cookie di LinkedIn dopo il login manuale
"""
import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("\n🔐 SCRIPT LOGIN LINKEDIN - SALVATAGGIO COOKIE\n")
print("Questo script:")
print("1. Apre Chrome")
print("2. Ti porta su LinkedIn")
print("3. TU fai login manualmente")
print("4. I cookie vengono salvati automaticamente")
print("5. Il bot userà questi cookie per rimanere loggato\n")

input("Premi INVIO per iniziare...")

# Configura Chrome
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Vai su LinkedIn
print("\n✅ Apro LinkedIn...")
driver.get("https://www.linkedin.com")

print("\n⏳ FAI LOGIN MANUALMENTE ORA!")
print("Inserisci email: giorgiognoli@gmail.com")
print("Inserisci password: AnconaNumanaSirolo!25")
print("\nQuando hai completato il login e vedi la tua home di LinkedIn...")

input("\nPremi INVIO dopo aver fatto login...")

# Salva i cookie
cookies = driver.get_cookies()
with open('/Users/giorgio/Downloads/giorgio/Auto_job_applier_linkedIn/linkedin_cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

print("\n✅ Cookie salvati in: linkedin_cookies.pkl")
print("✅ Il bot userà questi cookie per rimanere loggato!")

driver.quit()
print("\n🎉 Setup completato! Ora puoi eseguire: python3 runAiBot.py")
