# JWT Key Generator / Генератор JWT Ключей

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Version](https://img.shields.io/badge/Version-2.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Security](https://img.shields.io/badge/Security-Testing_Only-red.svg)

## 🇺🇸 English

### 🚀 Overview
**JWT Key Generator** - Advanced Python tool for secure JWT key generation with interactive control panel and extensive configuration options. Perfect for development, testing, and educational purposes.

### ✨ Features
- 🎛️ **Interactive Control Panel** - User-friendly terminal interface
- ⚙️ **Configurable Settings** - Customizable key generation parameters
- 🔑 **Multiple Algorithms** - HMAC, RSA, and ECDSA support
- 📁 **Smart File Management** - Organized output with timestamps
- 🎫 **Token Testing** - Generate and verify JWT tokens
- 💾 **Configuration Profiles** - Save and load settings
- 🔒 **Security Focused** - Secure random generation

### 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Control Panel (RECOMMENDED)
python panel.py

# Or use generator directly
python jwtgen.py --help

# Generate specific key types
python jwtgen.py --hmac-only
python jwtgen.py --rsa-only
python jwtgen.py --ec-only
```

### 🎛️ Control Panel Usage
1. **Launch**: `python panel.py`
2. **Configure**: Set algorithms, key sizes, output directory
3. **Generate**: Start key generation with one click
4. **Results**: Keys saved in organized folder structure

### 📁 Generated Files
```
generated_keys/
├── jwt_keys_hmac_20231201_143022.json
├── jwt_keys_rsa_private_20231201_143022.pem
├── jwt_keys_rsa_public_20231201_143022.pem
├── jwt_keys_ec_private_20231201_143022.pem
├── jwt_keys_ec_public_20231201_143022.pem
└── jwt_keys_example_20231201_143022.json
```

### ⚠️ Security Notice
> **CRITICAL**: This tool is for **DEVELOPMENT & TESTING** only. 
> - 🔒 Never use generated keys in production
> - 🔑 Store secrets securely  
> - 🚫 Never commit generated keys to version control

---

## 🇷🇺 Русский

### 🚀 Обзор
**JWT Key Generator** - Продвинутый Python инструмент для безопасной генерации JWT ключей с интерактивной панелью управления и расширенными настройками. Идеален для разработки, тестирования и обучения.

### ✨ Возможности
- 🎛️ **Интерактивная панель управления** - Удобный терминальный интерфейс
- ⚙️ **Настраиваемые параметры** - Гибкая конфигурация генерации
- 🔑 **Множество алгоритмов** - Поддержка HMAC, RSA и ECDSA
- 📁 **Умное управление файлами** - Организованный вывод с временными метками
- 🎫 **Тестирование токенов** - Генерация и верификация JWT токенов
- 💾 **Профили конфигурации** - Сохранение и загрузка настроек
- 🔒 **Безопасность** - Защищенная случайная генерация

### 🚀 Быстрый старт

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск панели управления (РЕКОМЕНДУЕТСЯ)
python panel.py

# Или использование генератора напрямую
python jwtgen.py --help

# Генерация конкретных типов ключей
python jwtgen.py --hmac-only
python jwtgen.py --rsa-only
python jwtgen.py --ec-only
```

### 🎛️ Использование панели управления
1. **Запуск**: `python panel.py`
2. **Настройка**: Выбор алгоритмов, размеров ключей, папки сохранения
3. **Генерация**: Запуск генерации ключей в один клик
4. **Результаты**: Ключи сохраняются в организованную структуру папок

### 📁 Генерируемые файлы
```
generated_keys/
├── jwt_keys_hmac_20231201_143022.json
├── jwt_keys_rsa_private_20231201_143022.pem
├── jwt_keys_rsa_public_20231201_143022.pem
├── jwt_keys_ec_private_20231201_143022.pem
├── jwt_keys_ec_public_20231201_143022.pem
└── jwt_keys_example_20231201_143022.json
```

### ⚠️ Важное предупреждение
> **ВАЖНО**: Этот инструмент только для **РАЗРАБОТКИ & ТЕСТИРОВАНИЯ**.
> - 🔒 Никогда не используйте ключи в продакшене
> - 🔑 Храните секреты в безопасном месте
> - 🚫 Не коммитьте сгенерированные ключи в репозиторий

## 📄 License / Лицензия
MIT License - see LICENSE file for details / MIT Лицензия - подробности в файле LICENSE

## 🔧 Requirements / Зависимости

```txt
pyjwt>=2.0.0
cryptography>=3.0
```

## 🐛 Issue Reporting / Сообщение об ошибках
If you find any issues, please create an issue in the GitHub repository.  
Если вы нашли ошибки, пожалуйста, создайте issue в репозитории GitHub.

## 📁 Project Structure / Структура проекта
```
jwt-gen/
├── panel.py             # 🎛️ Main control panel / Основная панель управления
├── jwtgen.py            # 🔧 Core generator / Ядро генерации
├── config.json          # ⚙️ Auto-generated config / Авто-генерируемый конфиг
├── panel_settings.json  # 💾 Panel settings / Настройки панели
├── requirements.txt     # 📦 Dependencies / Зависимости
└── README.md            # 📖 Documentation / Документация
```

---
**⭐ If this project helped you, please give it a star! / Если проект помог вам, поставьте звезду! ⭐**
