import streamlit as st

def main():
    # Set page title and background color
    st.set_page_config(page_title="Global Mental Health Analysis Dashboard", page_icon=":brain:", layout="wide", initial_sidebar_state="collapsed")
    # Apply some styling to the title
    st.markdown(
        """
        <style>
            .title {
                color: #000000;
                text-align:left;
                font-size: 45px;
                margin-bottom: 50px;
            }
            .intro-text {
                font-size: 20px;
                color:black;
                margin-bottom: 20px;
            }
            .icon {
                vertical-align: middle;
                margin-right: 10px;
            
            }
            .title-col {
                display: flex;
                align-items: center;
            }
        
            .disorder-section {
                margin-top: 50px;
            }
            .disorder-title {
                font-size: 24px;
                font-weight: bold;
                color: black;
                margin-bottom: 20px;
            }
            .disorder-description {
                font-size: 20px;
                color: black;
                margin-bottom: 20px;
            }
            .element-container img {
                display: block;
                margin: 0 auto;
                color:black;
                max-width: 600px;
                height: auto;
                border-radius:10px;
            }
            .main {
                background-image: url('https://img.freepik.com/free-photo/pastel-brush-paint-textured-background_53876-96676.jpg');
                background-size: cover;
                background-position: center;
                background- 
            }
            .content {
                position: relative;
                z-index: 1;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )
    # Display background image container
    st.markdown('<div class="bg-container"></div>', unsafe_allow_html=True)



    # Display title and introductory text
    c1,c2= st.columns([1,10])
    with c1:
        st.image(r"C:\Users\SHRUTI\Desktop\MHDD\images\dashboard icon.webp", width=100)

    with c2:
        st.markdown("<div class='title-col'>", unsafe_allow_html=True)
        st.title("Global Mental Health Analysis Dashboard")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<p class='intro-text'>Welcome to the Global Mental Health Analysis Dashboard.</p>", unsafe_allow_html=True)
    st.markdown("<p class='intro-text'>This dashboard provides insights and analysis of mental health data from around the world.</p>", unsafe_allow_html=True)
    
    
    # Display section for various mental health disorders
    st.markdown("<div class='disorder-section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='disorder-title'>Common Mental Health Disorders</h2>", unsafe_allow_html=True)

    # Display text and image for each disorder
    disorders = [
        {
            "name": "Anxiety Disorders",
            "description": "Anxiety disorders are a group of mental disorders characterized by significant feelings of anxiety and fear. Common types include generalized anxiety disorder (GAD), panic disorder, and social anxiety disorder.",
            "image_path": r"C:\Users\SHRUTI\Desktop\MHDD\images\anxiety disorders.png"
        },
        {
            "name": "Depression",
            "description": "Depression is a mood disorder that causes persistent feelings of sadness, hopelessness, and loss of interest. It can affect how you feel, think, and handle daily activities.",
            "image_path": r"C:\Users\SHRUTI\Desktop\MHDD\images\depression.jpg"
        },
        {
            "name": "Bipolar Disorder",
            "description": "Bipolar disorder, formerly known as manic-depressive illness, is a brain disorder that causes unusual shifts in mood, energy, activity levels, and the ability to carry out day-to-day tasks.",
            "image_path": r"C:\Users\SHRUTI\Desktop\MHDD\images\bipolar disorder.jpg"
        },
        {
            "name": "Schizophrenia",
            "description": "Schizophrenia is a severe mental disorder characterized by profound disruptions in thinking, affecting language, perception, and sense of self. People with schizophrenia often experience hallucinations, delusions, disorganized thinking, and cognitive deficits. Symptoms typically emerge in early adulthood and can be chronic, leading to significant impairment in social, occupational, and daily functioning. ",
            "image_path": r"C:\Users\SHRUTI\Desktop\MHDD\images\schizoprenia.png.jpg"
        },
        {
            "name": "Eating Disorder",
            "description": "Eating disorders are serious mental health conditions characterized by unhealthy behaviors surrounding food and weight. Common types include anorexia nervosa, bulimia nervosa, and binge eating disorder. Individuals with anorexia may severely restrict food intake, leading to dangerously low body weight, while those with bulimia often engage in cycles of binge eating followed by purging behaviors.  ",
            "image_path": r"C:\Users\SHRUTI\Desktop\MHDD\images\eatinf disoredr.jpeg"
        }


    ]

    for disorder in disorders:
        st.markdown(f"<h3 class='disorder-title'>{disorder['name']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='disorder-description'>{disorder['description']}</p>", unsafe_allow_html=True)
        st.image(disorder["image_path"], caption=disorder["name"],use_column_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
# load data
