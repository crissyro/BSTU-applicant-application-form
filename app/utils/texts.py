START_TEXT = """🎓 Добро пожаловать в опрос для абитуриентов!

📝 Цель этого опроса - собрать статистические данные для улучшения системы образования. 

⏱ Опрос займет не более 5 минут
"""

def format_summary(data):
    return f"""🧑‍🎓 Ваши ответы:
    
♂️ Пол: {data.get('gender', '—')}
🏫 Класс: {data.get('grade', '—')}
📚 Школа: {data.get('school', '—')}
📊 Профиль: {data.get('profile', '—')}
📖 Предметы ЕГЭ: {data.get('subjects', '—')}
🎯 Планируемый балл: {data.get('scores', '—')}
🏛 Вузы: {data.get('universities', '—')}
🎓 Специальности: {data.get('specialties', '—')}
🎖 Военная кафедра: {data.get('military_dep', '—')}
🏢 БГТУ: {data.get('bstu', '—')}"""