import streamlit as st 
from all_the_pages.Dashboards import the_titanic, bank_sales
import base64
import time




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
        st.write("Welcome to mbutulabs an interesting web app that can privide you with some usefull applications. It also serves as a portfolio so if theres a product you find functional and would like to develop a similar one,  feel free to make a request.")
        if "my_input" not in st.session_state:
            st.session_state["my_input"] = ""
        my_input = st.text_input("What do you think", st.session_state["my_input"])
        submit = st.button("Submit")
        if submit:
            st.session_state["my_input"] = my_input
            st.write("So you think:", my_input)
        
        self.set_bg_hack()

# Creating an instance of the Home class and calling its method to display content
home = Home()

# Main function to run the Streamlit app

def main():
    with st.sidebar:
        st.sidebar.title("Navigation")

        with st.sidebar.expander("Home"):
            # Use buttons for dashboard selection
            the_home_button = st.button("homepage")


        with st.sidebar.expander("Dashboards"):
            # Use buttons for dashboard selection
            the_titanic_button = st.button("The Titanic")
            bank_sales_button = st.button("Bank Sales")

        with st.sidebar.expander("Apps"):
            st.markdown("Some apps you can use are coming soon.")

        with st.sidebar.expander("Contacts"):
            st.markdown("Some ways of contacting me.")


        st.markdown(
            """
            <style>
            button {
                background: none!important;
                border: none;
                padding: 0!important;
                color: white !important;
                text-decoration: none;
                cursor: pointer;
                border: none !important;
            }
            button:hover {
                text-decoration: none;
                color: white !important;
            }
            button:focus {
                outline: none !important;
                box-shadow: none !important;
                color: white !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Handle dashboard selection based on button clicks
    if not the_home_button and not the_titanic_button and not bank_sales_button:
        home.show_it()
    elif the_titanic_button:
        the_titanic()
    elif bank_sales_button:
        bank_sales()
    elif the_home_button:
        # If no button is clicked, show the home page
        home.show_it()

if __name__ == "__main__":
    main()





