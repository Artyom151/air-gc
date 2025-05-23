# Air-GC

Инструмент для проверки портов и уязвимостей SQL-инъекций.

## Установка

```bash
pip install air-gc
```
# Использование

## Сканирование портов
```bash
# Сканирование распространенных портов
air-gc scan-ports example.com --common
```
```bash
# Сканирование диапазона портов
air-gc scan-ports example.com --range 1-1000
```
```bash
# Тестирование SQL-инъекций
air-gc test-sql http://example.com
```