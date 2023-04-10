import streamlit as st

def mad_libs():
    st.title("Mad Libs Game")

    # Create form to get input words
    with st.form("mad_libs_form"):
        adjective_1 = st.text_input("Enter an adjective")
        noun_1 = st.text_input("Enter a noun")
        verb_1 = st.text_input("Enter a verb (past tense)")
        adverb_1 = st.text_input("Enter an adverb")
        adjective_2 = st.text_input("Enter another adjective")
        noun_2 = st.text_input("Enter another noun")
        verb_2 = st.text_input("Enter another verb (past tense)")

        # Create a submit button
        submit_button = st.form_submit_button(label="Create Mad Libs Story")

    # Create Mad Libs Story using the input words
    if submit_button:
        st.write(f"Once upon a time, there was a {adjective_1} {noun_1}.")
        st.write(f"The {noun_1} {verb_1} {adverb_1} to the {adjective_2} {noun_2}.")
        st.write(f"The {noun_2} {verb_2} and lived happily ever after.")

mad_libs()
