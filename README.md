## Natural Language Processing Use Cases

### Sentiment Analysis
Understand the social sentiment of your brand, product or service while monitoring online conversations. Sentiment Analysis is contextual mining of text which identifies and extracts subjective information in source material.

### Emotion Analysis
Sometimes the three classes of sentiment (positive, negative and neutral) are not sufficient to understand the nuances regarding the underlying tone of a sentence. Our Emotion Analysis classifier is trained on our proprietary dataset and tells whether the underlying emotion behind a message is: Happy, Sad, Angry, Fearful, Excited or Bored.

### Named Entity Recongnition
Named Entity Recognition can identify individuals, companies, places, organization, cities and other various type of entities. API can extract this information from any type of text, web page or social media network.

### Steps to Get Started

#### Clone Repository
To run the website at your end, you need to get this source code.

``` git clone https://github.com/EdagPSIT/nlp-usecases-flask-website.git ```

#### Create Virtual Environment and Install dependencies
We need to create new virtual environment to isolate your dependencies from other environments and proper working of the application.
You can create new virtual environment as follows

``` python -m venv <venv_name> ```  

This will create virtual environment for you, now you can activate your environment to install required dependecies for this project.  
Open Git bash terminal and type the command

``` source <venv_name>/Scripts/activate ```  

Now install dependencies  

``` pip install -r requirements.txt ```  

#### Run application locally
Now you need to create `.env` file to store your parallelodots API key.

``` PARALLELDOTS_API_KEY=your_api_key ```   

You are all set to run the application at your end. 

``` python src/app.py ```    

Website is live now and same can be accessed at `localhost:5000`.


