import requests
from bs4 import BeautifulSoup

def get_soup() -> BeautifulSoup:
    resp = requests.get("https://www.placetel.de/blog/buchstabieren-am-telefon-buchstaben-alphabet")
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup

def extract_alphabet(soup: BeautifulSoup) -> dict:
    div_element = soup.find("div", class_="content-body")
    liste = div_element.find_all("li")[0:29]

    alphabet = {}
    for item in liste:
        alphabet[item.get_text()[0]] = item.get_text().split(" wie ")[1].strip()

    return alphabet


if __name__ == "__main__":
    print(extract_alphabet(get_soup()))