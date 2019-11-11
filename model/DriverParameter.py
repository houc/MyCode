from config_path.path_file import read_file
from selenium import webdriver
from model.Logs import logger


def browser(switch=False):
    driver_path = read_file('package', 'ChromeDriver.exe')
    options = webdriver.ChromeOptions()
    options.headless = switch
    method = '无头模式打开浏览器' if switch else '有头模式打开浏览器'
    logger.info(f'打开浏览器，采用->{method}')
    drivers = webdriver.Chrome(driver_path, options=options)
    if switch:
        drivers.set_window_size(1900, 980)
    else:
        drivers.maximize_window()
    return drivers


