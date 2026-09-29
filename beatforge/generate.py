"""Generación de una instrumental ORIGINAL con MusicGen (audiocraft).

Se condiciona con un prompt de texto (estilo, instrumentación, energía) y,
opcionalmente, con el CROMA de la referencia (contorno armónico general) — NO
con su melodía nota a nota. Esto produce una obra nueva "en la onda de" la
referencia. Lee la política de originalidad del README antes de usarlo.
"""
from __future__ import annotations


def build_prompt(base_prompt, analysis=None):
    """Enriquece el prompt de estilo con el tempo/tonalidad detectados."""
    if not analysis:
        return base_prompt
    extra = f", {analysis['bpm']} bpm, key {analysis['key']} {analysis['mode']}"
    return base_prompt.strip() + extra


def generate(prompt, duration=20, out_path="generated", melody_path=None,
             model_name="facebook/musicgen-melody"):
    """Genera una instrumental original y la escribe en `out_path`.wav.

    - prompt: descripción de estilo (p. ej. "dark trap beat, heavy 808, brass").
    - duration: segundos.
    - melody_path: opcional; si se da, guía SOLO el contorno armónico (croma),
      no copia la melodía. Revisa siempre la originalidad del resultado.
    """
    import torchaudio
    from audiocraft.models import MusicGen
    from audiocraft.data.audio import audio_write

    model = MusicGen.get_pretrained(model_name)
    model.set_generation_params(duration=duration)

    if melody_path:
        melody, sr = torchaudio.load(melody_path)
        wav = model.generate_with_chroma([prompt], melody[None], sr, progress=True)
    else:
        wav = model.generate([prompt], progress=True)

    audio_write(out_path, wav[0].cpu(), model.sample_rate,
                strategy="loudness", loudness_compressor=True)
    return out_path + ".wav"
