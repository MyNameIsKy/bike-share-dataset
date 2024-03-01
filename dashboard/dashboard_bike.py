import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

#Membuat function untuk menampilkan rata-rata rental berdasarkan bulan
def monthly_mean_rent(df):
    monthly_rent = monthly_rent = df.groupby(by = 'mnth_x').agg({
    'cnt_x' : 'mean',
    })

    return monthly_rent

#Membuat function untuk menampilkan rata-rata rental berdasarkan Jam
def hour_mean_rent(df):
    rent_hour_max = df.groupby(by = 'hr').cnt_y.mean()

    return rent_hour_max

#Membuat function untuk menampilkan rata-rata rental berdasarkan Musim
def season_mean_rent(df):
    per_season = df.groupby(by = 'season_x').agg({
    'cnt_x' : 'mean'
    })

    return per_season

#Untuk membuat variabel yang dapat membaca Data Frame
all_df = pd.read_csv('bike_data.csv')

#Mengassign function yang sudah dibuat
monthly_rent = monthly_mean_rent(all_df)
hour_rent = hour_mean_rent(all_df)
season_rent = season_mean_rent(all_df)


#Membuat Tab untuk menampilkan visualisasi data
tab1, tab2, tab3 = st.tabs(['Rata - Rata Rental (Bulan)', 'Rata - Rata Rental (Jam)', 'Rata - Rata Rental (Musim)'])

with tab1:

    fig = plt.figure(figsize=(15,6))

    ax = sns.barplot(x='mnth_x', y='cnt_x', data= monthly_rent)
    ax.bar_label(ax.containers[0])

    plt.xlabel("Bulan")
    plt.ylabel("Rata - Rata")
    plt.title("Data Rata-rata rental sepeda (Bulan)")

    st.pyplot(fig)

with tab2:
    fig = plt.figure(figsize=(15,6))

    sns.barplot(x='hr', y=hour_rent, data=all_df)

    plt.xlabel("Jam")
    plt.ylabel("Rata - Rata")
    plt.title("Data Rata-rata rental sepeda (Jam)")

    st.pyplot(fig)

with tab3:
    fig = plt.figure(figsize=(15, 6))

    colors = ['#65B741', '#FCDC2A', '#ECB159', '#40A2E3']
    sns.barplot( y="cnt_x", x="season_x", data=season_rent, palette = colors)

    plt.title("Data rata-rata rental sepeda (Musim)", fontsize=15)
    plt.ylabel(None)
    plt.xlabel('Musim')
    plt.tick_params(axis='x', labelsize=12)
    plt.xticks([0,1,2,3], ['Spring', 'Summer', 'Fall', 'Winter'])
    st.pyplot(fig)


with st.sidebar:
    st.write('BIKE SHARING DASHBOARD :bike:')
    st.image('bike-rental.jpg')
    with st.expander ('Fungsi Dashboard Bike-Sharing'):
        st.markdown("""
        Fungsi dari dashboard Bike-Sharing ini adalah untuk menampilkan
        suatu visualisasi data yang sudah ada. Data tersebut berisi rata-rata
        dari beberapa kondisi seperti contohnya : 'Data rata-rata perental
        sepeda berdasarkan bulan'. Disini terdapat tiga data yaitu Data 
        rata-rata perental sepeda berdasarkan bulan, jam dan musim
        """)


with st.expander ('Pada bulan apakah orang-orang banyak merental sepeda?'):
    st.markdown("""
    Rata-Rata orang melakukan sewa atau rental sepeda terbanyak adalah pada bulan 6, 8 dan 9. 
    Bulan tersebut merupakan bulan dimana sewa sepeda banyak diminati dikarenakan faktor cuaca dan musim. 
    Bulan tersebut merupakan bulan transisi antara musim panas dan musim gugur
    """)

with st.expander ('Pada jam berapakah rata-rata orang merental sepeda?'):
    st.markdown("""
    Rata-Rata orang melakukan sewa atau rental sepeda adalah pada jam 5 Sore, 6 Sore dan juga jam 8 Pagi. 
    Hal ini dikarenakan orang-orang lebih senang untuk bersepeda di waktu pagi hari dan waktu sore hare yang 
    disebabkan waktu dan jam tersebut merupakan waktu dimana panas matahari dan suhu tidak terlalu panas.
    """)

with st.expander ('Pada musim apakah rata-rata orang merental sebuah sepeda?'):
    st.markdown("""
    Rata-rata orang yang merental sepeda adalah pada musim panas dan  musim gugur dikarenakan adanya korelasi 
    antara musim dan juga suhu serta windspeed yang ada pada dataset.
    """)

    