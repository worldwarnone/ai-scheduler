import streamlit as st
import openai
import os

openai.api_key = os.getenv('openai')

def generate_schedule() -> str:
    prompt = st.session_state['prompt']
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=3000)['choices'][0]['text']
    st.session_state['schedule'] = response

def generate_prompt():
    prompt = f"""
can you help make an itinerary for dates between based on this information.

I need the itinerary to be precise down to the hour.

I want at least 2 activities per day, other than eating.

dates: {st.session_state['dates']}
location: {st.session_state['location']}
things i like: {st.session_state['likes']}
things I don't like: {st.session_state['dislikes']}

I'm busy at these times: {st.session_state['already_planned']}

make restaurant recommendations for each meal


"""
    st.session_state['prompt'] = prompt

def submit_user_configs():
    generate_prompt()
    generate_schedule()


questions = [
    ('dates', 'What dates do we need to plan for?'),
    ('location', 'Where will you be?'),
    ('likes', 'tell me somethings you like'),
    ('dislikes', 'anything you want to avoid?'),
    ('already_planned', 'Let me know if you have anything already planned'),
    ('restaurants', 'Do you want me to make some restaurent recommendations?')
]

for i in questions:
    if i[0] not in st.session_state:
        st.session_state[i[0]] = ''
    
    st.session_state[i[0]] = st.sidebar.text_area(i[1])

if 'prompt' not in st.session_state:
    st.session_state['prompt'] = ''

if 'schedule' not in st.session_state:
    st.session_state['schedule'] = ''



st.sidebar.button('submit', on_click=submit_user_configs)

st.text_area('schedule', value=st.session_state['schedule'], height=750)