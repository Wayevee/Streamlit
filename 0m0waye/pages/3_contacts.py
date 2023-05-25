import streamlit as slt

slt.title("Contacts")

def local_css(file_name):
    with open(file_name) as f:
        slt.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css(f'style.css')

slt.write("Drop Your Messages Below")

contact_form = """
<form action="https://formsubmit.co/vhicktarh@gmail.com" method="POST">
    <input type= "Hidden" name="_captcha" value= "false">
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder= "Your E-mail" required>
     <textarea name= "Message" Placeholder= "Your Message Here" required></textarea>
     <button type="submit">Send</button>
</form>
    """

left_column, right_column = slt.columns(2)
with left_column:
    slt.markdown(contact_form, unsafe_allow_html = True)
with right_column:
    slt.empty()
