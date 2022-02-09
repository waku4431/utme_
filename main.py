import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('研究オリジナルTシャツ　公開！')

pass_true=st.secrets["password"]
pass_st=0
pass_in = st.text_input('PASSWORD')

if pass_st==0:
  if pass_in==pass_true:
    #st.write("OK")
    pass_st=1
  elif pass_in=='':
    st.write("パスワードを入力し、Enterキーを押してください")
  else:
    st.write("パスワードが違います")


  if pass_st==1:

    img=Image.open('utme.JPG')
    st.image(img,caption='utme',use_column_width=True)

