@echo off

endlocal
goto settings

:tld
set /p TLD=TLD/extension (default is .com):
echo Please enter a TLD

if not defined TLD set "TLD=.com"
goto settings

:resultspath
set /p RP=Results path (default is Results):
if not defined RP set "RP=Results"
goto settings


:listpath
set /p LP=List path (default is WordLists):
if not defined LP set "LP=WordLists"
goto settings


:wordlist1
set /p L1=Wordlist 1 path (default is sampleList1.txt):
if not defined L1 set "L1=sampleList1.txt"
goto settings


:wordlist2
set /p L2=Wordlist 2 path (default is sampleList2.txt):
if not defined L2 set "L2=sampleList2.txt"
goto settings

:outputamount
set /p OA=Output amount (default is 100):
if not defined OA set "OA=100"
goto settings

:filename
set /p FN=File name (default is newList, only changes the prefix; date and time are still present):
if not defined FN set "FN=newList"
goto settings

:textsummary
set /p TS=Text summary (yes or no) (default is no):
if not defined TS set "TS=no"
goto settings

echo.



:scanagain
cls
echo.**********************
echo.
if /i "%TS%"=="yes" (
    python dnn.py -TLD %TLD% -RP %RP% -LP %LP% -L1 %L1% -L2 %L2% -OA %OA% -FN %FN% -TS 
) else (
    python dnn.py -TLD %TLD% -RP %RP% -LP %LP% -L1 %L1% -L2 %L2% -OA %OA% -FN %FN%
)

echo.
echo.**********************
echo.
echo [Enter] - Run Again
echo [S] - Modify Settings
echo.
set /p choice=Repeat Domain Name Ninja or change settings?:
echo.
echo.
if /i "%choice%"=="R" goto scanagain 
if /i "%choice%"=="S" goto settings
goto scanagain
echo.


:settings
cls
echo Welcome to Domain Name Ninja!
echo.
echo Please enter the following arguments:

echo [1] - TLD

echo [2] - Results Path

echo [3] - List Path

echo [4] - Wordlist 1

echo [5] - Wordlist 2

echo [6] - Output Amount

echo [7] - File name (prefix)

echo [8] - Text summary
echo.
echo [default] - Restore settings to default
echo.
echo [r] - Run
echo.
set /p choice=What would you like to do? (1-8, Default, R)
if /i "%choice%"=="1" goto tld
if /i "%choice%"=="2" goto resultspath
if /i "%choice%"=="3" goto listpath
if /i "%choice%"=="4" goto wordlist1
if /i "%choice%"=="5" goto wordlist2
if /i "%choice%"=="6" goto outputamount
if /i "%choice%"=="7" goto filename
if /i "%choice%"=="8" goto textsummary
if /i "%choice%"=="default" goto defaults
if /i "%choice%"=="r" goto scanagain
goto settings

:defaults
set "TLD=.com"
set "RP=Results"
set "LP=WordLists"
set "L1=sampleList1.txt"
set "L2=sampleList2.txt"
set "OA=100"
set "FN=newList"
set "TS=no"
echo "Defaults have been restored!"
pause
goto settings