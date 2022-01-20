import streamlit as st
from google.cloud import firestore

#st.header('HELLO !!')
#if st.button('Balloons?'):
#   st.balloons()

#Authenticate to Firestore with the JSON account key
db = firestore.Client.from_service_account_json("firestore-key.json")

#Create a reference to the Google post
doc_ref = db.collection("posts").document("Google")

#Get data at that reference
doc = doc_ref.get()

#See the data obtained
st.write("ID: ", doc.id)
st.write("Contents: ", doc.to_dict()) 

#Create a new post reference
doc_ref = db.collection("posts").document("Apple")

#Upload some data to that reference
doc_ref.set({
	"title": "Apple",
	"url": "www.apple.com"
})