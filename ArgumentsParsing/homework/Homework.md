Колеги в цьому завданні ми будемо вчитися підбивати статистику та писати скрипти



В Директорії [beer_review](beer_review) ви можете знайти набір csv файлів з зібраними данними по фідбеках пива. 


Задача 1

Напишіть скрипт, який приймає на вхід 
 - start_year; required: false; default: min(start_year)
 - end_year; required: false; default: max(end_year) 
 - path_to_source_files; required: true;
 - destination_path; required: false; default: .
 - destination_filename; required: false; default: f"{start_year}-{end_year}_{timestamp}.csv".
Скрипт заходить в директорію path_to_source_files, та знаходить всі csv файли в діапазоні start_year:end_year.
Витягує всі данні з них і створює 1 файл з всім витягнутими данними. 


Задача 2

Напишіть скрипт, який приймає на вхід наступні параметри
 - source_file_path; required: true;
 - beer_type; required: false; help: find most favorite beer type;
 - beer_name; required: false; help: find most favorite beer name;
 - day_of_review; required: false; help: find day with they most number of review;(based on review_time)
 - reviewer_stats; required: false; help: Show number of reviews for reviewer;
 
 

