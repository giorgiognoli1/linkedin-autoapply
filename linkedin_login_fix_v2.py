from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def fix_linkedin_login(driver, username, password, max_attempts=3):
    try:
        time.sleep(3)
        try:
            accedi_button = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accedi') or contains(@class, 'sign-in')]"))
            )
            print("⚠️ Login popup rilevato! Procedo con login automatico...")
            time.sleep(1)
            accedi_button.click()
            time.sleep(3)
        except TimeoutException:
            print("✅ Nessun popup di login rilevato")
            return True
        
        attempt = 0
        while attempt < max_attempts:
            attempt += 1
            try:
                print(f"🔐 Tentativo di login {attempt}/{max_attempts}...")
                username_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "username"))
                )
                username_field.clear()
                username_field.send_keys(username)
                time.sleep(1)
                password_field = driver.find_element(By.ID, "password")
                password_field.clear()
                password_field.send_keys(password)
                time.sleep(1)
                login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
                login_button.click()
                time.sleep(5)
                try:
                    error_element = driver.find_element(By.XPATH, "//*[contains(@class, 'error') or contains(@class, 'alert')]")
                    if error_element.is_displayed():
                        print(f"❌ Login fallito (tentativo {attempt})")
                        if attempt < max_attempts:
                            continue
                        else:
                            return False
                except NoSuchElementException:
                    print("✅ Login completato!")
                    return True
            except Exception as e:
                print(f"⚠️ Errore: {str(e)}")
                if attempt >= max_attempts:
                    return False
                time.sleep(2)
        return False
    except Exception as e:
        print(f"⚠️ Login fix: {str(e)}")
        return True
