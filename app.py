import streamlit as st
import pickle as pk
import numpy as np


st.header("Book Recommendation System")
model=pk.load(open("artifacts/model.pkl",'rb'))
book_name=pk.load(open("artifacts/book_name.pkl",'rb'))
book_matrix=pk.load(open("artifacts/book_matrix.pkl",'rb'))
final_rated_books=pk.load(open("artifacts/final_rated_books.pkl",'rb'))

selected_books=st.selectbox("Type or Select a Book",book_name)

def fetch_poster(suggestions):
    book_name=[]
    idx_list=[]
    poster_url=[]
    for id_book in suggestions:
        book_name.append(book_matrix.index[id_book])
    for name in book_name[0]:
        ids =np.where(final_rated_books['Title']==name)[0][0]
        idx_list.append(ids)
    for idx in idx_list:
        url=final_rated_books.iloc[idx]['Image_url']
        poster_url.append(url)
    return poster_url



def recommend_book(book_name):
    book_list=[]
    book_id=np.where(book_matrix.index==book_name)[0][0]
    distance,suggestions=model.kneighbors(book_matrix.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)
    poster_url=fetch_poster(suggestions)
    for i in suggestions:
        books=book_matrix.index[i]
        for j in books:
            book_list.append(j)
    return book_list,poster_url 
if st.button("Show Recommendation"):
    recommendation_books,poster_url=recommend_book(selected_books)
 
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
     st.text(recommendation_books[1])
     st.image(poster_url[1])
    with col2:
     st.text(recommendation_books[2])
     st.image(poster_url[2])
     with col3:
      st.text(recommendation_books[3])
      st.image(poster_url[3])
    with col4:
     st.text(recommendation_books[4])
     st.image(poster_url[4])
    with col5:
     st.text(recommendation_books[5])
     st.image(poster_url[5])

