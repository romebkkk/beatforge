"""Ensamblaje final: normaliza y exporta la instrumental a WAV y MP3.

Requiere ffmpeg instalado en el sistema (lo usa pydub para el MP3).
"""
from __future__ import annotations

import os


def export_beat(wav_path, out_base="output/beat", mp3_bitrate="320k"):
    """Normaliza el volumen y exporta a WAV + MP3. Devuelve {wav, mp3}."""
    from pydub import AudioSegment

    out_dir = os.path.dirname(out_base) or "."
    os.makedirs(out_dir, exist_ok=True)

    audio = AudioSegment.from_file(wav_path)
    audio = audio.normalize()

    wav_out = out_base + ".wav"
    mp3_out = out_base + ".mp3"
    audio.export(wav_out, format="wav")
    audio.export(mp3_out, format="mp3", bitrate=mp3_bitrate)
    return {"wav": wav_out, "mp3": mp3_out}
