import streamlit as st
import base64
import pandas as pd
import plotly.express as px

def the_titanic():
    st.title("The Titanic")
    st.header("Take A look at the Titanic")
    st.markdown("This is some data from the doomed titanic ship. It had a variety of people emberking from 3 different habours.")
    st.markdown("Southampton: The Titanic set sail from Southampton, England, on April 10th, 1912.")
    st.markdown("Cherbourg: After leaving Southampton, the ship stopped in Cherbourg, France, to pick up additional passengers.")
    st.markdown("Queenstown: The final pickup point was in Queenstown (now Cobh), Ireland, where the Titanic made its last stop before heading towards New York.")

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


    PassengerId    =   df['PassengerId'].unique().tolist()
    Survived       =   df['Survived'].tolist()
    Pclass         =   df['Pclass'].tolist()
    Sex            =   df['Sex'].tolist()
    Age            =   df['Age'].tolist()
    SibSp          =   df['SibSp'].unique().tolist()
    Parch          =   df['Parch'].unique().tolist()
    Ticket         =   df['Ticket'].unique().tolist()
    Fare           =   df['Fare'].unique().tolist()
    Cabin          =   df['Cabin'].unique().tolist()
    Embarked       =   df['Embarked'].unique().tolist()
    Southampton_count   = df['Embarked'].value_counts()['S']  # Get count of value 1 (survived)
    Cherbourg_count     = df['Embarked'].value_counts()['C']  # Get count of value 0 (deceased) or 0 if it doesn't exist
    Queenstown_count    = df['Embarked'].value_counts()['Q']  # Get count of value 0 (deceased) or 0 if it doesn't exist

    # Create a dictionary with counts and set an index (e.g., "Status")
    d = {
            "Origin": ["Southampton", "Cherbourg","Queenstown"],
            "Count": [Southampton_count, Cherbourg_count,Queenstown_count]
        }

    # Create DataFrame with the dictionary and explicit index
    df_emberked     =   pd.DataFrame(data=d)
    Emberked_chart  =   px.bar(df_emberked,
                               x=df_emberked["Origin"],
                               y=df_emberked['Count']
                               )
    st.plotly_chart(Emberked_chart)


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


    
    #with st.spinner(text='In progress'):
        #time.sleep(3)
        #st.success('Done')

    
    survived_males = df.query("Survived==1")["Sex"].value_counts()["male"]  # Get count of value 1 (survived)
    total_male = df["Sex"].value_counts()["male"]
    deceased_males=total_male-survived_males

    # Create a dictionary with counts and set an index (e.g., "Status")
    d = {
            "Status": ["Survived males", "Deceased males"],
            "Count": [survived_males, deceased_males]
        }

    # Create DataFrame with the dictionary and explicit index
    df_survived = pd.DataFrame(data=d)
    
    Male_Survival_pie_chart  =   px.pie(
                            df_survived,  # Data source (DataFrame)
                            names=df_survived['Status'],  # Column names for pie slices (from index)
                            values=df_survived['Count'],  # Column containing values for pie slice sizes
                            labels={'Status': 'Survival Status', 'Count': 'Number of People'},  # Customize labels
                            color=df_survived['Status'],  # Use status as color reference for slices
                            title='Male Survival Rate',  # Set chart title
    )

    survived_females = df.query("Survived==1")["Sex"].value_counts()["female"]  # Get count of value 1 (survived)
    total_female = df["Sex"].value_counts()["female"]
    deceased_females=total_female-survived_females

    # Create a dictionary with counts and set an index (e.g., "Status")
    d = {
            "Status": ["Survived females", "Deceased females"],
            "Count": [survived_females, deceased_females]
        }

    # Create DataFrame with the dictionary and explicit index
    df_survived = pd.DataFrame(data=d)
    
    Female_Survival_pie_chart  =   px.pie(
                            df_survived,  # Data source (DataFrame)
                            names=df_survived['Status'],  # Column names for pie slices (from index)
                            values=df_survived['Count'],  # Column containing values for pie slice sizes
                            labels={'Status': 'Survival Status', 'Count': 'Number of People'},  # Customize labels
                            color=df_survived['Status'],  # Use status as color reference for slices
                            title='Female Survival Rate',  # Set chart title
    )
    
    # Display the charts
    col1,col2=st.columns(2)
    with col1:
        st.plotly_chart(Male_Survival_pie_chart,use_container_width=True)
    with col2:
        st.plotly_chart(Female_Survival_pie_chart,use_container_width=True)
    #st.markdown("a check for null values")
    selected_columns = ['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']

    # Count the number of null values in each of the selected columns
    null_counts = df[selected_columns].isnull().sum()

    # Print the results
    #st.dataframe(null_counts)
    #st.dataframe(df)
    


def bank_sales():
    st.title("Bank Sales Data")
    st.header("Take A look at this BAnks data")


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




    excel_file = "info_datasets/Bank.xlsx"
    sheet_name = "DATA"

    df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    header=0)
    st.dataframe(df)
    st.write(df.describe())
    st.write(list(df.columns))
    st.plotly_chart(px.histogram(df["age"].to_list(),title="The Age Distribution of Curstomers"))
    st.plotly_chart(px.histogram(df["job"].to_list(),title="The Job Distribution of Curstomers"))
    st.plotly_chart(px.histogram(df["marital"].to_list(),title="The Marital Status of Curstomers"))
    st.plotly_chart(px.histogram(df["education"].to_list(),title="The Education of Curstomers"))
    st.plotly_chart(px.histogram(df["default"].to_list(),title="The Loan default status of Curstomers"))
    st.plotly_chart(px.histogram(df["housing"].to_list(),title="The housing of Curstomers")) 
    st.plotly_chart(px.histogram(df["loan"].to_list(),title="The loan status of Curstomers"))
    st.plotly_chart(px.histogram(df["duration"].to_list(),title="The Loan durations of Curstomers"))











