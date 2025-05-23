import socket
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict

class PortScanner:
    """Класс для сканирования открытых портов на хосте"""
    
    def __init__(self, target: str, timeout: float = 1.0):
        self.target = target
        self.timeout = timeout
        self.common_ports = [
            21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 
            443, 445, 587, 993, 995, 1433, 3306, 3389, 5432,
            8080, 8443
        ]
    
    def scan_port(self, port: int) -> bool:
        """Проверяет, открыт ли указанный порт"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                result = s.connect_ex((self.target, port))
                return result == 0
        except:
            return False
    
    def scan_common_ports(self) -> Dict[int, bool]:
        """Сканирует список распространенных портов"""
        open_ports = {}
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            results = executor.map(self.scan_port, self.common_ports)
            
            for port, is_open in zip(self.common_ports, results):
                if is_open:
                    open_ports[port] = True
        
        return open_ports
    
    def scan_range(self, start_port: int, end_port: int) -> Dict[int, bool]:
        """Сканирует диапазон портов"""
        open_ports = {}
        ports = range(start_port, end_port + 1)
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            results = executor.map(self.scan_port, ports)
            
            for port, is_open in zip(ports, results):
                if is_open:
                    open_ports[port] = True
        
        return open_ports