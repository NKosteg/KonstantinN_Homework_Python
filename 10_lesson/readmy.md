##### Инструкция по прогонам тестов, созданию, выгрузке и просмотрам отчетов.

Для запуска прогона тестов и формирования отчета выполни следующую команду: ~python -m pytest --alluredir allure-result~

Для выгрузки отчета в браузер выполни следующую команду: ~allure serve allure-result~

Для выгрузки отчета в директорию выполни команду: ~allure serve allure-result~ 
Файлы сохранятся в созданной по умолчанию директории `allure-report`, теперь отчет можно передать заинтересованным лицам.
Также можно открыть отчет из этой директории выполнив команду: ~allure open allure-report~

##### Дополнительно.
Также есть возможность запускать прогоны тестов и формировать отчеты с автоматическим сохранением предыдущих результатов, 
для отслеживания динамики прогонов и статистики результатов прогонов.
Для автоматического прогона и создания отчета выполни команду: ~./run.sh~, которая выполнит код из файла: `run.sh`
Отчет автоматически откроется в новом окне браузера, при этом в нем будут отображены также результаты предыдущих прогонов.


