echo "Скрипт запущен"

alias python=${PWD}/Python/Scripts/python.exe
ver=$(python --version)

if [ "$ver" = "Python 3.9.13" ] 
then
echo "Окружение успешно активировано"
else
echo "Ошибка активации окружения"
exit 1
fi

echo 'Запуск игры'
start "" "App\TrashCatWindows\TrashCat-Windows.exe"
sleep 10

echo 'Запуcк тестов'

python -m pytest -s TestsPython\\new_tests
# python -m pytest -s TestsPython\\tests
