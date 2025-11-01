# JWT Key Generator / Генератор JWT Ключей

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Security](https://img.shields.io/badge/Security-Testing_Only-red.svg)

## 🇺🇸 English

### 🔐 Overview
A secure Python tool for generating JWT keys for development and testing purposes. Supports HMAC secrets and RSA key pairs with token generation and verification examples.

### ✨ Features
- 🔑 Generate HMAC secrets (HS256, HS384, HS512)
- 🔐 Create RSA key pairs (RS256, RS384, RS512) 
- 🎫 JWT token generation with custom payloads
- ✅ Token verification and validation
- 💾 Save keys to files with timestamps
- 🛡️ Secure random generation

### 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Generate all keys
python jwt_generator.py

# HMAC keys only
python jwt_generator.py --hmac-only

# RSA keys only  
python jwt_generator.py --rsa-only

# Custom output prefix
python jwt_generator.py --output my_project_keys
```

📁 Generated Files

· *_hmac_*.json - HMAC secret keys
· *_rsa_private_*.pem - RSA private keys
· *_rsa_public_*.pem - RSA public keys
· *_example_*.json - JWT token examples

⚠️ Security Notice

WARNING: This tool is for DEVELOPMENT and TESTING only. Never use generated keys in production environments.

---

🇷🇺 Русский

🔐 Обзор

Безопасный Python инструмент для генерации JWT ключей для разработки и тестирования. Поддерживает HMAC секреты и RSA ключевые пары с примерами генерации и верификации токенов.

✨ Возможности

· 🔑 Генерация HMAC секретов (HS256, HS384, HS512)
· 🔐 Создание RSA ключевых пар (RS256, RS384, RS512)
· 🎫 Генерация JWT токенов с кастомными payload
· ✅ Верификация и валидация токенов
· 💾 Сохранение ключей в файлы с временными метками
· 🛡️ Безопасная случайная генерация

🚀 Быстрый старт

```bash
# Установка зависимостей
pip install -r requirements.txt

# Генерация всех ключей
python jwt_generator.py

# Только HMAC ключи
python jwt_generator.py --hmac-only

# Только RSA ключи
python jwt_generator.py --rsa-only

# Свой префикс для файлов
python jwt_generator.py --output my_project_keys
```

📁 Генерируемые файлы

· *_hmac_*.json - HMAC секретные ключи
· *_rsa_private_*.pem - RSA приватные ключи
· *_rsa_public_*.pem - RSA публичные ключи
· *_example_*.json - Примеры JWT токенов

⚠️ Важное предупреждение

ВНИМАНИЕ: Этот инструмент предназначен только для РАЗРАБОТКИ и ТЕСТИРОВАНИЯ. Никогда не используйте сгенерированные ключи в продакшене.

📄 License / Лицензия

MIT License - see LICENSE file for details / MIT Лицензия - подробности в файле LICENSE

🔧 Requirements / Зависимости

```txt
pyjwt>=2.0.0
cryptography>=3.0
```

🐛 Issue Reporting / Сообщение об ошибках

If you find any issues, please create an issue in the GitHub repository.
Если вы нашли ошибки, пожалуйста, создайте issue в репозитории GitHub.

---

⭐ If this project helped you, please give it a star! / Если проект помог вам, поставьте звезду! ⭐

```
