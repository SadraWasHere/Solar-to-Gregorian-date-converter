# Simple Gregorian ⇄ Solar Date Converter

A lightweight Python module for converting between Gregorian and Solar (Shamsi) dates using a fixed offset approach.

> ⚠️ Note: This module does NOT implement a full astronomical or algorithmic calendar conversion. It applies a constant timedelta offset based on a predefined reference date.

---

## 📌 Overview

This module provides three functions:

- `GregToSol(dt)` – Convert Gregorian datetime to Solar
- `SolToGreg(dt)` – Convert Solar datetime to Gregorian
- `AutoConv(dt)` – Automatically detect and convert based on year

The conversion is performed by calculating a fixed time delta between:

- Gregorian reference: `2005-12-24`
- Solar reference: `1384-10-03`

All conversions are based on this delta.

---

## ⚙️ Installation

No external dependencies are required.

Just copy the module file into your project.

Python version: 3.x

---

## 🚀 Usage

```python
from datetime import datetime
from your_module import GregToSol, SolToGreg, AutoConv

dt = datetime(2023, 5, 1)

solar = GregToSol(dt)
print("Solar:", solar)

greg = SolToGreg(solar)
print("Gregorian:", greg)

auto = AutoConv(dt)
print("Auto:", auto)
