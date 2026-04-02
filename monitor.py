import sqlite3
import socket
import time
from datetime import datetime

# 配置你要监控的服务列表 (IP/域名, 端口, 服务名称)
SERVICES = [
    ("1.1.1.1", 53, "Public DNS"),
    ("127.0.0.1", 22, "Local SSH"),
    # 可以随时替换成你自己的节点或管理面板地址
]

DB_NAME = "uptime.db"

def init_db():
    """初始化 SQLite 数据库"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS status_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            service_name TEXT,
            host TEXT,
            port INTEGER,
            is_online BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()

def check_port(host, port, timeout=3):
    """检测指定 IP 和端口是否连通"""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, socket.error):
        return False

def log_status(service_name, host, port, is_online):
    """将结果写入数据库"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO status_log (timestamp, service_name, host, port, is_online)
        VALUES (?, ?, ?, ?, ?)
    ''', (datetime.now(), service_name, host, port, is_online))
    conn.commit()
    conn.close()

def main():
    init_db()
    print(f"[{datetime.now()}] Starting monitoring cycle...")
    
    for host, port, name in SERVICES:
        is_online = check_port(host, port)
        status_text = "ONLINE" if is_online else "OFFLINE"
        print(f" - {name} ({host}:{port}) is {status_text}")
        log_status(name, host, port, is_online)

if __name__ == "__main__":
    main()
