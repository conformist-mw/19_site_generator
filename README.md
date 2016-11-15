# 19 Site generator

Данный скрипт может конвертировать файлы с разметкой markdown в html и создаёт статический сайт с базовой вёрсткой (применяется bootstrap). [Здесь](https://conformist-mw.github.io/19_site_generator/site/index.html) можно ознакомиться с примером такого сайта. 

Структура сайта задаётся конфиг-файлом в формате json, его нужно указать при запуске скрипта. 

## Запуск скрипта

Традиционно для запуска нужно установить необходимые зависимости, которые перечислены в файле requirements.txt, например так:

:::python
pip3 install -r requirements.txt
:::
И после этого:
:::bash
python3 site_generator.py config.json
:::
