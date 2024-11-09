@echo off

echo ============================
echo    INFORMACION DEL EQUIPO
echo ============================
echo.

:: 1. Nombre del equipo
echo Nombre del Equipo:
echo %COMPUTERNAME%
echo.

::2. Fecha y Hora Actual
echo Fecha y Hora Actual:
echo %date% %time%
echo.

::3. Pagina a Facebook, Google, Youtube y WhatsAoo
echo Realizando ping a sitios populares ...
echo.

echo ping a Facebook:
ping www.facebook.com -n 4
echo.

echo ping a Google:
ping www.google.com -n 4
echo.

echo ping a Youtube:
ping www.youtube.com -n 4
echo.

echo ping WhatsApp:
ping www.whatsapp.com -n 4
echo.

pause