def article_validate(title, author, content):
    errors = {}
    if not title:
            errors['title'] = 'Поле обязательное'
    elif len(title) < 5:
        errors['title'] = 'Введите больше 5 символов'
    if not author:
        errors['author'] = 'Поле обязательное'
    elif len(author) > 50:
        errors['author'] = 'Вы ввели больше 50 символов'
    if not content:
        errors['content'] = 'Поле обязательное'
    elif len(content) > 3000:
        errors['content'] = 'Вы ввели больше 3000 символов'
    return errors