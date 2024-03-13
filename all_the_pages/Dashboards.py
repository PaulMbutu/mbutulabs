import streamlit as st
import base64
import pandas as pd
import plotly.express as px

def the_titanic():
    st.title("The Titanic")
    st.header("Take A look at the Titanic")
    st.markdown("This is some data from the doomed titanic ship. It had a variety of people emberking from 3 different habours")

    def set_bg_hack(main_bg):
        '''
        A function to unpack an image from root folder and set as bg.
    
        Returns  The background.
        '''
        # set bg name
        main_bg_ext = "gif"
            
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed; /* Keeps the background fixed while scrolling */
                background-position: center;
                height: 100vh; /* Ensures full viewport height */
                overflow-x: hidden; /* Hides horizontal overflow */
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg_hack(r"57731.gif")


    def mode(l1:list,l2:list):#l1 list of counts l2 list of values
        h_c=sorted(l1,reverse=True)[0] #highest count
        index_h_c=l1.index(h_c)
        return f"{l2[index_h_c]} occurs {h_c} times"

    excel_file = "info_datasets/Titanic.xlsx"
    sheet_name = "DATA"

    df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    header=0)
    #st.dataframe(df)

    PassengerId    =   df['PassengerId'].unique().tolist()
    Survived       =   df['Survived'].unique().tolist()
    Pclass         =   df['Pclass'].unique().tolist()
    Sex            =   df['Sex'].tolist()
    Age            =   df['Name'].tolist()
    SibSp          =   df['SibSp'].unique().tolist()
    Parch          =   df['Parch'].unique().tolist()
    Ticket         =   df['Ticket'].unique().tolist()
    Fare           =   df['Fare'].unique().tolist()
    Cabin          =   df['Cabin'].unique().tolist()
    Embarked       =   df['Embarked'].unique().tolist()
    Sex            =   df['Sex'].tolist()

    df = pd.DataFrame(Sex, columns=['Sex'])
    px.pie()
    pie_chart = px.pie(
                    df['Sex'].value_counts(),
                    men     =df['Sex'].value_counts().index, 
                    y       =df['Sex'].value_counts().values, 
                    labels  ={'x': 'Sex', 'y': 'Count'},
                    color   =df['Sex'].value_counts().index, 
                    title   ='Sex Distribution')

    # Display the chart
    st.plotly_chart(pie_chart,use_container_width=True)
    st.dataframe(df['Sex'])
    #with st.spinner(text='In progress'):
        #time.sleep(3)
        #st.success('Done')
    


def bank_sales():
    st.markdown("coming soon")












