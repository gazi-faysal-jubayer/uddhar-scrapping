import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://ipdibd.com/hospital-list-bangladesh/private-hospital-list/") 

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//tbody")))

    csv_file = "private hospital 3/private-hospital-3-output.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Hospital Name", "Address", "Contact"]) 

        for i in range(2, 95):
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, f"//tbody/tr[{i}]/td[2]")))
                data1 = driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[2]").text
                data2 = driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[3]").text
                data3 = driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[4]").text

                writer.writerow([data1, data2, data3])

            except Exception as e:
                print(f"Error processing row {i}: {e}")
                writer.writerow([f"Error at row {i}", "", ""])

    print(f"Data has been written to {csv_file}")

finally:
    driver.quit()
