"""Análisis acústico de la referencia: tempo (BPM), tonalidad y duración.

Solo lectura: extrae características musicales objetivas (no protegidas por
copyright) para condicionar una generación original.
"""
from __future__ import annotations

import numpy as np

# Perfiles de Krumhansl-Schmuckler para estimar la tonalidad
_MAJOR = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
_MINOR = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
_NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def estimate_key(y, sr):
    """Estima tonalidad y modo (mayor/menor) por correlación de croma."""
    import librosa
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    profile = chroma.mean(axis=1)
    best = None  # (nota, modo, score)
    for i in range(12):
        maj = np.corrcoef(np.roll(_MAJOR, i), profile)[0, 1]
        mnr = np.corrcoef(np.roll(_MINOR, i), profile)[0, 1]
        for mode, score in (("major", maj), ("minor", mnr)):
            if best is None or score > best[2]:
                best = (_NOTES[i], mode, float(score))
    return {"key": best[0], "mode": best[1], "confidence": best[2]}


def analyze(path):
    """Devuelve BPM, tonalidad, modo y duración de un archivo de audio."""
    import librosa
    y, sr = librosa.load(path, mono=True)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    key = estimate_key(y, sr)
    return {
        "path": path,
        "duration_s": round(float(librosa.get_duration(y=y, sr=sr)), 2),
        "bpm": int(round(float(np.atleast_1d(tempo)[0]))),
        "key": key["key"],
        "mode": key["mode"],
        "key_confidence": round(key["confidence"], 3),
        "beat_count": int(len(beats)),
    }
