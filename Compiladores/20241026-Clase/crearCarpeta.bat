@echo off
set "DIRECTORIO=C:\CESBA"

if exist "%DIRECTORIO%" (
    echo La carpeta "Cesba" ya existe en c:\
    ) else (
        mkdir "%DIRECTORIO%"
        echo La carpeta "Cesba" ha sido creada en C:\
        )
pause