# 🎛️ BeatForge

> Turn any reference track into an **original beat "in its vibe"**. BeatForge analyses a reference's **tempo, key and energy** and uses **MusicGen** to generate a brand-new instrumental in that style — it does **not** copy the melody note-for-note. Python pipeline for producers.

<sub>Part of the **DataFlow Audio** suite · [🇪🇸 Español abajo](#-español)</sub>

---

## ⚖️ Originality policy (read this)

BeatForge is built to create **original works inspired by a style**, not to clone songs or evade copyright detection. Musical **style/vibe is not copyrightable**; a specific melody/composition **is**. So BeatForge:

- ✅ Extracts objective, non-copyrightable features (BPM, key, energy) to condition generation.
- ✅ Generates a **new** instrumental with MusicGen from a text prompt (+ optional *harmonic-contour* guidance via chroma).
- ❌ Does **not** copy the reference's melody note-for-note.
- ❌ Has **no** "evade Content ID" feature by design.

**You** are responsible for reviewing the originality of anything you distribute.

## How it works

```
reference.mp3
   │  librosa → BPM, key, duration            (analyze.py)
   │  (optional) HTDemucs → stems             (separate.py)
   ▼
MusicGen  ← text prompt + tempo/key + optional chroma guidance   (generate.py)
   ▼
normalize & export → beat.wav / beat.mp3       (assemble.py)
```

## Install

Needs Python 3.10+, **ffmpeg**, and ideally a **CUDA GPU** (MusicGen/Demucs are heavy).

```bash
pip install -r requirements.txt
```

## Use

```bash
python cli.py --reference ref.mp3 \
              --prompt "dark trap beat, heavy 808, aggressive brass" \
              --duration 20 --out output/mi_beat
# optional harmonic-contour guidance from the reference:
python cli.py --reference ref.mp3 --prompt "boom bap, jazzy keys" --melody-guidance
```

Output: `output/mi_beat.wav` and `.mp3`, plus a JSON report with the detected BPM/key.

## Modules
`analyze.py` (librosa) · `separate.py` (Demucs) · `generate.py` (MusicGen) · `assemble.py` (export) · `pipeline.py` (orchestrator) · `cli.py`.

## Status
Reference implementation targeting the documented APIs of librosa, Demucs, audiocraft/MusicGen and pydub. Run it on a machine with a GPU + the dependencies above.

## License
[MIT](LICENSE) © 2026 DataFlow Elegance

---

## 🇪🇸 Español

**BeatForge** convierte cualquier pista de referencia en un **beat original "en su onda"**: analiza el **tempo, la tonalidad y la energía** de la referencia y usa **MusicGen** para generar una instrumental nueva en ese estilo — **sin copiar la melodía nota a nota**.

### ⚖️ Política de originalidad (léela)
El **estilo/vibe no es copyrightable**; la **composición concreta, sí**. BeatForge extrae solo características objetivas (BPM, tonalidad, energía) y genera obra **nueva**. **No** copia la melodía nota a nota y **no** incluye ninguna función para "evadir Content ID". Tú eres responsable de revisar la originalidad de lo que distribuyas. Así el resultado es legalmente obra nueva y lo puedes vender tranquilo.

### Instalar y usar
Requiere Python 3.10+, **ffmpeg** y preferiblemente **GPU CUDA**.
```bash
pip install -r requirements.txt
python cli.py --reference ref.mp3 --prompt "dark trap beat, heavy 808" --duration 20 --out output/mi_beat
```

---

<div align="center">
Hecho con ❤️ por <a href="https://github.com/romebkkk">DataFlow Elegance</a> · <a href="https://dataflowelegance.es">dataflowelegance.es</a>
</div>
