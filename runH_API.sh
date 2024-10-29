results=./allure_results_hotels_API
rep_history=./final-report_hotels_API/history
report=./final-report_hotels_API

rm -rf $results # Удалить папку с результатами
pytest test_hotels_API.py --alluredir=allure_results_hotels_API # Запустить тесты 
mv $rep_history $results # Перенести историю в результаты 
rm -rf $report # Удалить отчет
allure generate $results -o $report # Сгенерировать отчет
allure open $report # Открыть отчет