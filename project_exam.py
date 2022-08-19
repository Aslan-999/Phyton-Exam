print("İmtahan 20 sualdan ibarətdir və hər doğru sual 5 bal kimi hesablanır. \nİmtahan sonunda nəticələrinizlə tanış ola bilərsiz. UĞURLAR!")
variant_q =str(input("Seçə biləcəyiniz variantlar (A , B , C , D): " ))
start_q = input("Imtahana baslamaq ucun 'Basla' yazin: ")



#                                             A variantı


questions = [
    {
        "content" : "Eqoizmin əksi?",
        "a" : "Etika",
        "b" : "Hedoniz",
        "c" : "Altruizm",
        "d" : "Utilitarianizm",
        "answer" : "c"
    },

   {
        "content" : "İlk qüllə saatı neçənci ildə düzəlib?",
        "a" : "1432",
        "b" : "1404",
        "c" : "1534",
        "d" : "1345",
        "answer" : "b"
    },

    {
        "content" : "Çempionlar liqasını 5 dəfə qaldıran klub?",
        "a" : "M. Yunayted",
        "b" : "Milan",
        "c" : "Barselona",
        "d" : "Liverpul",
        "answer" : "d"
    },

    {
        "content" : "Pişiklərin maksimum surəti saatda neçə kilometrdir?",
        "a" : "70",
        "b" : "60",
        "c" : "40",
        "d" : "50",
        "answer" : "d" 
    },

    {
        "content" : "Hansı heyvanın qırılan sümüyü qaynamır?",
        "a" : "Delfin",
        "b" : "At",
        "c" : "Zürafə",
        "d" : "Pişik",
        "answer" : "a"
    },
    
    {
        "content" : "İlk teleskop neçənci ildə düzəlib?",
        "a" : "1608",
        "b" : "1589",
        "c" : "1622",
        "d" : "1699",
        "answer" : "a"
    },

    {
        "content" : "4 ədəd dizi olan yeganə heyvan hansıdır?",
        "a" : "Ayı",
        "b" : "Dələ",
        "c" : "Fil",
        "d" : "Ceyran",
        "answer" : "c"
    },

    {
        "content" : "Hansı canlının qanı bəyazdır?",
        "a" : "Çəyirtgə",
        "b" : "Kəpənək",
        "c" : "İlbiz",
        "d" : "Hörümçək",
        "answer" : "a"
    },

    {
        "content" : "1950-ci ildə dünya kuboku hansı ölkədə keçirilib?",
        "a" : "Kanada",
        "b" : "Fransa",
        "c" : "Brazilya",
        "d" : "İtalya",
        "answer" : "c"
    },

    {
        "content" : "2010-cu ildə dünya kubokunu hansı ölkə qazanıb?",
        "a" : "Hollandiya",
        "b" : "Uruquvay",
        "c" : "Fransa",
        "d" : "İspaniya",
        "answer" : "d"
    },

    {
        "content" : "Azadlıq heykəlinin ayaq nömrəsi neçədir?",
        "a" : "919",
        "b" : "879",
        "c" : "909",
        "d" : "899",
        "answer" : "b"
    },

    {
        "content" : "Hansı ölkədə ad günlərində hədiyə qəbul etmək yerinə hədiyə vermək adətdir?",
        "a" : "Brazilya",
        "b" : "Ərəbistan",
        "c" : "Tayland",
        "d" : "Peru",
        "answer" : "c"
    },

    {
        "content" : "İnsan başında təxmini nə qədər saç olur?",
        "a" : "80-300 min",
        "b" : "60-150 min",
        "c" : "30-450 min",
        "d" : "10-15 min",
        "answer" : "b"
    },

    {
        "content" : "Kişilərin saqqalları hansı fəsildə daha çox uzanır?",
        "a" : "Yaz",
        "b" : "Yay",
        "c" : "Payız",
        "d" : "Qış",
        "answer" : "a"
    },

    {
        "content" : "Bir auksionda , bir inək üçün ödənən ən çox pul nə qədərdir?",
        "a" : "1300000",
        "b" : "1400000",
        "c" : "1200000",
        "d" : "1100000",
        "answer" : "a"
    },

    {
        "content" : "Hansı heyvanın gözləri 4 ayaqlarınıda görəbiləcək şəkildədir?",
        "a" : "Balıq",
        "b" : "Eşşək",
        "c" : "Ceyran",
        "d" : "Zürafə",
        "answer" : "b"
    },

    {
        "content" : "Bu günə qədər bir qadın ən çox nə qədər uşaq dünaya gətirib?",
        "a" : "65",
        "b" : "67",
        "c" : "55",
        "d" : "69",
        "answer" : "d"
    },

    {
        "content" : "Neçənci ilə qədər pomidorun zəhərli olduğu zənn edilirdi?",
        "a" : "1840",
        "b" : "1870",
        "c" : "1860",
        "d" : "1830",
        "answer" : "d"
    },

    {
        "content" : "Uşaqlar hansı fəsildə daha çox böyüyür",
        "a" : "Yaz",
        "b" : "Yay",
        "c" : "Payız",
        "d" : "Qış",
        "answer" : "a"
    },

    {
        "content" : "Qarğalar orta hesabla neçə il yaşayır?",
        "a" : "100",
        "b" : "120",
        "c" : "180",
        "d" : "300",
        "answer" : "b"
    },

]

point = 0
quest_num = 1
quest_len = len(questions)


for i in questions:
    if variant_q != "A":
        print("Düzgün variantı seçdiyinizdən əmin olun")
        break
    elif start_q != "Basla":
        print("İmtahana başlamaq mümkun olmadı!")
        break
    print(quest_num, ".", i["content"])
    print("A) ", i["a"])
    print("B) ", i["b"])
    print("C) ", i["c"])
    print("D) ", i["d"])
    quest_num += 1
    user_ans = str(input("Cavab: ").lower())
    if user_ans == i["answer"]:
        point += 1

        print("Sizin cavabiniz doğrudur! \n")
    else:
        print("Sizin cavabınız yanlışdır! \n")
    
    print(
        "İmtahan başa çatdı!\n"
        "İmtahan suallarının sayı: {}\n"
        "Düzgün cavabların sayı: {}\n"
        "Düzgün olmayan cavabların sayı: {}\n"
        "Toplam Bal: {}\n"
        .format(quest_num - 1 , point , quest_len - point , point*5)
        )    
            

