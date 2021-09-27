import pickle
import streamlit as st

def recommend(book):
    model = pickle.load(open('model_rec.pkl','rb'))
    book_pivot = final_rating.pivot_table(columns='User-ID', index='title', values='Book-Rating')
    book_pivot.fillna(0, inplace=True)
    distances, suggestions = model.kneighbors(book_pivot.loc[book,:].values.reshape(1, -1))
    rec_books = []

    for i in range(len(suggestions)):
        rec_books.append(book_pivot.index[suggestions[i]])
    return rec_books

st.header('Book Recommender System')
final_rating = pickle.load(open('final_rating.pkl','rb'))
books_list=set(final_rating['title'].values)
selected_book = st.selectbox('Type or Select a book from the dropdown',books_list)
images = final_rating[['title', 'Image-URL-M']]
images = images.groupby('title')['Image-URL-M'].sum()
if st.button('Show Recommendation'):
    recommended_book_names = recommend(selected_book)
    col1, col2, col3, col4,col5 = st.columns(5)
    with col1:
        st.text(recommended_book_names[0][0])
        st.image(images[recommended_book_names[0][0]])
    with col2:
        st.text(recommended_book_names[0][1])
        st.image(images[recommended_book_names[0][1]])

    with col3:
        st.text(recommended_book_names[0][2])
        st.image(images[recommended_book_names[0][2]])
    with col4:
        st.text(recommended_book_names[0][3])
        st.image(images[recommended_book_names[0][3]])
    with col5:
        st.text(recommended_book_names[0][4])
        st.image(images[recommended_book_names[0][4]])