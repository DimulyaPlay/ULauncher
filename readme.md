Универсальный лаунчер для запуска приложений с заданными аргрументами (как ярлык, но портативный)
1. Конфигурация сохраняется в обычном текстовом файле. Имя файла конфигурации совпадает с именем .exe файла лаунчера.
2. Путь к программе не указывается, так как предполагается, что все программы находятся в одной директории с лаунчером.
3. Пример содержания файла launcher.exe "Program1.exe -arg1 -arg2", возможно несколько строк (запустятся несколько программ/экземпляров)
4. Добавление "pause" в конце строчки конфигурации (последним аргументом) запускает программу в консольном окне, которое не будет закрыто после выполнения
