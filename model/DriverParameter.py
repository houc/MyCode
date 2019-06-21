from config_path.path_file import read_file
from selenium import webdriver

def browser(switch=False):
    """打开浏览器"""
    driver_path = read_file('package', 'ChromeDriver.exe')
    options = webdriver.ChromeOptions()
    options.headless = switch
    drivers = webdriver.Chrome(driver_path, options=options)
    if switch:
        drivers.set_window_size(1900, 980)
    else:
        drivers.maximize_window()
    return drivers

if __name__ == '__main__':
    driver = browser(True)
    driver.get('http://www.ukuaiqi.com')
    driver.save_screenshot(r'D:\work_file\auto_script\UI\img\logo.png')
    driver.quit()
