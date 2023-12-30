import streamlit as st

st.set_page_config('HPP', layout='wide')

sidebar = st.sidebar
with sidebar:
    st.title("House Price Prediction")
    st.write('## Menu')
    City = st.radio(
        label='Select the City',
        options=['Chennai', 'Delh', 'Mumbai'],
        index=0
    )

    for i in range(16):
        st.text("")

    col1, col2 = st.columns(2)

    with col1:
        st.link_button("My Github", "https://github.com/2Sriram4")

    with col2:
        st.link_button(
            "My Linkedin", "https://www.linkedin.com/in/sriram-k-4798aa21a/")

if City == 'Chennai':

    st.title('House Price Prediction - Chennai')

    tab1, tab2 = st.tabs(['Prediction', 'Overview'])

    with tab1:

        col1, col2 = st.columns(2)

        with col1:

            area = st.selectbox(
                label='Area',
                options=['Karapakkam', 'Anna Nagar', 'Adyar',
                         'Velachery', 'Chrompet', 'KK Nagar', 'T Nagar'],
                index=None
            )

        with col2:

            sqft = st.number_input(
                label='SquareFeet',
                min_value=500,
                max_value=3000,
                value=None
            )

        col3, col4 = st.columns(2)

        with col3:

            bedroom = st.slider(
                label='No of Bedrooms',
                min_value=1,
                max_value=10,
                step=1,
                value=None
            )

        with col4:

            bathroom = st.slider(
                label='No of Bathrooms',
                min_value=1,
                max_value=5,
                step=1,
                value=None
            )

        col5, col6 = st.columns(2)

        with col5:

            n_room = st.number_input(
                label='Total Rooms',
                min_value=2,
                max_value=20,
                value=None
            )

        with col6:

            age = st.number_input(
                label='Age of the property',
                min_value=1,
                max_value=100,
                value=None
            )

        col7, col8 = st.columns(2)

        with col7:

            utility_avail = st.selectbox(
                label='Utilities',
                options=['AllPub', 'ELO', 'NoSewr ', 'NoSeWa'],
                index=None
            )

        with col8:

            street = st.selectbox(
                label='Type of alley access to the property',
                options=['Paved', 'Gravel', 'No Access'],
                index=None
            )

        col9, col10 = st.columns(2)

        with col9:

            sale_cond = st.selectbox(
                label='Condition of sale',
                options=['AbNormal', 'Family',
                         'Partial', 'AdjLand', 'Normal Sale'],
                index=None
            )

        with col10:

            mzzone = st.selectbox(
                label='General zoning classification of the sale',
                options=['A', 'RH', 'RL', 'I', 'C', 'RM'],
                index=None
            )

        col11, col12 = st.columns(2)

        with col11:

            buildtype = st.selectbox(
                label='Purpose of House',
                options=['Commercial', 'House', 'Others'],
                index=None
            )

        with col12:

            park_facil = st.selectbox(
                label='Parking Facility',
                options=['Yes', 'No'],
                index=None
            )

        col13, col14 = st.columns(2)

        with col13:

            reg_fee = st.number_input(
                label='Registration fee',
                min_value=50000,
                max_value=2000000,
                value=None
            )

        with col14:

            commition = st.number_input(
                label='Commition',
                min_value=5000,
                max_value=1000000,
                value=None
            )

        st.divider()

        st.write('Click the button to Predict the price of the House')

        if st.button("Predict"):
            from Chennai_HPP_py import pred_chennai
            price = pred_chennai(area, sale_cond, park_facil, buildtype, utility_avail,
                                 street, mzzone, sqft, bedroom, bathroom, n_room, reg_fee, commition, age)
            st.write("## The Price of the House is : 💸", price)

    with tab2:

        st.write(
            """The Chennai house price prediction project involves utilizing machine learning techniques to forecast property prices. The project starts by loading a dataset and ensuring data quality through cleaning processes that address missing values. The dataset undergoes transformations, such as converting data types and introducing new features like property age, which is calculated from sale and build dates. Categorical variables are encoded for consistency in numerical representation, and the dataset is split into subsets containing categorical and numerical features.

The choice of a RandomForestRegressor model allows capturing complex relationships within the data. The model is trained on the prepared dataset, and its performance is evaluated using the R-squared metric, which measures how well the model explains the variability in the target variable (house prices). This evaluation ensures the effectiveness of the trained model in making accurate predictions.

The project also includes a user-friendly prediction function, enabling users to input specific property details. The function employs label-encoded values and the trained model to predict house prices based on the provided inputs, enhancing the model's practical usability.

In summary, this project provides a holistic approach to Chennai house price prediction, encompassing data preprocessing, feature engineering, model training, and a user-friendly interface for making real-world predictions."""
        )

        st.divider()

        st.write(":red[_Click the button to view the dataset_]")

        st.link_button(
            "Dataset", "https://www.kaggle.com/datasets/kunwarakash/chennai-housing-sales-price")

elif City == 'Delhi':

    st.title('House Price Prediction - Delhi')

    tab1, tab2 = st.tabs(['Prediction', 'Overview'])

    with tab1:

        col1, col2 = st.columns(2)

        with col1:

            locality = st.selectbox(
                label='Locality',
                options=['Rohini Sector', 'Lajpat Nagar', 'Dwarka Sector',
                         'Laxmi Nagar', 'Patel Nagar', 'Vasant Kunj', 'Shahdara',
                         'Punjabi Bagh', 'Paschim Vihar', 'Alaknanda', 'Vasundhara Enclave',
                         'Kalkaji', 'Other'],
                index=None
            )

        with col2:

            area = st.number_input(
                label='SquareFeet',
                min_value=10,
                max_value=30000,
                value=None
            )

        col3, col4 = st.columns(2)

        with col3:

            bhk = st.slider(
                label='BHK',
                min_value=1,
                max_value=10,
                step=1,
                value=None
            )

        with col4:

            bathroom = st.slider(
                label='No of Bathrooms',
                min_value=1,
                max_value=10,
                step=1,
                value=None
            )

        col5, col6 = st.columns(2)

        with col5:

            type = st.selectbox(
                label='Type',
                options=['Builder Floor', 'Apartment'],
                index=None
            )

        with col6:

            furnishing = st.selectbox(
                label='Furnishing',
                options=['Semi Furnished', 'Furnished', 'Unfurnished'],
                index=None
            )

        col7, col8 = st.columns(2)

        with col7:

            transaction = st.selectbox(
                label='Transaction',
                options=['New Property', 'Resale'],
                index=None
            )

        with col8:

            status = st.selectbox(
                label='Status',
                options=['Ready to move', 'Almost ready'],
                index=None
            )

        col9, col10 = st.columns(2)

        with col9:

            parking = st.number_input(
                label='No of Parking available',
                min_value=0,
                max_value=10,
                value=None
            )

        st.divider()

        st.write('Click the button to Predict the price of the House')

        if st.button("Predict"):
            from Delhi_HPP_py import pred_delhi
            price = pred_delhi(furnishing, locality, status,
                               transaction, type, area, bhk, bathroom, parking)
            st.write("## The Price of the House is : 💸", price)

    with tab2:

        st.write(
            """The Delhi house price prediction project employs a systematic approach to anticipate property prices, leveraging machine learning methodologies. Commencing with data handling, the project addresses anomalies by intelligently dropping rows associated with specific parking values and refines the dataset by categorizing localities into broader groups, enhancing the granularity of analysis.

Moving on to data preprocessing, the project adopts strategic methods for handling missing values, ensuring data completeness. Imputations, including the calculation of per-square-foot prices and mode-based filling, contribute to this aspect. Transformation processes, such as string replacements and type conversions, maintain consistency in data representation.

Subsequently, categorical variables undergo label encoding, and feature engineering involves creating distinct subsets. The project stands out with its utilization of a RandomForestRegressor model, known for capturing intricate relationships within data. The user-friendly prediction function is a noteworthy aspect, allowing individuals to input specific property details and obtain accurate price estimates. The incorporation of label decoding enhances the interpretability of predictions, making the project a comprehensive and practical solution for predicting house prices in Delhi."""
        )

        st.divider()

        st.write(":red[_Click the button to view the dataset_]")

        st.link_button(
            "Dataset", "https://www.kaggle.com/datasets/neelkamal692/delhi-house-price-prediction")

elif City == 'Mumbai':

    st.title('House Price Prediction - Mumbai')

    tab1, tab2 = st.tabs(['Prediction', 'Overview'])

    with tab1:

        col1, col2 = st.columns(2)

        with col1:

            region = st.selectbox(
                label='Region',
                options=['Andheri West', 'Naigaon East', 'Borivali West', 'Panvel',
                         'Mira Road East', 'Parel', 'Boisar', 'Santacruz East',
                         'Badlapur East', 'Fort', 'Badlapur West', 'Khopoli', 'Chembur',
                         'Jogeshwari West', 'Vasai', 'Kalamboli', 'Powai', 'Ghansoli',
                         'Thane West', 'Vikhroli', 'Bhiwandi', 'Airoli', 'Ambernath West',
                         'Borivali East', 'Virar', 'Kharghar', 'Ulwe', 'Kamothe',
                         'Jogeshwari East', 'Mulund West', 'Palghar', 'Goregaon West',
                         'Taloja', 'Rasayani', 'Ghatkopar East', 'Ulhasnagar', 'Dombivali',
                         'Kewale', 'Nala Sopara', 'Goregaon East', 'Kandivali East',
                         'Kurla', 'Andheri East', 'Dahisar', 'Karanjade', 'Mahim', 'Vashi',
                         'Malad West', 'Girgaon', 'Dadar West', 'Bandra West',
                         'Kandivali West', 'Kalyan West', 'Neral', 'Kalyan East', 'Karjat',
                         'Ghatkopar West', 'Dronagiri', 'Mulund East', 'Navade', 'Ambivali',
                         'Agripada', 'Owale', 'Ville Parle East', 'Kalwa', 'Khar',
                         'Santacruz West', 'Nerul', 'Kanjurmarg', 'Vangani',
                         'Bhayandar East', 'Seawoods', 'Sewri', 'Ambernath East',
                         'Nilje Gaon', 'Prabhadevi', 'Matunga', 'Lower Parel', 'Titwala',
                         'Shil Phata', 'Koper Khairane', 'Napeansea Road', 'Bhandup West',
                         'Koproli', 'Anjurdive', 'Wadala', 'Sion', 'Taloje', 'Cuffe Parade',
                         'Bhandup East', 'Byculla', 'Tardeo', 'Vasai West', 'Vasai east',
                         'Malad East', 'Colaba', 'Thane East', 'Nalasopara East', 'Deonar',
                         'Nahur East', 'Sanpada', 'Sector 21 Kamothe', 'Saphale', 'Kasheli',
                         'Juinagar', 'Worli', 'Panch Pakhdi', 'Mazagaon',
                         'Hiranandani Estates', 'Belapur', 'Vichumbe', 'Bandra East',
                         'Sector 17 Ulwe', 'Sector 23 Ulwe', 'Nalasopara West', 'Mahalaxmi',
                         'Sector 20 Kamothe', 'Dadar East', 'Sector 19 Kamothe', 'Shahapur',
                         'Sector 30 Kharghar', 'Asangaon', 'Vikroli East', 'Mira Road',
                         'Kanjurmarg East', 'Rambaug', 'Sector-12 Kamothe', 'Juhu',
                         'Ville Parle West', 'Mazgaon', 'Virar East', 'Khar West',
                         'Sector 8 New panvel', 'Rabale', 'Bhayandar West',
                         'Sector 20 Ulwe', 'Sector 22 Kamothe', 'Sector 21 Nerul',
                         'Bandra Kurla Complex', 'Sector 14 Vashi', 'Mumbai Central',
                         'Virar West', 'Sector 11 Koparkhairane', 'Unnat Nagar', 'Diva',
                         'Palava', 'Dombivali East', 'Sector-14 Koparkhairane',
                         'Greater Khanda', 'Sector-35D Kharghar', 'Umroli', 'Sector-9 Ulwe',
                         'Govandi', 'vile parle west', 'MATUNGA WEST', 'Sector-3 Ulwe',
                         'kasaradavali thane west', 'Kurla East', 'Pestom Sagar Colony',
                         'Sector 12 Kharghar', 'Police Colony', 'Dahisar West',
                         'Marine Lines', 'Sector 19 Kharghar', 'Kalher', 'Hindu Colony',
                         'Dahisar East', 'Sector 9 Vashi', 'Khardi', 'Babulnath Road',
                         'Sector 21 Kharghar', 'Dharavi', 'Vasind', 'Tilak Nagar',
                         'Ashok nagar', 'Antop Hill', 'Peddar Road', 'Kamathipura',
                         'Usarghar Gaon', 'Ambarnath', 'Patlipada', 'Vevoor', 'Shelu',
                         'Kurla West', 'Goregaon', 'Naupada', 'Bhoiwada',
                         'Sector 7 Kharghar', 'Roadpali', 'Sector-9 Kamothe', 'Borivali',
                         'Badlapur', 'Khanda Colony', 'Dombivli (West)', 'GTB Nagar',
                         'Bandra', 'kandivali', 'Mahavir Nagar', 'Churchgate', 'Pali Hill',
                         'Manpada', 'Sector-50 Seawoods', 'Uttan', 'Gauripada',
                         'Gandhar Nagar', 'Mahim West', 'Warai', 'mumbai', 'Khatiwali',
                         'Chandivali', 'Mumbra', 'Chembur East', 'Malabar Hill', 'sector',
                         'Uran', 'Manjarli', 'Ghodbunder Road', 'Mulund',
                         'Sector 18 Kharghar', 'Palidevad', 'Juhu Scheme', 'Adaigaon',
                         'Versova', 'Sector-4 New Panvel', 'Pen', 'Sector 6 Kamothe',
                         'Maneklal Estate', 'L I C Colony'],
                index=None
            )

        with col2:

            area = st.number_input(
                label='SquareFeet',
                min_value=10,
                max_value=30000,
                value=None
            )

        col3, col4 = st.columns(2)

        with col3:

            bhk = st.slider(
                label='BHK',
                min_value=1,
                max_value=10,
                step=1,
                value=None
            )

        with col4:

            age = st.selectbox(
                label='Age',
                options=['New', 'Resale', 'Unknown'],
                index=None
            )

        col5, col6 = st.columns(2)

        with col5:

            type = st.selectbox(
                label='Type',
                options=['Apartment', 'Villa', 'Studio Apartment', 'Independent House',
                         'Penthouse'],
                index=None
            )

        with col6:

            status = st.selectbox(
                label='Status',
                options=['Ready to move', 'Under Construction'],
                index=None
            )

        st.divider()

        st.write('Click the button to Predict the price of the House')

        if st.button("Predict"):
            from Mumbai_HPP_py import pred_mumbai
            price = pred_mumbai(type, region, status, age, bhk, area)*100000
            st.write("## The Price of the House is : 💸", price)

    with tab2:

        st.write(
            """The Mumbai house price prediction script utilizes a RandomForestRegressor model to forecast property prices. After loading the dataset from a CSV file, the 'locality' column is dropped, streamlining the data for analysis. A transformation function is applied to convert prices from crore to lakhs, followed by a logarithmic transformation of the 'price' variable to enhance model performance. Categorical and numerical subsets are created to facilitate effective model training. Categorical variables undergo label encoding, contributing to the model's interpretability. The RandomForestRegressor model is then trained on the prepared dataset, and predictions are generated for the test set.

The script introduces a user-friendly prediction function that empowers users to input specific property details such as type, region, status, age, number of bedrooms (bhk), and area. This function maps these inputs to their label-encoded counterparts and employs the trained model to predict house prices. The predictions are then transformed back to their original scale for meaningful interpretation. This user-centric approach enhances the script's practicality for real-world applications, making it a comprehensive tool for Mumbai house price prediction.

In essence, this script presents a holistic framework, covering crucial stages from data preprocessing to model training and providing a user-friendly interface for accurate house price predictions in Mumbai.""")

        st.divider()

        st.write(":red[_Click the button to view the dataset_]")

        st.link_button(
            "Dataset", "https://www.kaggle.com/datasets/dravidvaishnav/mumbai-house-prices")
