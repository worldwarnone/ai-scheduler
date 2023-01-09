import streamlit as st 
import os
import openai

openai.api_key = os.getenv('openai')


def generate_schedule(prompt) -> str:
    prompt = prompt
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=3000)['choices'][0]['text']
    return response

st.title('AI Scheduler')

if 'schedule' not in st.session_state:
    st.session_state['schedule'] = ''

location = st.sidebar.text_input('location')
start_date = st.sidebar.date_input('start_date')
end_date = st.sidebar.date_input('end_date')
likes_input = st.sidebar.text_area('likes_input')
dislikes_input = st.sidebar.text_area('dislikes_input')

pre_existing_plans = None
breakfast_time = st.sidebar.time_input('breakfast_time')
lunch_time = st.sidebar.time_input('lunch_time')
dinner_time = st.sidebar.time_input('dinner_time')


prompt = f"""
can you help make an itinerary for dates between {start_date} and {end_date} based on this information.
I need restaurant recommendations for each day. I need the itinerary to be precise down to the hour.

location: {location}
things i like: {likes_input}
things I don't like: {dislikes_input}

I like to eat breakfast around {breakfast_time}
I like to eat lunch around {lunch_time}
I like to eat dinner around {dinner_time}

"""

schedule = generate_schedule(prompt)
st.session_state['schedule'] = schedule

if st.session_state['schedule']:
    st.text_area('schedule', value=st.session_state['schedule'])