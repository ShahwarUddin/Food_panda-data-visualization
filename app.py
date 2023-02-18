import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df=pd.read_csv("pakpanda.csv")

# print(df.head())
# print(df.columns)
# Index(['Unnamed: 0', 'budget', 'latitude', 'longitude',
#        'minimum_delivery_time', 'minimum_order_amount', 'minimum_pickup_time',
#        'name', 'post_code', 'rating', 'review_number',
#        'review_with_comment_number', 'vertical', 'vertical_parent',
#        'delivery_provider', 'is_active', 'is_new', 'is_promoted', 'city',
#        'timezone', 'dine_in', 'main_cuisine', 'country'],
#       dtype='object')
list_of_cities=list(df["city"].unique())
list_of_cities.insert(0,"All_Over_Pakistan")

st.sidebar.title('Foodpanda Pakistan')

selected_cities = st.sidebar.selectbox('Select a state',list_of_cities)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[7:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[7:]))
graph = st.sidebar.selectbox('Select Any Grpah',["bar (cat-num)","line (cat-num)","map_box (num-num)","scatter_plot (num_num)"])
plot = st.sidebar.button('Plot Graph')


primaryColor="#3C97FF"
base="dark"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#3C97FF"
textColor="#262730"
font="sans serif"



if plot:

    
    if selected_cities == 'All_Over_Pakistan':
        try:
            st.text('Size represent primary parameter')
            st.text('Color represents secondary parameter')
            if graph == "bar (cat-num)":
                fig=px.bar(df,x=primary,y=secondary)
                st.plotly_chart(fig,use_container_width=True)
    
            elif graph == "line (cat-num)":
                fig=px.line(df,x=primary,y=secondary)
                st.plotly_chart(fig,use_container_width=True)

            elif graph == "scatter_plot (num_num)":
                fig=px.scatter(df,x=primary,y=secondary)
                st.plotly_chart(fig,use_container_width=True)

            elif graph == "map_box (num-num)":
                fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", size=primary, color=secondary, zoom=4,size_max=35,
                mapbox_style="carto-positron",width=1200,height=700,hover_name='name')
                st.plotly_chart(fig,use_container_width=True)
            

        except:
            st.header('Canot possible to plot this graph on these columns')
       
    else:
        
        
        state_df = df[df['city'] == selected_cities]
        
        try:
            st.text('Size represent primary parameter')
            st.text('Color represents secondary parameter')
            if graph == "bar (cat-num)":
                fig=px.bar(state_df,x=primary,y=secondary)
                st.plotly_chart(fig,use_container_width=True)
            
            elif graph == "line (cat-num)":
                fig=px.line(state_df,x=primary,y=secondary)
                st.plotly_chart(fig,use_container_width=True)
            elif graph == "scatter_plot (num_num)":
                fig=px.scatter(state_df,x=primary,y=secondary)
                st.plotly_chart(fig,use_container_width=True)
            elif graph == "map_box (num-num)":
                fig = px.scatter_mapbox(state_df, lat="latitude", lon="longitude", size=primary, color=secondary, zoom=4,size_max=35,
                mapbox_style="carto-positron",width=1200,height=700,hover_name='name')
                st.plotly_chart(fig,use_container_width=True)
            

        except:
            st.header('Canot possible to plot this graph on these columns')


