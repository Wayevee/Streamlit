from PIL import Image
import requests
import streamlit as slt
import streamlit_lottie

slt.set_page_config(page_title= "My WebPage", page_icon= ":tada:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
        with open(file_name) as f:
            slt.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("0m0waye\style.css")

lottie_coding =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_dews3j6m.json")
img_contact_form = Image.open("images\images.jfif")
with slt.container():
    slt.subheader ("HI I am Omowaye Victor :wave:")
    slt.title("A Data Analyst")
    slt.write("I am passionate about finding ways tonuse Python and VBA to be more effective")
    slt.write("[Learn More >](https://wayevee.github.io/WayeA/)")



with slt.container():
    slt.write("---")
    left_column, right_column = slt.columns(2)
    with left_column:
        slt.header("What I do")
        slt.write("##")
        slt.write(
        """
        Ability to demonstrate the data proficiency, flair and mastery on data manipulation to solve or answer organisations questions should be a habit of a good analyst.
         This quality would help the analyst develop the ability to spot when things or data issue are very wrong. I have seen an analyst produced an analysis and make recommendations based on dirty data.
         The analyst must be comfortable with large volumes of data from disparate data sources, and be able to spot relevant patterns and trends.
It is important to be able to look at disjoint thought or action, see pattern that the ordinary people will ignore and also translate those less obvious pattern into business meanings.
Rarely do we see people born with this skill, but this can be developed.
         """
        )
#with right_column:
    #streamlit_lottie(lottie_coding)


with slt.container():
    slt.write("---")
    slt.header("My Projects")
    slt.write("##")
    image_column,text_column = slt.columns((2, 4))
    with image_column:
        slt.image(img_contact_form)


    with text_column:
        slt.subheader("My Python Project")
        slt.write("The Project contains the visual correlation of a collection of Movie Data")
        slt.markdown("[Click here to view](https://github.com/Wayevee/My-Projects/blob/main/Python%20Movies%20Project.ipynb)")

with slt.container():
    slt.write("---")
    slt.header("Get In Touch With Me!")
    slt.write("##")


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
