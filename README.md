# Предварительный просмотр файлов для конфигураций 1С

Проект реализует предварительный просмотр файлов для конфигураций на платформе 1С. Проект состоит из 2-х компонентов: 
- подсистемы на **платформе 1С** (1cApp) 
- веб-приложение для просмотра и конвертации файлов на **python** (PreviewerWebApp).

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

#### Сборка и установка PreviewerWebApp

Установка с использованием [Docker](https://www.docker.com/):
```bash
git clone https://github.com/alz-34/FilesPreviewFor1C.git .
docker-compose up -d
```

По умолчанию приложение будет доступно на стандартном порту **5000** flask-приложения. Проверить работу приложения:
```
http://localhost:5000/test
```
Авторизации приложения не требует.

Все файлы, которые приложение хранит у себя для отображения, монтируются с помощью [Docker Volumes](https://docs.docker.com/storage/volumes/) на host-машине. По умолчанию для Windows это:
```
\\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes\
```

#### Сборка и установка 1cApp

Сборка из исходников в Windows. Необходимо указать корректный путь к версии 1С:
```cmd
git clone https:/github.com/alz-34/FilesPreviewFor1C.git
"C:\Program files\1cv8\8.3.18.1208\bin\1cv8" CREATEINFOBASE File=%CD%/db
"C:\Program files\1cv8\8.3.18.1208\bin\1cv8" DESIGNER /WA- /DisableStartupDialogs /IBConnectionString File="%CD%/db" /LoadConfigFromFiles "%CD%/1cApp/src" /UpdateDBCfg
"C:\Program files\1cv8\8.3.18.1208\bin\1cv8" DESIGNER /WA- /DisableStartupDialogs /IBConnectionString File="%CD%/db" /CreateDistributionFiles -cffile "%CD%/1cv8.cf"
```

Либо скачать артефакт из раздела с [релизами](https://github.com/alz-34/FilesPreviewFor1C/releases).

СF следует использовать как демо, либо интегрировать как подсистему в целевую систему на платформе 1С.