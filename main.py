from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


driver = webdriver.Firefox()
driver.get("https://resumave.vercel.app/edit?tab=personalInfo")

driver.implicitly_wait(2)

with open("job.json", "r") as f:
    new = json.load(f)

    job = json.dumps(new)

    driver.execute_script(
        f"localStorage.setItem('resume-storage', JSON.stringify({job}))"
    )
    driver.refresh()
    # Wait for a tag that has download="Arjun_Mehta_Resume.pdf" (new.name replace space with _ and add _Resume.pdf at the end)
    resume_name = new["state"]["personalInfo"]["name"].replace(" ", "_") + "_Resume.pdf"
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, f'a[download="{resume_name}"]')
        )
    )
    # Click on the tag
    driver.find_element(By.CSS_SELECTOR, f'a[download="{resume_name}"]').click()
