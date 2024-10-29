results=./allure_results_tickets_API
rep_history=./final-report_tickets_API/history
report=./final-report_tickets_API

rm -rf $results # Удалить папку с результатами
pytest test_tickets_API.py --alluredir=allure_results_tickets_API # Запустить тесты 
mv $rep_history $results # Перенести историю в результаты 
rm -rf $report # Удалить отчет
allure generate $results -o $report # Сгенерировать отчет
allure open $report # Открыть отчет