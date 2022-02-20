import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('研究オリジナルTシャツ！')

img=Image.open('utme.JPG')
st.image(img,caption='utme',use_column_width=True)

