# network.py

import psutil
import socket
import traceback

def is_suspicious_connection(remote_ip):

    if not remote_ip:
        return False
    if remote_ip.startswith("127.") or remote_ip == "0.0.0.0" or remote_ip.startswith("192.168.") or remote_ip.startswith("10."):
        return False
    return True

def analyze_network(file_path):
    suspicious = []

    try:
        connections = psutil.net_connections(kind='inet')

        for conn in connections:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr_ip = conn.raddr.ip if conn.raddr else None
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            status = conn.status
            pid = conn.pid

            proc_name = "unknown"
            try:
                if pid:
                    proc = psutil.Process(pid)
                    proc_name = proc.name()
            except Exception:
                pass

            if is_suspicious_connection(raddr_ip):
                suspicious.append({
                    "local": laddr,
                    "remote": raddr,
                    "status": status,
                    "pid": pid,
                    "process": proc_name
                })

        return {
            "status": f"Анализировано {len(connections)} соединений",
            "suspicious_connections": suspicious
        }

    except Exception as e:
        return {
            "status": "Ошибка при анализе сети",
            "error": repr(e),  # Лучше, чем str(e)
            "suspicious_connections": []
        }
