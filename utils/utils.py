import os
import sqlite3
import logging

def clear_console():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

def print_banner():
    banner = r'''
    _    _   _  ___  __  __ _____    _____ ____      _    ____ _  __ _____ ____ 
   / \  | \ | ||_ _||  \/  | ____|  |_   _|  _ \    / \  / ___| |/ /| ____|  _ \ 
  / _ \ |  \| | | | | |\/| |  _|      | | | |_) |  / _ \| |   | ' / |  _| | |_) |
 / ___ \| |\  | | | | |  | | |___     | | |  _ <  / ___ \ |___| . \ | |___|  _ < 
/_/   \_\_| \_||___||_|  |_|_____|    |_| |_| \_\/_/   \_\____|_|\_\|_____|_| \_\
    '''
    print(banner)

def init_db():
    connection = sqlite3.connect('./data/database.sqlite')
    with open('./data/schema.sql', 'r') as schema:
        connection.executescript(schema.read())
    connection.commit()
    connection.close()

def init_logs():
    filename = './logs/error.log'
    logging.basicConfig(filename=filename, level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')