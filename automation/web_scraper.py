"""Simple web scraper that fetches content from a page and saves questions to CSV."""

import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def scrape_with_requests(url):
    """Fetch a page using the requests library and return its HTML."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    print("Failed to retrieve the webpage.")
    return None


def extract_questions(html_content):
    """Return all question texts found in a page using BeautifulSoup."""
    soup = BeautifulSoup(html_content, "html.parser")
    questions = soup.find_all("div", class_="question")
    return [question.get_text() for question in questions]


def save_to_csv(data):
    """Save scraped question text to a CSV file."""
    df = pd.DataFrame(data, columns=["Questions"])
    df.to_csv("questions.csv", index=False)
    print("Data saved to questions.csv")


def scrape_with_selenium(url):
    """Fallback scraper using Selenium for JavaScript-heavy pages."""
    options = Options()
    options.add_argument("--headless")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(10)

    questions = driver.find_elements(By.CLASS_NAME, "question")
    extracted_questions = [question.text for question in questions]
    driver.quit()
    return extracted_questions


def main():
    """Prompt the user for a URL and scrape questions from the page."""
    url = input("Enter a URL: ")

    html_content = scrape_with_requests(url)
    if html_content:
        questions = extract_questions(html_content)
    else:
        questions = scrape_with_selenium(url)

    if questions:
        print("Extracted Questions:")
        for question in questions:
            print(question)

        save_to_csv(questions)


if __name__ == "__main__":
    main()
