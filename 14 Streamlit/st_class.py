import streamlit as st
import pandas as pd
import numpy as np
import time

art = """
   __                         
  /__\ ___  __ _  __ _ _ __   
 / \/// _ \/ _` |/ _` | '_ \  
/ _  \  __/ (_| | (_| | | | | 
\/ \_/\___|\__, |\__,_|_| |_| 
           |___/              
"""

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon=":zipper-mouth_face:")

st.title('This is a title')
st.header('This is a header')
st.subheader('This is the subheader')
st.text(art)

# Write
st.write('This is the write method!')

# Magic Commands
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(df)

# CHARTS AND MAPS
# Line chart
chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
st.line_chart(chart_data)
# Maps
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

# # INPUT WIDGETS
# # Text Area
# text_area = st.text_area('Enter some text', max_chars=1000, placeholder='Enter some text')
# # Text Input
# st.text_input('Email Address', placeholder='Enter email')

# Checkbox
if st.checkbox('Show dataframe'):
      chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['a', 'b', 'c'])
      st.dataframe(chart_data)

# Select box

df=pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox('Which number do you like best?', df['first column'])
st.write('You selected: ', option)


# side bar
st.sidebar.selectbox(
    'Sidebar Numbers?',
     df['second column'])

# side by side widget
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo! The button has been pressed!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations..")


# Progress Bar
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'...and now we\'re done!'

# LaTeX
st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')
