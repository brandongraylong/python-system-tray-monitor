import psutil, threading, time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from constants import LOGO_PATH


def __get_cpu_stats():
    return str(psutil.cpu_percent(interval=1)) + '% CPU Used'


def __get_mem_str_b_to_gb(bytes_int):
    return "{:.2f}".format(bytes_int / 10**9) + ' GB'


def __get_memory_stats():
    curr_mem = psutil.virtual_memory()

    return __get_mem_str_b_to_gb(curr_mem.used) + ' Used / ' + \
        __get_mem_str_b_to_gb(curr_mem.total) + ' Total Memory'


def __get_storage_stats():
    curr_storage = psutil.disk_usage('/')
    
    return __get_mem_str_b_to_gb(curr_storage.used) + ' Used / ' + \
        __get_mem_str_b_to_gb(curr_storage.total) + ' Total Storage'
    

def __get_network_stats():
    curr_net = psutil.net_io_counters()

    return __get_mem_str_b_to_gb(curr_net.bytes_sent) + ' Sent / ' + \
        __get_mem_str_b_to_gb(curr_net.bytes_recv) + ' Received Network \n' + \
        str(curr_net.dropin) + ' Incoming / ' + \
        str(curr_net.dropout) + ' Outgoing Packets Dropped'


def __update_actions(cpu_percent_action, memory_stat_action,
    storage_stat_action, net_stat_action):
    while True:
        cpu_percent_action.setText(__get_cpu_stats())
        memory_stat_action.setText(__get_memory_stats())
        storage_stat_action.setText(__get_storage_stats())
        net_stat_action.setText(__get_network_stats())


def run_tray_app():
    # Initialize app
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    # Initialize tray icon
    icon = QIcon(LOGO_PATH)

    # Initialize tray with icon
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Initialize the menu
    menu = QMenu()

    # Add actions for stats
    cpu_percent_action = QAction(__get_cpu_stats())
    menu.addAction(cpu_percent_action)

    memory_stat_action = QAction(__get_memory_stats())
    menu.addAction(memory_stat_action)

    storage_stat_action = QAction(__get_storage_stats())
    menu.addAction(storage_stat_action)

    net_stat_action = QAction(__get_network_stats())
    menu.addAction(net_stat_action)
    
    # Add quit action
    quit_action = QAction('Quit')
    quit_action.triggered.connect(app.quit)
    
    # Add quit item to menu
    menu.addAction(quit_action)

    # Add menu to tray
    tray.setContextMenu(menu)

    update_action_th = threading.Thread(
        target=__update_actions, 
        args=(
            cpu_percent_action,
            memory_stat_action,
            storage_stat_action,
            net_stat_action
        ),
        daemon=True
    )
    update_action_th.start()
    
    app.exec_()


def main():
    run_tray_app()    


if __name__ == "__main__":
    main()
