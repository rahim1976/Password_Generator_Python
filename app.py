import streamlit as st
import random

st.set_page_config(
    page_title="Password Generator",
    page_icon="🔒",
    layout="centered"
)

# Sidebar Start
with st.sidebar:
    st.title("About")
    st.markdown("### Creator:")
    st.write("Rahim Ali")
    
    st.markdown("### How It Works")
    st.markdown("""
    1. Enter the number of passwords you want to generate
    2. Specify the length for each password
    3. Click 'Generate Passwords' button
    4. Copy the generated passwords using the copy button
    """)
    
    st.markdown("### Features")
    st.markdown("""
    - Generate multiple passwords at once
    - Customizable password length
    - One-click copy functionality
    - Secure random generation
    - Supports all ASCII characters
    """)
# Sidebar End

# Main content Start
st.title("Password Generator🔒")
st.markdown("### *Generate Strong Passwords in Seconds*")
st.markdown('> *"Your password is the key to your digital kingdom - make it strong!"*')

# Characters From Which Password Will Be Generated
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$%&*.'

# Columns For Number Input Fields
col1, col2 = st.columns(2)

with col1:
    number = st.number_input("Number of Passwords", min_value=1, max_value=50, value=1)

with col2:
    length = st.number_input("Password Length", min_value=8, max_value=50, value=12)

# Password Generation Button
if st.button("Generate Passwords"):
    st.markdown("### Generated Passwords:")
    
    # Container For Password
    password_container = st.container()
    
    with password_container:
        for _ in range(number):
            password = ''.join(random.choice(chars) for _ in range(length))
            # Create a row with password and copy button
            col1, col2 = st.columns([3, 1])
            with col1:
                st.code(password, language="text")
            with col2:
                if st.button("Copy", key=f"copy_{_}"):
                    st.write("Copied to clipboard!")
                    st.code(password, language="text")

# Footer Start
st.markdown("---")
st.markdown("© 2024 All Rights Reserved | Created by Rahim Ali") 
# Footer End

# Main content End
