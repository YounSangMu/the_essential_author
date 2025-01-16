#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd 
import streamlit as st 
from PIL import Image
import os

#0. data summary
author_db = pd.read_csv('author_db.csv')
author_list = list(author_db["author_cd"])

group_to_authors = {
    "group_a" : ['GO', 'KSY'],
    "group_b" : ['BW', 'HG', 'KYS'],
    "group_c" : ['AC', 'HH', 'DO'],
    "group_d" : ['EH', 'SF'],
    "group_e" : ['EH', 'SF', 'DO'],
    "group_f" : ['HG', 'BW'],
    "group_infp" : ['BW', 'DO', 'KYS'],
    "group_intp" : ['AC', 'KSY']
}

author_emblem_dict_1 = {}
for index, row in author_db.iterrows() :
    author_emblem_dict_1[row["prestigious emblem_1"]] = row["author_cd"]


#1. 디 에센셜 소개
st.header("디 에센셜 작가 테스트📚")
st.markdown('#### *"좋아하는 작가를 만난다는 것"*')
st.markdown(f"한동안 한 명의 작가에게 빠진다는 건, 잠시 인생을 함께 걸을 동행을 만나는 것 같다는 생각이 들어요.<br>핵심 작품을 엮은 한 권의 책으로, 인생을 섬세하게 느끼고 치열하게 고민했던 작가와 만나는 시간 가지길 바랍니다.", unsafe_allow_html=True)

img = Image.open('image/main_image.png')
st.image(img, width=300, caption='Image from Unsplash', use_container_width=True)


#2. 서비스 & 취지 소개 
st.markdown("#### 테스트 제대로 활용하는 법 ❗")
st.markdown("나와 비슷한 취향의 작가를 만나는 것도 물론 좋지만, 내가 **배우고 싶은 사람** 또는 나와 **반대되는 사람**도 한번 떠올려보세요. 더 많은 작가를 만날 수 있을 겁니다.") 

st.divider()

#3. 테스트 시작 
st.markdown('### 테스트 시작!')
st.markdown("#### 1.기본 질문 ✅")

#3-1. 1번 문항 : 분량
options_basic_1 = {
    "500p 초과!": "upper",
    "500p 이하": "500",
    "400p 이하": "400",
    "300p 이하": "300"
}

basic_1 = st.radio(
'Q1-1. 감당할 수 있는 분량은 어느정도 인가요?', list(options_basic_1.keys()),
captions = ['당신은 진정한 낭만 독서가', '그날의 내가 책임지겠죠', '나는 나를 믿지 않아', '요즘 너무 바빠요..']
)
#st.write(f"선택한 값: {options_basic_1[basic_1]}")

st.markdown('')

#3-2. 2번 문항 : 국내/외
options_basic_2 = {
    "가리지 않아요" : 2 ,
    "한국": 0,
    "해외": 1
}

basic_2 = st.radio(
'Q1-2. 국내/외 중 선호하는 소설이 있나요?', list(options_basic_2.keys()),
captions = ['', '한국도 이제 노벨문학상 보유국', '문화 교류가 중요하죠']
)

st.markdown('')

#3-3. 3번 문항 : 시 선호 여부 
options_basic_3 = {
    "상관 없어요": 0,
    "시는 어려워요": 1
}

basic_3 = st.radio(
'Q1-3. 시와 에세이로 이뤄진 책도 괜찮나요?', list(options_basic_3.keys())
)

st.divider()
st.markdown("#### 2.성향 테스트 📋")
st.markdown('')

#4-1. 4번 문항 : 성향 
options_tendency_1 = {
    "세상에 전하는 메시지": "group_a",
    "독자가 느낄 감정": "group_b",
    "인생에 대한 깊이 있는 통찰": "group_c",
    "사랑과 상처가 교차하는 인간적인 서사": "group_d"
}

tendency_1 = st.radio(
'Q2-1. 당신이 소설을 읽을 때 가장 중요하게 생각하는 것은?', list(options_tendency_1.keys())
)

st.markdown('')

#4-4. 7번 문항 : 성향 
options_tendency_2 = {
    "재미있는 이야기나 활동으로 기분을 전환시킨다.": "SF",
    "문제의 원인을 분석하고 해결책을 함께 찾아준다.": "GO",    
    "따뜻한 말보다 옆에서 조용히 함께 있어준다.": "HG",
    "자신의 상처를 이야기하며 혼자가 아님을 말한다.": "DO",    
    "고통 속에서 자기만의 길을 갈 수 있도록 지탱해준다.": "AC"
}

tendency_2= st.radio(
'Q2-2. 사랑하는 사람이 힘들어할 때, 당신은 어떻게 위로하나요?',list(options_tendency_2.keys())
)

st.markdown('\n')


#4-2. 5번 문항 : 성향 
options_tendency_3 = {
    "먼저 다가가지 못하고 마음속으로만 괴로워한다.": "DO",    
    "친구의 의미를 되돌아보고 담담하게 받아들인다.": "AC",
    "관계가 소원해진 원인을 분석하고 대화를 시도한다.": "GO", 
    "쿨한 척 돌아서지만, 오랫동안 친구를 기다린다." : "SF",
    "깊은 자기반성 후에 자기 마음을 솔직하게 표현한다.": "KSY"
}

tendency_3 = st.radio(
'Q2-3. 오랜 친구와의 관계가 멀어졌습니다. 당신은 어떻게 하나요?',list(options_tendency_3.keys())
)

st.markdown('\n')

#4-3. 6번 문항 : 성향 
options_tendency_4 = {
    "일상의 소소한 아름다움이 더 소중하게 여겨지는 세상을 만든다.": "KYS",
    "누구나 두려움 없이 도전하고 실패해도 괜찮은 세상을 만든다.": "EH",
    "감정과 생각을 자유롭게 표현할 수 있는 세상을 만든다.": "BW",    
    "사람들의 상처와 고통을 보듬어주는 조용하고 평화로운 세상을 만든다.": "HG",
    "사람들이 자신을 깊이 탐구하고 내면의 평화를 찾을 수 있는 세상을 만든다.": "HH"
}

tendency_4 = st.radio(
'Q2-4. 세상을 마음대로 바꿀 수 있다면?', list(options_tendency_4.keys())
)

st.markdown('\n')

#4-5. 8번 문항 : 성향 
options_tendency_5 = {
    "생각의 깊이가 느껴지는 사람": "HH",
    "감정의 결을 세심하게 읽어내는 사람": "BW",
    "고독하지만 진실된 사람": "KSY",
    "도전적이면서 의지가 강한 사람": "EH",    
    "따뜻하고 맑은 마음으로 세상을 바라보는 사람": "KYS"
}

tendency_5 = st.radio(
'Q2-5. 어떤 인물이 가장 매력적으로 느껴지나요?',list(options_tendency_5.keys())
)

st.markdown('\n')

#4-6. 8번 문항 : 성향 
options_tendency_6 = {
    "잔잔한 여운과 따뜻한 감동": "KYS",
    "삶에 대한 깊은 고민과 사색": "AC",
    "생생하고 강렬한 감정": "group_e",
    "변화하고 싶은 열망": "GO",    
    "아픔 속에서도 피어나는 아름다움": "group_f"
}

tendency_6 = st.radio(
'Q2-6. 책을 읽은 후, 무엇을 얻길 바라나요?',list(options_tendency_6.keys())
)

st.markdown('\n')

#4-7. 9번 문항 : 성향 
options_tendency_7 = {
    "ESTP": "EH",
    "ENFP": "SF",    
    "INTJ": "GO",
    "INFP": "group_infp",
    "ISFP": "HG",
    "INFJ": "HH",
    "INTP": "group_intp",
}

st.markdown("Q2-7. 좋아하는 MBTI를 모두 고르세요. (복수선택)")
for mbti, author in options_tendency_7.items() : 
    st.checkbox(f"{mbti}", key=f"{mbti}")


st.divider()
st.markdown("#### 3.연애 테스트 ❤")
st.markdown('')

#5-1. 10번 문항 : 시뮬레이션 
options_simulation_1 = {
    "서로의 성장을 존중하고 지켜봐 주는 것" : "HH",    
    "슬픔과 외로움 조차도 이해해주는 것" : "DO", 
    "함께 모험하고 새로운 경험을 쌓는 것" : "EH", 
    "즐거운 순간을 함께 즐기는 것" : "SF",
    "각자의 자유를 존중해주는 것" : "AC",    
    "말 없이 곁에 있어주는 것." : "HG", 
    "감정과 내면의 깊이를 나누는 것" : "BW", 
    "서로를 마주보고 솔직해지는 것" : "KSY", 
    "가치와 신념을 공유하는 것": "GO", 
    "일상 속에서도 소중함 인식하는 것" : "KYS"
}

st.markdown("Q3-1. 연인과의 관계에서 중요한 것은? (복수선택)")
for value, author in options_simulation_1.items() : 
    st.checkbox(f"{value}", key=f"simulation_{author}_1")

st.markdown('\n')

#5-2. 11번 문항 : 시뮬레이션 
options_simulation_2 = {
    "감성이 가득 담긴 손편지" : "BW", 
    "세상에 대한 깊은 통찰을 나눌 수 있는 여행" : 'GO',         
    "햇살 좋은 오후, 한적한 카페에서의 프로포즈" : "AC",    
    "나의 슬픔을 이해해주는 따뜻한 말 한마디" : "DO", 
    "함께 떠나는 모험적인 여행" : "EH", 
    "‘사랑’이란 단어 하나 없지만 온몸으로 느껴지는 사랑의 시" : "KSY",     
    "로맨틱한 저녁 식사와 유쾌한 대화" : "SF",    
    "나를 잘 알아야만 줄 수 있는 세심한 선물들" : "KYS",
    "조용한 숲속에서 손잡고 함께 걷는 하루." : "HG",     
    "오랜 시간 곁에서 함께 있어주는 존재" : "HH",
}

st.markdown("Q3-2. 사랑하는 사람에게 받고 싶은 선물은? (복수선택)")
for value, author in options_simulation_2.items() : 
    st.checkbox(f"{value}", key=f"simulation_{author}_2")

st.markdown('\n')

#5-3. 12번 문항 : 시뮬레이션
options_simulation_3 = {
    "감정을 글로 풀어 편지나 일기로 전달한다." : "BW", 
    "스스로를 탓하며 잠시 거리를 둔다." : "DO", 
    "조용히 곁에 있어주고 말없이 위로한다." : "HG",
    "분위기를 전환시키기 위해 농담을 건넨다." : "SF",    
    "격렬히 싸우고 빠르게 화해한다." : "EH", 
    "사소한 일에 연연하지 않고 자연스럽게 풀어간다." : "KYS",
    "문제의 원인을 논리적으로 분석하고 해결책을 찾는다." : 'GO',         
    "깊은 대화를 통해 서로를 이해한다." : "HH",
    "불만을 직설적으로 표현하며 갈등의 본질에 접근한다." : "KSY", 
    "감정에 휘둘리지 않고 무심하게 넘긴다." : "AC"
}

st.markdown("Q3-3. 연인과 갈등이 생겼을 때, 원하는 연인의 행동은? (복수선택)")
for value, author in options_simulation_3.items() : 
    st.checkbox(f"{value}", key=f"simulation_{author}_3")

st.divider()
st.markdown("#### 4.명문장 픽 ✍")
st.markdown('\n')

#6-1. 16번 문항 : 명문장 픽
st.markdown("Q4-1. 다음 중 마음에 드는 문장을 선택하세요 (복수선택)")

for emblem, author_cd in author_emblem_dict_1.items() : 
    author = f'{author_cd}_4'
    st.checkbox(f"{emblem}", key=author)


if st.button('제출', type='primary') : 
#    for i in (1, 10) : 
#        options_tendency_{i}[tendency_{i}]
#    st.write(options_tendency_1[tendency_1])
#    selected_mbti = [options_tendency_9[mbti] for mbti in tendency_1.keys() if st.session_state.get(mbti)]
    
    basic_check = []
    basic_total_dict = {
        basic_1 : options_basic_1, 
        basic_2 : options_basic_2,
        basic_3 : options_basic_3
    }

    for i, v in basic_total_dict.items() : 
        basic_check.append(v[i])
    # st.write(basic_check)

    
    tendency_check = []
    tendency_total_dict = {
        tendency_1 : options_tendency_1,
        tendency_2 : options_tendency_2,
        tendency_3 : options_tendency_3,
        tendency_4 : options_tendency_4,
        tendency_5 : options_tendency_5,
        tendency_6 : options_tendency_6,
    }

    for i, v in tendency_total_dict.items() : 
        tendency_check.append(v[i])
    # st.write(tendency_check)


    mbti_check = []
    selected_mbti = [options_tendency_7[mbti] for mbti in options_tendency_7.keys() if st.session_state.get(mbti)]

    # 선택 결과 출력
    if selected_mbti:
        for mbti in selected_mbti :
            mbti_check.append(mbti)
    # st.write(mbti_check)

    simulation_check = []
    # selected_simul_1 = [options_simulation_1[author] for author in options_simulation_1.keys() if st.session_state.get(author)]
    # selected_simul_2 = [options_simulation_2[author] for author in options_simulation_2.keys() if st.session_state.get(author)]
    # selected_simul_3 = [options_simulation_3[author] for author in options_simulation_3.keys() if st.session_state.get(author)]

    selected_options_1 = [
        value for value, author in options_simulation_1.items()
        if st.session_state.get(f"simulation_{author}_1")
    ]

    selected_options_2 = [
        value for value, author in options_simulation_2.items()
        if st.session_state.get(f"simulation_{author}_2")
    ]

    selected_options_3 = [
        value for value, author in options_simulation_3.items()
        if st.session_state.get(f"simulation_{author}_3")
    ]
    
    if selected_options_1:
        for option in selected_options_1:
            simulation_check.append(options_simulation_1[option])
    
    if selected_options_2:
        for option in selected_options_2:
            simulation_check.append(options_simulation_2[option])    
    
    if selected_options_3:
        for option in selected_options_3:
            simulation_check.append(options_simulation_3[option])
    
    # st.write(simulation_check)
        
    emblem_check = []
    
    selected_emblem_1 = [
        emblem for emblem, author_cd in author_emblem_dict_1.items()
        if st.session_state.get(f"{author_cd}_4")
    ]

    if selected_emblem_1:
        for emblem in selected_emblem_1:
            emblem_check.append(author_emblem_dict_1[emblem])
    
    # st.write(emblem_check)

    author_tendency_scores = {author: 0 for author in author_list}

    for item in tendency_check:
        if item in author_list :
            # 직접 작가 이름이 나오면 점수 추가
            author_tendency_scores[item] += 10
        elif item in group_to_authors:
            # 그룹 키면 해당 작가들에게 점수 추가
            for author in group_to_authors[item]:
                author_tendency_scores[author] += 10

    author_mbti_scores = {author: 0 for author in author_list}

    for item in mbti_check:
        if item in author_list :
            # 직접 작가 이름이 나오면 점수 추가
            author_mbti_scores[item] += 10
        elif item in group_to_authors:
            # 그룹 키면 해당 작가들에게 점수 추가
            for author in group_to_authors[item]:
                author_mbti_scores[author] += 10

    author_simulation_scores = {author: 0 for author in author_list}

    for item in simulation_check:
        if item in author_list :
            # 직접 작가 이름이 나오면 점수 추가
            author_simulation_scores[item] += 10
        elif item in group_to_authors:
            # 그룹 키면 해당 작가들에게 점수 추가
            for author in group_to_authors[item]:
                author_simulation_scores[author] += 10


    author_emblem_scores = {author: 0 for author in author_list}

    for item in emblem_check:
        if item in author_list :
            # 직접 작가 이름이 나오면 점수 추가
            author_emblem_scores[item] += 10
        elif item in group_to_authors:
            # 그룹 키면 해당 작가들에게 점수 추가
            for author in group_to_authors[item]:
                author_emblem_scores[author] += 10


    df_scores = pd.DataFrame({
        "author_cd": author_list,
        "성향점수": [author_tendency_scores[author] for author in author_list],
        "MBTI점수": [author_mbti_scores[author] for author in author_list],
        "연애점수": [author_simulation_scores[author] for author in author_list], 
        "명문장점수": [author_emblem_scores[author] for author in author_list] 
    })

    # 총점 컬럼 추가
    df_scores["총점"] = df_scores["성향점수"] + df_scores["MBTI점수"] + df_scores["연애점수"] + df_scores["명문장점수"]

    # 컬럼 순서 변경 (총점을 Author 옆으로 이동)
    df_scores = df_scores[["author_cd", "총점", "성향점수", "MBTI점수", "연애점수", "명문장점수"]]

    # 총점 기준으로 내림차순 정렬
    df_total = pd.merge(author_db, df_scores, left_on='author_cd', right_on='author_cd', how='inner')

    df_scores = df_total[["author_nm", "총점", "성향점수", "MBTI점수", "연애점수", "명문장점수"]]
    df_scores.rename(columns={'author_nm': '작가', '명문장점수': '명문장 점수'}, inplace=True)

    df_scores = df_scores.sort_values(by=["총점", "성향점수", "연애점수"], ascending=False)

    real_df_total = df_total

    if basic_check[0] == "500" : 
        real_df_total = real_df_total[real_df_total["page"] <= 500]
    elif basic_check[0] == "400" : 
        real_df_total = real_df_total[real_df_total["page"] <= 400]
    elif basic_check[0] == "300" : 
        real_df_total = real_df_total[(real_df_total["page"] <= 300) | (real_df_total["author_nm"]=='한강')]

    if basic_check[1] == 0 :
        real_df_total = real_df_total[real_df_total["foreign_yn"] == 0]
    elif basic_check[1] == 1 :
        real_df_total = real_df_total[real_df_total["foreign_yn"] == 1]

    if basic_check[2] == 1 :
        real_df_total = real_df_total[real_df_total["author_cd"] != 'KSY']

    real_df_total = real_df_total.sort_values(by=["총점", "성향점수", "연애점수"], ascending=False)
    target_author = real_df_total.head(1)

    st.header(f"{target_author['author_nm'].iloc[0]} 🎉")
    
    img = Image.open(f"image/{target_author['author_cd'].iloc[0]}.png")
    st.image(img, width=200, caption=f'{target_author['lifetime'].iloc[0]}, {target_author['country'].iloc[0]}')
    st.markdown(f"[디 에센셜 설명 페이지 연결🔗](https://event.kyobobook.co.kr/desntl/detail/{target_author['book_seq'].iloc[0]})")

    
    st.markdown(f"**1) 작가 소개** : ")
    st.markdown(f"<small>{target_author['explain_1'].iloc[0]} <br> {target_author['explain_2'].iloc[0]} </small>", unsafe_allow_html=True)
    st.markdown(f"**2) 페이지 수** : {target_author['page'].iloc[0]} \n")
    st.markdown(f"**3) 수록 작품 📚** : {target_author['masterpiece_1'].iloc[0]}, {target_author['masterpiece_2'].iloc[0]}, {target_author['masterpiece_3'].iloc[0]} \n")
    st.markdown(f"""
    **4) 명문장 ✍🏻** :  
    <small>
        1. {target_author['prestigious emblem_1'].iloc[0]} <br>
        2. {target_author['prestigious emblem_2'].iloc[0]} <br>
        3. {target_author['prestigious emblem_3'].iloc[0]} <br>
        4. {target_author['prestigious emblem_4'].iloc[0]} <br>
        5. {target_author['prestigious emblem_5'].iloc[0]} <br>
    </small>
    """, unsafe_allow_html=True)


    basic_answer_list = []
    if basic_1 in ["500p 이하", "400p 이하", "300p 이하"] :
        basic_answer_list.append(f"✅ {basic_1}")
    if basic_2 in ["한국", "해외"] : 
        basic_answer_list.append(f"✅ {basic_2} 작가")
    if basic_3 == "시는 어려워요" : 
        basic_answer_list.append(f"✅ 시집 제외")

    basic_list_join = ", ".join(basic_answer_list)

    st.markdown(f"**5) 상세 점수 🎯** : <br> {basic_list_join} <br><small>많은 작가에 관심을 가지기 바라는 마음에 아래 점수는 필터링을 반영하지 않았습니다 😊</small>", unsafe_allow_html=True)
    st.markdown('\n')


    # dataframe 출력
    st.dataframe(df_scores)








# #4-7. 10번 문항 : 성향 
# options_tendency_7 = {
#     "작은 변화에도 의미를 찾으며 적응한다.": "KYS",
#     "감정을 솔직하게 표출하고 본질을 직시한다.": "KSY",
#     "고민하지 않고 즉시 행동에 나선다.": "EH",
#     "그 일이 내 삶에 어떤 의미가 있는지 깊이 고민한다.": "HH",
#     "감정이 흐르는 대로 자연스럽게 반응한다. ": "BW"
# }

# tendency_7 = st.radio(
# 'Q2-7. 예상치 못한 일이 생겼을 때, 당신의 반응은?', list(options_tendency_7.keys())
# )

# st.markdown('\n')


# st.markdown('\n')

#4-2. 5번 문항 : 성향 
# options_tendency_2 = {
#     "냉철하고 비판적인 시각": "group_a",
#     "따뜻하지만 때로는 허무한 시각": "group_b",
#     "감상적이고 내면 성찰적인 시각": "group_c",
#     "직설적이고 현실적인 시각": "group_d"
# }

# tendency_2 = st.radio(
# 'Q2-2. 세상을 바라보는 당신의 시각은?', list(options_tendency_2.keys())
# )

# st.markdown('\n')






# %%
