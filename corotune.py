from functions import file

class example:
    descr = "Различные примеры функций | https://github.com/ktnk-dev/python_tasks"
    index = True
    baseurl = None

    def _1() -> str: 
        """Это пример функции"""
        return 'Привет, мир'

    def _2(name: str) -> str:
        """Это пример функции в которую можно вписать значение"""
        return f'Привет, {name}'

    def _test() -> bool:
        """В качестве имени функции можно указать любое имя"""
        return True

    def _error() -> int:
        """Это пример функции с ошибкой"""
        return 1+'lol'
    
