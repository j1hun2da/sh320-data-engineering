def get_my_chosun_name(family_name, month, day):
    #1
    first_names = ['쌍', '쇠', '복', '돌', '팽', '육', '쌍', '개', '칠', '갑', '삼', '방']
    
    #2
    second_names = ['봉', '구', '욕', '포', '똥', '삼', '식', '석', '놈', '님', '년', '돌', '단', '득', '방', '질', '장', '걸', '래', '룡', '동', '순', '자', '박', '창', '언', '것', '포', '만', '단', '국']
    
    #3
    first_name = first_names[month - 1]
    second_name = second_names[day - 1]
    
    #4
    chosun_name = family_name + first_name + second_name
    return f"당신의 조선시대 이름은 {chosun_name} 입니다."

print(get_my_chosun_name('배', 9, 13))
