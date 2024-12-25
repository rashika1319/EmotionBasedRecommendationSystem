import streamlit as st
from emotion_analysis import detect_emotion
from recommendation import recommend_content

# Title for the web app
st.title("Emotion-Based Recommendation System")

# Initialize session state for emotion and recommendations if not already set
if 'emotion' not in st.session_state:
    st.session_state.emotion = None
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = {}

# Create buttons for starting the application or "Ask an Expert"
if 'start' not in st.session_state:
    st.session_state.start = False
if 'ask_expert' not in st.session_state:
    st.session_state.ask_expert = False

if st.button("Start"):
    st.session_state.start = True
    st.session_state.ask_expert = False  # Reset "Ask an Expert" mode if start is clicked

if st.button("Ask an Expert"):
    st.session_state.ask_expert = True
    st.session_state.start = False  # Reset start mode if "Ask an Expert" is clicked

# If the user clicks "Start," display the emotion analysis interface
if st.session_state.start:
    # User input section for mood analysis
    st.write("### How's your mood right now?")
    user_input = st.text_area("Describe your current mood:", "")

    # Process the input when the user submits the text
    if st.button("Analyze Emotion"):
        if user_input:
            # Detect emotion from the user's input
            emotion = detect_emotion(user_input)
            st.session_state.emotion = emotion  # Store the emotion in session state
            st.session_state.recommendations = recommend_content(emotion)  # Store recommendations in session state

    # If emotion is detected, show the recommendations
    if st.session_state.emotion:
        st.write(f"**Detected Emotion:** {st.session_state.emotion.capitalize()}")

        # Let the user choose which category they want to see
        selected_category = st.selectbox("Select a category to get recommendations:",
                                         ["Songs", "Books", "Movies", "Yoga"])

        # Display the selected category recommendations
        st.write(f"### Recommendations for {selected_category}:")
        recommendations = st.session_state.recommendations

        if selected_category == "Songs":
            if recommendations["songs"]:
                for song in recommendations["songs"]:
                    st.write(f"**{song['title']}**")
                    st.markdown(f"[Click here to enjoy the song]({song['url']})")
            else:
                st.write("No songs available for this emotion.")

        elif selected_category == "Books":
            if recommendations["books"]:
                for book in recommendations["books"]:
                    st.write(f"**{book['title']}**")
                    st.write(f"**Description**: {book['description']}")
                    st.write(f"[Click here to check this book]({book['url']})")
            else:
                st.write("No books available for this emotion.")

        elif selected_category == "Movies":
            if recommendations["movies"]:
                for movie in recommendations["movies"]:
                    st.write(f"**{movie['title']}**")
                    st.write(f"**Description**: {movie['description']}")
                    st.markdown(f"[Click here to enjoy the Movie]({movie['url']})")
            else:
                st.write("No movies available for this emotion.")

        elif selected_category == "Yoga":
            if recommendations["yoga"]:
                for yoga in recommendations["yoga"]:
                    st.write(f"**{yoga['title']}**")
                    st.write(f"**Description**: {yoga['description']}")
                    st.markdown(f"[Click here to Follow Yoga]({yoga['url']})")
            else:
                st.write("No yoga poses available for this emotion.")

# If the user clicks "Ask an Expert," display the expert interaction interface
if st.session_state.ask_expert:
    st.write("### Ask an Expert")
    st.write(
        "Submit your query or describe your emotional state, and we’ll provide professional advice or helpful resources.")

    expert_query = st.text_area("What's on your mind?", "")
    if st.button("Submit Query"):
        if expert_query:
            st.write("Thank you for your submission. Our expert team will provide tailored advice shortly!")
        else:
            st.write("Please describe your concern or query to get expert advice.")
