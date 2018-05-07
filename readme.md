# memberspartyapp
memberspartyapp is a simple Flask app that shows the breakdown in gender for the House of Commons, and Lords, in the [UK Parliament][parliament]. The app uses the [Members Names Information Service][mnisapi] API.

The [MNIS][mnisapi] api is the public interface to the UK Parliament's Members Names database, a comprehensive database of all MPs elected to Parliament since 1983. The API is flexible and powerful, but is straightforward to use.

At the most basic level, the mnis api allows you to download key data on all MPs to text and then converted to json. It makes it easy to obtain the same summary data for MPs as a list of Python dictionaries, or alternatively to get the full data for each MP returned by the API. The parameters sent to the API provides an analysis of MPs' careers.

The MNIS API provides the following data on members of Parliament using these parameters:

  - Member ID
  - Name
  - Constituency
  - Party
  - Date of Birth
  - Gender
  - Date first became an MP
  - Committee

Memberspartyapp still represents work in progress and demonstrates my ongoing education in the language of Python and aspects of Data Science. The application uses matplotlib, which is used to generate graphs from data and the library mpld3 which allows you to generate matplotlib data visualizations within a browser. It is shared "as is".

### Python requirements:
The application is written in Python 3.6. It requires specific python packages (located in requirements.txt) which are installed through the Usage instructions.

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
  - To continue refinement of the data visualization logic
  - Improvement of test coverage
  - Deployment to Heroku via Docker

[mnisapi]: <http://data.parliament.uk/membersdataplatform/memberquery.aspx>
[requests]: <http://docs.python-requests.org/en/master/>
[parliament]: <https://en.wikipedia.org/wiki/Parliament_of_the_United_Kingdom>
