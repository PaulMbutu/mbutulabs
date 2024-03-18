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
    Survived       =   df['Survived'].tolist()
    Pclass         =   df['Pclass'].tolist()
    Sex            =   df['Sex'].tolist()
    Age            =   df['Name'].tolist()
    SibSp          =   df['SibSp'].unique().tolist()
    Parch          =   df['Parch'].unique().tolist()
    Ticket         =   df['Ticket'].unique().tolist()
    Fare           =   df['Fare'].unique().tolist()
    Cabin          =   df['Cabin'].unique().tolist()
    Embarked       =   df['Embarked'].unique().tolist()

    df_sex = pd.DataFrame(Sex, columns=['Sex'])
    sex_pie_chart = px.pie(
                    df_sex['Sex'].value_counts(),
                    names   =df_sex['Sex'].value_counts().index, 
                    values  =df_sex['Sex'].value_counts().values, 
                    labels  ={'x': 'Sex', 'y': 'Count'},
                    color   =df_sex['Sex'].value_counts().index, 
                    title   ='Sex Distribution')
    
    survived_count = df['Survived'].value_counts()[1]  # Get count of value 1 (survived)
    deceased_count = df['Survived'].value_counts().get(0, 0)  # Get count of value 0 (deceased) or 0 if it doesn't exist

    # Create a dictionary with counts and set an index (e.g., "Status")
    d = {
            "Status": ["Survived", "Deceased"],
            "Count": [survived_count, deceased_count]
        }

    # Create DataFrame with the dictionary and explicit index
    df_survived = pd.DataFrame(data=d)
    
    Survived_pie_chart  =   px.pie(
                            df_survived,  # Data source (DataFrame)
                            names=df_survived['Status'],  # Column names for pie slices (from index)
                            values=df_survived['Count'],  # Column containing values for pie slice sizes
                            labels={'Status': 'Survival Status', 'Count': 'Number of People'},  # Customize labels
                            color=df_survived['Status'],  # Use status as color reference for slices
                            title='Survival Rate on the Titanic',  # Set chart title
    )
    
    # Display the charts
    col1,col2=st.columns(2)
    with col1:
        st.plotly_chart(sex_pie_chart,use_container_width=True)
    with col2:
        st.plotly_chart(Survived_pie_chart,use_container_width=True)

    st.dataframe(df)
    #with st.spinner(text='In progress'):
        #time.sleep(3)
        #st.success('Done')
    


def bank_sales():
    st.markdown("coming soon")












