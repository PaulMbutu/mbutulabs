import streamlit as st 
from all_the_pages.Dashboards import the_titanic, bank_sales
import base64
import time
from streamlit_option_menu import option_menu
import streamlit_antd_components as sac

def hide_streamlit_header_footer():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
def display_existing_messages():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
class Home:
    def __init__(self) -> None:
        self.file_path = "57731.gif"

    def get_base64_of_bin_file(self):
        try:
            with open(self.file_path, "rb") as file: 
                binary_data = file.read()
                base64_data = base64.b64encode(binary_data).decode("utf-8")
                return base64_data
        except Exception as e:
            print(f"Error: {e}")
            return None

    def set_bg_hack(self):
        main_bg_ext = "gif"
        bg_base64 = self.get_base64_of_bin_file()
        if bg_base64:
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background: url(data:image/{main_bg_ext};base64,{bg_base64});
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                    background-position: center;
                    height: 100vh;
                    overflow-x: hidden;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

    def show_it(self):
        st.title("MbutuLabs")
        st.write("Welcome to mbutulabs an interesting web app that can privide you with some usefull applications. \
                 It also serves as a portfolio so if theres a product you find functional and would like to develop a similar one,  \
                 feel free to make a request.\
                 You can interact with the chatbot in this hompage.")
        
        hide_streamlit_header_footer()
        display_existing_messages()
        if "messages" not in st.session_state:
            st.session_state["messages"] = []
        for message in st.session_state["messages"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if prompt := st.chat_input("What's up?"):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state["messages"].append({"role":"user","content":prompt})
            response=f"Echo: {prompt}"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state["messages"].append({"role":"assistant","content":response})

        
        self.set_bg_hack()

# Creating an instance of the Home class and calling its method to display content
home = Home()

# Main function to run the Streamlit app

def main():
    """ 
    with st.sidebar:
            selected = option_menu(
            menu_title = "Main Menu",
            options = ["Home","Dashboards","Apps","Contact Us"],
            icons = ["house","gear","activity","envelope"],
            menu_icon = "cast",
            default_index = 0,
            #orientation = "horizontal",
            

        )
    with st.sidebar:
            selected=sac.tree(
                                items=[
                                        sac.TreeItem('Home', icon='house'),
                                        sac.TreeItem('Dashboards', icon='table',
                                                        children=[
                                                                    sac.TreeItem('The Titanic'),
                                                                    sac.TreeItem('Bank Sales')
                                                                ]),
                                        sac.TreeItem('Apps', icon="activity", disabled=True),
                                        sac.TreeItem('Contact',icon='envelope',disabled=True)
                                        ],
                                label='MENU', align='left', size='xl',open_all=True
                            )
    """
    with st.sidebar:
        selected=sac.menu(
                    items   =   [
                                    sac.MenuItem('Home',icon='house'),
                                    sac.MenuItem('Dashboards',icon='table',children=['The Titanic','Bank Sales']),
                                    sac.MenuItem('Apps',icon='activity',disabled=True),
                                    sac.MenuItem('Contact',icon='envelope',disabled=True)
                                ]
                )

    
    if selected == "Home":
        home.show_it()
    if selected==   'Dashboards':
        open_this=1
    if selected == "The Titanic":
        the_titanic()
    if selected == "Bank Sales":
        bank_sales()
    if selected == "Apps":
        #no need for headers
        st.header("Some apps comming soon")

    if selected == "Contact Us":
        #no need for headers
        st.header("Ways for contact")

if __name__ == "__main__":
    main()







