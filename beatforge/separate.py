"""Separación de stems con Demucs (HTDemucs) vía su CLI.

Opcional en el pipeline. Útil para inspeccionar la instrumentación de la
referencia (batería/bajo/melodía). NO redistribuyas los stems de una obra
protegida: son solo para análisis/inspiración local.
"""
from __future__ import annotations

import os
import subprocess
import sys


def separate(path, out_dir="stems", model="htdemucs"):
    """Separa un audio en stems (drums, bass, other, vocals) con Demucs.

    Requiere `pip install demucs`. Devuelve un dict {stem: ruta_wav}.
    """
    os.makedirs(out_dir, exist_ok=True)
    cmd = [sys.executable, "-m", "demucs", "-n", model, "-o", out_dir, path]
    subprocess.run(cmd, check=True)

    base = os.path.splitext(os.path.basename(path))[0]
    stem_dir = os.path.join(out_dir, model, base)
    return {
        name: os.path.join(stem_dir, f"{name}.wav")
        for name in ("drums", "bass", "other", "vocals")
    }
