import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('研究オリジナルTシャツ　公開！')

# st.write('DataFrame')

# df=pd.DataFrame({
#     '１列目':[1,2,3,4],
#     '２列目':[10,20,30,40]
# })

# st.write(df)
# st.write(df.style.highlight_max(axis=1))
# st.table(df.style.highlight_max(axis=0))

# """

# # 章
# ## 節
# ### 項

# """

# df=pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# st.line_chart(df)#折れ線グラフ
# st.area_chart(df)#折れ線塗りつぶし
# st.bar_chart(df)#棒グラフ

# df=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)

img=Image.open('utme.JPG')
st.image(img,caption='utme',use_column_width=True)

#st.write('プログレスバーの表示')
# 'Start!!'

# latest_iteration=st.empty()
# bar=st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration{i+1}')
#     bar.progress(i+1)
#     time.sleep(0.3)
