import unittest

def run_case():
    discover = unittest.defaultTestLoader.discover('./',pattern='*_st.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)

if __name__ == '__main__':
    run_case()