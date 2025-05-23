import argparse
from .port_scanner import PortScanner
from .sql_injection import SQLInjectionTester

def main():
    parser = argparse.ArgumentParser(
        description='Air-GC - инструмент для проверки портов и SQL-инъекций'
    )
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Парсер для сканирования портов
    port_parser = subparsers.add_parser('scan-ports', help='Сканирование портов')
    port_parser.add_argument('target', help='Целевой хост или IP-адрес')
    port_parser.add_argument(
        '--range', 
        help='Диапазон портов (например, 1-1000)',
        default=None
    )
    port_parser.add_argument(
        '--common', 
        help='Сканировать только распространенные порты',
        action='store_true'
    )
    
    # Парсер для тестирования SQL-инъекций
    sql_parser = subparsers.add_parser('test-sql', help='Тестирование SQL-инъекций')
    sql_parser.add_argument('url', help='Целевой URL')
    
    args = parser.parse_args()
    
    if args.command == 'scan-ports':
        scanner = PortScanner(args.target)
        
        if args.common:
            print(f"Сканирование распространенных портов на {args.target}...")
            open_ports = scanner.scan_common_ports()
        elif args.range:
            start, end = map(int, args.range.split('-'))
            print(f"Сканирование портов {start}-{end} на {args.target}...")
            open_ports = scanner.scan_range(start, end)
        else:
            print("Не указан диапазон портов или флаг --common")
            return
        
        print("\nОткрытые порты:")
        for port in sorted(open_ports.keys()):
            print(f"  - {port}")
    
    elif args.command == 'test-sql':
        tester = SQLInjectionTester(args.url)
        print(f"Тестирование SQL-инъекций на {args.url}...")
        vulnerabilities = tester.test_get_parameters()
        
        if vulnerabilities:
            print("\nНайдены потенциальные уязвимости:")
            for url, params in vulnerabilities.items():
                print(f"  - URL: {url}")
                print(f"    Уязвимые параметры: {', '.join(params)}")
        else:
            print("\nУязвимости не обнаружены")