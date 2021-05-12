# Предварительный просмотр файлов для конфигураций 1С

Проект реализует предварительный просмотр файлов для конфигураций на платформе 1С. 

## Основные возможности

* Просмотр файлов в HTML-поле форм. Реализовано с помощью библиотеки [ViewerJS](https://viewerjs.org/) . Для просмотра файлов на стороне 1С не требуется установка допонительных компонентов.
* Конвертация файлов между форматами, поддеживаемыми [LibreOffice](https://www.libreoffice.org/). Реализовано с помощью библиотеки [unoconv](https://github.com/unoconv/unoconv)
* Настройка формата для конвертации файла на стороне приложения 1С (например docx-файл, можно конвертировать как в pdf, так и в odt)
  

### Необходимые компоненты

* Python 3.9.1 и выше (ниже не тестировалось)
* [WSL 2](https://docs.microsoft.com/ru-ru/windows/wsl/install-win10) и [Docker Desktop](https://docs.docker.com/docker-for-windows/install/) для запуска в контейнере в Windows
* [LibreOffice](https://www.libreoffice.org/)
* [ViewerJS](https://viewerjs.org/)
* [unoconv](https://github.com/unoconv/unoconv)
* Платформа 1С:Предприятия 8.3.18 и выше (https://releases.1c.ru/project/Platform83)
* СУБД, поддерживаемая 1С:Предприятием
* OS Windows 7 или выше, ОС Linux.

### Сборка и установка проекта

Выполните команды в Linux:


Выполните команды в Windows, указав корректный путь к версии 1С:
