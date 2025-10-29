# Web Scraper Fútbol Uruguay 🇺🇾⚽

Scraper de datos reales de la Primera División Uruguaya desde FBref.

## 🚀 ¿Qué hace?

- Extrae la tabla de posiciones del fútbol uruguayo (Liga Uruguaya)
- Parseo completo de equipos + estadísticas
- Guarda resultados en CSV dentro de `data/`
- Funciona incluso con protección anti-bot (Selenium headless)

✅ Código ejecutable desde terminal  
✅ Datos reales  
✅ Entrega lista para presentación

---

## 🧪 Ejemplo de uso

```bash
python -m webscraper_futbol

## 📦 Descarga

[⬇️ Descargar última release](https://github.com/matihassastre/webscraper-futbol/releases/latest)
![Release](https://img.shields.io/github/v/release/matihassastre/webscraper-futbol?label=release)
![Downloads](https://img.shields.io/github/downloads/matihassastre/webscraper-futbol/total?label=descargas)

## 🧪 Instalación desde Release (Windows)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
python -m webscraper_futbol
