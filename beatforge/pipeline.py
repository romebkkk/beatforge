"""Orquestador de extremo a extremo de BeatForge.

Flujo: analizar referencia -> (opcional) separar stems -> generar original
condicionada por estilo + tempo/tonalidad -> exportar WAV/MP3.
"""
from __future__ import annotations

import os

from .analyze import analyze
from .generate import build_prompt, generate
from .assemble import export_beat


ORIGINALITY_NOTICE = (
    "[BeatForge] Genera obra ORIGINAL inspirada en la referencia. No copia la "
    "melodia nota a nota ni evade deteccion de copyright. Revisa la "
    "originalidad del resultado antes de distribuirlo."
)


def run_pipeline(reference_path, prompt, duration=20, out_base="output/beat",
                 use_melody_guidance=False, separate_stems=False):
    """Ejecuta el flujo completo y devuelve un informe con rutas y análisis."""
    print(ORIGINALITY_NOTICE)

    ana = analyze(reference_path)
    print(f"[analyze] BPM={ana['bpm']} key={ana['key']} {ana['mode']} "
          f"dur={ana['duration_s']}s")

    stems = None
    melody_path = None
    if separate_stems or use_melody_guidance:
        from .separate import separate
        stems = separate(reference_path)
        if use_melody_guidance:
            # "other" suele contener la melodía/armonía; guía solo el croma.
            melody_path = stems.get("other")

    full_prompt = build_prompt(prompt, ana)
    print(f"[generate] prompt: {full_prompt}")
    raw = generate(full_prompt, duration=duration,
                   out_path=os.path.splitext(out_base)[0] + "_raw",
                   melody_path=melody_path)

    out = export_beat(raw, out_base=out_base)
    print(f"[done] {out['wav']} | {out['mp3']}")
    return {"analysis": ana, "stems": stems, "prompt": full_prompt, "output": out}
