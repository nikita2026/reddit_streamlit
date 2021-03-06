import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("firestore-key.json")

#import json
#key_dict = json.loads(st.secrets["textkey"])
#creds = service_account.Credentials.from_service_account_info(key_dict)
#db = firestore.CLient(credentials=creds, project="reddit-streamlit")

#Streamlit widgets to let a user create a new post
title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")

#Upload the submitted post to the database
if title and url and submit:
	doc_ref = db.collection("posts").document("title")
	doc_ref.set({
	    "title": title,
	    "url": url
	})

#Render each post using some light markdown
posts_ref = db.collection("posts")
for doc in posts_ref.stream():
	post = doc.to_dict()
	title = post["title"]
	url = post["url"]

	st.subheader(f"Post: {title}")
	st.write(f":link: [{url}]({url})")