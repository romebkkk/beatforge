#!/usr/bin/env python3
"""BeatForge CLI — genera un beat original inspirado en una referencia.

Ejemplo:
  python cli.py --reference ref.mp3 --prompt "dark trap beat, heavy 808, aggressive brass" \
                --duration 20 --out output/mi_beat --melody-guidance
"""
import argparse
import json
import sys

from beatforge import run_pipeline, __version__


def main():
    ap = argparse.ArgumentParser(description=f"BeatForge v{__version__} — DataFlow Elegance")
    ap.add_argument("--reference", required=True, help="Audio de referencia (mp3/wav) o ruta local")
    ap.add_argument("--prompt", required=True, help="Estilo deseado, p. ej. 'dark trap beat, heavy 808'")
    ap.add_argument("--duration", type=int, default=20, help="Duración en segundos (def. 20)")
    ap.add_argument("--out", default="output/beat", help="Ruta base de salida (sin extensión)")
    ap.add_argument("--melody-guidance", action="store_true",
                    help="Usar el contorno armónico (croma) de la referencia como guía (opcional)")
    ap.add_argument("--stems", action="store_true", help="Separar stems de la referencia (Demucs)")
    args = ap.parse_args()

    try:
        report = run_pipeline(
            reference_path=args.reference,
            prompt=args.prompt,
            duration=args.duration,
            out_base=args.out,
            use_melody_guidance=args.melody_guidance,
            separate_stems=args.stems,
        )
    except Exception as e:  # noqa: BLE001
        print(f"[error] {e}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
