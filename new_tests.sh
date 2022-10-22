echo "Bash скрипт запущен"

source Python/Scripts/activate

ver=$(python --version)

if [ "$ver" = "Python 3.9.13" ] 
then
echo "Окружение активировано - $ver"
else
echo "Активировано какое то не то окружение... - $ver"
fi

# start "" "App\TrashCatWindows\TrashCat-Windows.exe"
# echo 'Запуск игры'
# sleep 10

echo 'Запуcк тестов'
sleep 1

python -m pytest -s TestsPython\\new_tests
# python -m pytest -s TestsPython\\tests
