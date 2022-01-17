import os

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
DATA_DIR = os.path.join(BASE_DIR, "data")
FONTS_DIR = os.path.join(DATA_DIR, "fonts")
FONDOS_DIR = os.path.join(DATA_DIR, "fondos")
FONDOS_LUNES = os.path.join(FONDOS_DIR, "Lunes")
FONDOS_MARTES = os.path.join(FONDOS_DIR, "Martes")
FONDOS_MIERCOLES = os.path.join(FONDOS_DIR, "Miercoles")
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
SAMPLE_INPUTS = os.path.join(SAMPLE_DIR, "inputs")
SAMPLE_OUTPUTS = os.path.join(SAMPLE_DIR, 'outputs')
