results=./allure_results_tickets_UI
rep_history=./final-report_tickets_UI/history
report=./final-report_tickets_UI

rm -rf $results # Удалить папку с результатами
pytest test_tickets_UI.py --alluredir=allure_results_tickets_UI # Запустить тесты 
mv $rep_history $results # Перенести историю в результаты 
rm -rf $report # Удалить отчет
allure generate $results -o $report # Сгенерировать отчет
allure open $report # Открыть отчет