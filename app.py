from connection2 import SpoonacularMetadataConnectionProvider
import streamlit as st
from connection import SpoonacularConnectionProvider
from requests import get
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
# Custom CSS styles
st.markdown(
    """
    <style>
    .stApp {
        max-width: 700px;
        margin: 0 auto;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #f0f0f0;
        color: black;  /* Keep the user input text as black */
        font-size: 16px;
        padding: 12px 15px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .stButton>button {
        background-color: #0078E7;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stMarkdown {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    """
    The main function to run the recipe information web app.

    This function sets up the Streamlit app, connects to the Spoonacular API,
    and handles user interactions to fetch and display recipe data.
    """
    api_connection = SpoonacularConnectionProvider(connection_name='recipeProvider')

    st.title("Recipedia")
    st.markdown("Enter your desired food name and we'll find you a recipe! :)")

    recipes_input = st.text_input("Enter your preffered food choice")
    

    if st.button("Get Recipes"):
        try:
            recipes = [city.strip() for city in recipes_input.split(",")]
            recipes_data = api_connection.query(recipes)
            if(len(recipes_data) != 0):
                st.success("Recipes fetched successfully!")
                
                display_recipes_data(recipes_data)
            else:
                st.error("No recipes found for the given query.")    
        except Exception as e:
            st.error(f"Error occurred: {e}")




def display_recipes_data(recipes_data):
   
    for city, data in recipes_data.items():
        if isinstance(data, str):
            st.markdown(data)
        else:

            
            st.image(data['image'])
            st.markdown(f"## Recipe Name: {data['title']}")
            st.markdown(f"## Recipe ID: {data['id']}")
            api_connection = SpoonacularMetadataConnectionProvider(connection_name='recipeProvider')


            with st.expander("See Recipe Details"):
                try:
                    recipe_data = api_connection.query(data['id'])


                    # Display recipe details
                    st.image(recipe_data['image'])
                    st.markdown(f"## Price per Serving: {recipe_data['pricePerServing']}")
                    st.markdown(f"## Health Score: {recipe_data['healthScore']}")
                    st.markdown(f"## Gluten Free: {recipe_data['glutenFree']}")
                    st.markdown(f"## Instructions:")
                    st.markdown(recipe_data['instructions'], unsafe_allow_html=True)
                    st.markdown(f"## Source URL:")

                    st.markdown(f"{recipe_data['sourceUrl']}")
                    st.markdown(f"## Ready in Minutes: {recipe_data['readyInMinutes']}")
                except Exception as e:
                    st.error(f"Error occurred while fetching recipe details: {e}")
                    
            

            
        st.markdown("---")
def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
    </style>
    """

    style_div = styles(
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        text_align="center",
        height="60px",
        opacity=0.6
    )

    style_hr = styles(
    )

    body = p()
    foot = div(style=style_div)(hr(style=style_hr), body)

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)
        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "<b>Made with</b>: Python 3.9.6 ",
        link("https://www.python.org/", image('https://i.imgur.com/ml09ccU.png',
        	width=px(18), height=px(18), margin= "0em")),
        ", Streamlit ",
        link("https://streamlit.io/", image('https://res.cloudinary.com/dc0tfxkph/image/upload/v1690664263/pngaaa.com-5084798.png',
        	width=px(24), height=px(25), margin= "0em")),
        ", and ❤️ in India by Mabud ",
        link("https://github.com/Pavel401", image('https://res.cloudinary.com/dc0tfxkph/image/upload/v1690664339/47685150.jpg',
        	width=px(24), height=px(25), margin= "0em", border_radius=px(50))),
        br(),
    ]
    layout(*myargs)
if __name__ == "__main__":
    main()
    


footer()
