from cx_Freeze import setup, Executable

setup(
    name='Abdiel GPT',
    version='1.0',
    description='Descripción de tu aplicación',
    executables=[Executable('interfaz.py')]
)
