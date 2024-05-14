from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

from src.controller.sendmess import sendmess
from src.model.variables import v


def parsing():
    course = get_currency()
    if course != 'Error':
        v.set_usd(course)
        sendmess("Курс взят: "+str(course)+"")
        print("Курс установлен: ", course)

    else:
        sendmess("Ошибка получения курса: "+course)


def get_currency() -> float:

    """
    Функция получает текущую валюту на веб-странице.
    :return: текущая валюта в виде строки, либо 'error' в случае ошибки
    """
    print("парсим")
    try:
        # Создаем экземпляр WebDriver с использованием Chrome
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')

        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Safari/605.1.15"
        chrome_options.add_argument(f"user-agent={user_agent}")

        driver = webdriver.Chrome(options=chrome_options)

        # Открываем страницу с курсом доллара к батам
        url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=RUB'
        driver.get(url)

        print(driver.title)


        elementCords = driver.execute_script(
    """return(document.querySelectorAll('.sc-1c293993-1')[0].textContent);""")


        driver.quit()
        result = elementCords.replace("Russian Rubles", "")
        return float(result)

    except WebDriverException as e:
        print(f"An error occurred: {e}")
        return 'error'

# print(get_currency())