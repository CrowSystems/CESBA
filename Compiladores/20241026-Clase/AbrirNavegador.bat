@echo off
setLocal

::Intenta Abrir Microsoft Edge
start "" "msedge"
if %errorlevel% equ 0(
    echo Microsoft Edge se ha abierto correctamente.
    goto end
)

::Si edge no esta instalado, intenta abrir Google Chrome
start "" "chrome"
if %errorlevel% equ 0 (
    echo Google Chrome se a abierto correctamente.
    goto end
)

::Si ninguno de los navegadores esta diponible
echo No se encontro Microsoft Edge ni Google Chrome en este sistema.
:end
pause
endlocal