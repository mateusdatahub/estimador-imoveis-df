# scrape_dfimoveis_save_per_page.py
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# ---------------------- CONFIG ----------------------
URL = "https://www.dfimoveis.com.br/venda/df/todos/imoveis"
OUT_DIR = r"C:\analise_imoveis\data\raw"
OUT_CSV = os.path.join(OUT_DIR, "imoveis_dfimoveis.csv")
os.makedirs(OUT_DIR, exist_ok=True)
TIME_SLEEP = 10  # segundos de espera por página
# -----------------------------------------------------

# Inicializa driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(URL)
time.sleep(TIME_SLEEP)  # espera carregar a página inicial

# Lista para armazenar os dados
imoveis = []

pagina_atual = 1
while True:
    print(f"Raspando página {pagina_atual}...")

    # Scroll até o final para carregar todos os imóveis
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(TIME_SLEEP)  # espera os cards carregarem

    # Coleta todos os cards de imóveis
    cards = driver.find_elements(By.CSS_SELECTOR, "a.imovel-card")
    print(f"Encontrados {len(cards)} imóveis nesta página.")

    for card in cards:
        try:
            titulo = card.find_element(By.CSS_SELECTOR, "h2").text
        except:
            titulo = None
        try:
            preco = card.find_element(By.CSS_SELECTOR, "div.imovel-price h4 span").text
        except:
            preco = None
        try:
            area = card.find_element(By.CSS_SELECTOR, "div.imovel-feature div:nth-child(1)").text
        except:
            area = None
        try:
            quartos = card.find_element(By.CSS_SELECTOR, "div.imovel-feature div:nth-child(2)").text
        except:
            quartos = None
        try:
            link = card.get_attribute("href")
        except:
            link = None

        imoveis.append({
            "titulo": titulo,
            "preco": preco,
            "area": area,
            "quartos": quartos,
            "link": link
        })

    # Salva CSV a cada página
    df = pd.DataFrame(imoveis)
    df.to_csv(OUT_CSV, index=False, encoding="utf-8-sig")
    print(f"CSV atualizado com {len(df)} imóveis até agora.\n")

    # Tenta clicar no botão "Próximo"
    try:
        btn_prox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.next"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(btn_prox).perform()
        time.sleep(2)
        btn_prox.click()
        pagina_atual += 1
        time.sleep(TIME_SLEEP)  # espera nova página carregar
    except TimeoutException:
        print("Fim das páginas!")
        break

# Fecha o navegador
driver.quit()

print(f"Raspagem concluída! {len(df)} imóveis salvos em {OUT_CSV}")
