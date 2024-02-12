import streamlit as st
import base64
st.title("Contacts")
st.write("So you think",st.session_state["my_input"])
def get_base64_of_bin_file2(file_path):
    try:
        with open(file_path, "rb") as file:
            # Read the binary data from the file
            binary_data = file.read()
            # Encode the binary data as Base64
            base64_data = base64.b64encode(binary_data).decode("utf-8")
            return base64_data
    except Exception as e:
        print(f"Error: {e}")
        return None

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
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

set_bg_hack(r"C:\Users\manch\OneDrive\Documents\dev\mbutulabs\57731.gif")