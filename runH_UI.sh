results=./allure_results_hotels_UI
rep_history=./final-report_hotels_UI/history
report=./final-report_hotels_UI

rm -rf $results # Удалить папку с результатами
pytest test_hotels_UI.py --alluredir=allure_results_hotels_UI # Запустить тесты 
mv $rep_history $results # Перенести историю в результаты 
rm -rf $report # Удалить отчет
allure generate $results -o $report # Сгенерировать отчет
allure open $report # Открыть отчет