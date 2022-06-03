import streamlit as st
import numpy as np
import pandas as pd
import math
from PIL import Image
import time

st.title("test")

st.write("プレグレスバーの表示")
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # print(i)
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!!!!!!'

left_column,right_column = st.columns(2) 
button1 = left_column.button('右カラムに文字を表示')
if button1:
    right_column.write('ここは右カラムです')

expander1 = st.expander('お問い合わせ1')
expander1.write('問い合わせ内容１の回答')
expander2 = st.expander('お問い合わせ2')
expander2.write('問い合わせ内容２の回答')
expander3 = st.expander('お問い合わせ3')
expander3.write('問い合わせ内容３の回答')


# left_column,center_column,right_column = st.columns(3) 
# button1 = left_column.button('右カラムに文字を表示')
# if button1:
#     right_column.write('ここは右カラムです')

# button2 = center_column.button('左カラムに文字を表示')
# if button2:
#     left_column.write('ここは左カラムです')

# button3 = right_column.button('中央カラムに文字を表示')
# if button3:
#     center_column.write('ここは中央カラムです')

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))


# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：',text,'です。'
# 'コンディション：', condition




# 'あなたの好きな数字は、',option,'です。'




# if st.checkbox("Show Image"):
#     img = Image.open("sample.jpg")
#     st.image：img,caption='Kokei Imanishi' , use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[5,5]+[35.69,139.70],
#     columns = ['lat','lon'])
# #st.bar_chart(df)
# #df
# st.map(df)

# #動的な表　
# #st.dataframe(df.style.highlight_max(axis=0),width=500,height=500)

# #静的な表　ただ表を表示させたい時
# #st.table(df.style.highlight_max(axis=0))
