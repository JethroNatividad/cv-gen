from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import json

options = Options()

options.set_preference(
    "browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/octet-stream"
)
options.set_preference("pdfjs.disabled", True)  # disable built-in pdf viewer
driver = webdriver.Firefox(options=options)

driver.get("https://resumave.vercel.app/edit?tab=personalInfo")

driver.implicitly_wait(2)

with open("jobs.json", "r") as f:
    jobs = json.load(f)
    for job in jobs:
        job_str = json.dumps(job)

        driver.execute_script(
            f"localStorage.setItem('resume-storage', JSON.stringify({job_str}))"
        )

        driver.refresh()
        resume_name = (
            job["state"]["personalInfo"]["name"].replace(" ", "_") + "_Resume.pdf"
        )

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f'a[download="{resume_name}"]')
            )
        )

        driver.find_element(By.CSS_SELECTOR, f'a[download="{resume_name}"]').click()
driver.quit()
