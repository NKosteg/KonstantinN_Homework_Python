results=./results
rep_history=./final-report/history
report=./final-report

rm -rf $results # Удалить папку с предыдущими результатами
pytest --alluredir=$results # Запустить тесты и сохранить новые результаты
mv $rep_history $results # Перенести историю из папки final-report в папку results с новыми результатами
rm -rf $report # Удалить старый отчет вместе с папкой final-report
allure generate $results -o $report # Сгенерировать новый отчет и поместить его во вновь созданную папку final-report
allure open $report # Открыть отчет из папки final-report