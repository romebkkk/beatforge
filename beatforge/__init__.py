"""
BeatForge — genera beats ORIGINALES inspirados en una referencia.
by DataFlow Elegance · MIT

Política de originalidad (léela): BeatForge extrae el tempo, la tonalidad y la
energía de una pista de referencia para generar una instrumental NUEVA "en la
onda de" esa referencia. NO está pensado para copiar la melodía nota a nota ni
para evadir sistemas de detección de copyright (Content ID). El objetivo es
crear obra original inspirada en un estilo — el estilo/vibe no es copyrightable;
la composición concreta, sí. Úsalo de forma responsable.
"""
from .analyze import analyze
from .generate import generate
from .assemble import export_beat
from .pipeline import run_pipeline

__version__ = "0.1.0"
__all__ = ["analyze", "generate", "export_beat", "run_pipeline", "__version__"]
