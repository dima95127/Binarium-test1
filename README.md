# Trading Helper — Android APK

## Сборка через GitHub Actions (без Linux на ПК)

1. Создай новый репозиторий на GitHub (Public)
2. Загрузи все файлы из архива, сохранив структуру:
   - main.py
   - buildozer.spec
   - icon.png
   - .github/workflows/build.yml
   - README.md
3. Запушь в ветку main — сборка запустится автоматически
4. Открой вкладку Actions → дождись зелёной галочки (30–60 мин)
5. Скачай артефакт trading-helper-apk — внутри готовый .apk

## Сборка через Linux/WSL2

```bash
pip install buildozer cython
buildozer -v android debug
```
APK появится в bin/

## Если сборка падает

В buildozer.spec строка `pure_python_modules = ta,yfinance,multitasking`
уже раскомментирована — ta и yfinance ставятся как чистый Python
без компиляции под ARM.

## Установка на телефон

Перекинь .apk на телефон, открой и разреши установку
из неизвестных источников.
