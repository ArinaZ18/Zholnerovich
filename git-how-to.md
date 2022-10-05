git 1. Создание ключа SSH
Вводим в терминал команду: ssh-keygen -t ed25519 -C "youremail"
Пропускаем запрос выбора папки и создания пороля.

2. Добавляем ключ SSH в GitHab
Заходим в папку .SSH. Открываем файл с расширением .pub.
Копируем ссылку и перехолим в GitHab.
В GitHab в настройках заходи в SSH and GPG keys и вставляем ссылку в графу SSH keys.

3. Клонируем репозиторий
Для клонирования репозитория используем, используя команду: git clone git@githab.com^username/repository.git 

git status
git add .
git commit -m ""
git push