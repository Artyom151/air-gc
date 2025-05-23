"""Air-GC - инструмент для проверки портов и уязвимостей SQL-инъекций"""
from .port_scanner import PortScanner
from .sql_injection import SQLInjectionTester
from .cli import main

__version__ = '0.1.0'
__all__ = ['PortScanner', 'SQLInjectionTester', 'main']