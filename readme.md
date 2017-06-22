# memberspartyapp
memberspartyapp is a simple Flask app that shows the breakdown in gender for the House of Commons and the House of Lords using the [Members Names Information Service][mnisapi].

The MNIS API is the public interface to the UK Parliament's Members Names database, a comprehensive database of all MPs elected to Parliament since 1983. The API is flexible and powerful, but is straightforward to use.

At the most basic level, the mnis api allows you to download key data on all MPs to text and then converted to json. It makes it easy to obtain the same summary data for MPs as a list of Python dictionaries, or alternatively to get the full data for each MP returned by the API. The parameters sent to the API provides an analysis of MPs' careers.

The MNIS API can provide the following data on MPs using these parameters:

  - Member ID
  - Name
  - Constituency
  - Party
  - Date of Birth
  - Gender
  - Date first became an MP
  - Number of days service (excluding dissolution periods)
  - Parliamentary role
  - Committee

Memberspartyapp still represents work in progress and demonstrates my ongoing education in the language of Python and aspects of Data Science. The application uses matplotlib and the library mpld3 which allows you to generate matplotlib data visualizations within a browser. It is shared "as is".

### Python requirements:
The application is written in Python 3.6. It requires the [requests][requests] package, which pip will install automatically if it is not already present.

### Usage (launch app):
        git clone https://github.com/aebirim/memberspartyapp.git
        cd /memberspartyapp
        pip install -r requirements.txt
        python app.py
        
  - To obtain the breakdown in gender for House of Commons,
    use http://127.0.0.1:5000/commons

  - To obtain the breakdown in gender for House of Lords,
    use http://127.0.0.1:5000/lords

### Next iteration:
The next iteration of this application would include the following:

  - Continuous refactoring
  - The development of a binary prediction model which uses Logistic Regression, a method for binary classification problems (problems with two class values) which could be used, for example, to predict political party based on gender in either House
  - To continue refinement of the data visualization logic
  - Deployment to Heroku via Docker

[mnisapi]: <http://data.parliament.uk/membersdataplatform/memberquery.aspx>
[requests]: <http://docs.python-requests.org/en/master/>
