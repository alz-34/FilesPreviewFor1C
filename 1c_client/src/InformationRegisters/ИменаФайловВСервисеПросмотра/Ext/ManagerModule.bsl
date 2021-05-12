﻿#Если Сервер Или ТолстыйКлиентОбычноеПриложение Или ВнешнееСоединение Тогда
	
Процедура ЗаписатьДанные(СсылкаНаФайл, Знач ИмяФайла, Знач Расширение) Экспорт
	
	Набор = РегистрыСведений.ИменаФайловВСервисеПросмотра.СоздатьНаборЗаписей();
	Набор.Отбор.Файл.Установить(СсылкаНаФайл);
	Набор.Прочитать();
	
	Если Набор.Количество() Тогда
		ТекущаяЗапись = Набор[0];
	Иначе
		ТекущаяЗапись = Набор.Добавить();
	КонецЕсли;   
	
	ТекущаяЗапись.Файл = СсылкаНаФайл;
	ТекущаяЗапись.Имя = ИмяФайла;
	ТекущаяЗапись.Расширение = Расширение;
	
	Набор.Записать(Истина);

КонецПроцедуры

Функция ПолучитьИмя(СсылкаНаФайл) Экспорт
	
	Запрос = Новый Запрос;
	Запрос.Текст = 
		"ВЫБРАТЬ
		|	ИменаФайловВСервисеПросмотра.Файл КАК Файл,
		|	ИменаФайловВСервисеПросмотра.Имя КАК Имя,
		|	ИменаФайловВСервисеПросмотра.Расширение КАК Расширение
		|ИЗ
		|	РегистрСведений.ИменаФайловВСервисеПросмотра КАК ИменаФайловВСервисеПросмотра
		|ГДЕ
		|	ИменаФайловВСервисеПросмотра.Файл = &Файл";
	
	Запрос.УстановитьПараметр("Файл", СсылкаНаФайл);
	
	РезультатЗапроса = Запрос.Выполнить();
	
	Результат = Новый Структура;
	Для каждого Колонка Из РезультатЗапроса.Колонки Цикл
		Результат.Вставить(Колонка.Имя);
	КонецЦикла;
	
	ВыборкаДетальныеЗаписи = РезультатЗапроса.Выбрать();
	
	Если ВыборкаДетальныеЗаписи.Следующий() Тогда
		ЗаполнитьЗначенияСвойств(Результат, ВыборкаДетальныеЗаписи);
	КонецЕсли;     	
	
	Возврат Результат;
	
КонецФункции
	
#КонецЕсли