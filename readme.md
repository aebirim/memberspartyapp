# memberspartyapp
memberspartyapp is a simple Flask app that shows the breakdown in gender for the House of Commons and the House of Lords using the [Members Names Information Service][mnisapi].

The MNIS API is the public interface to the UK Parliament's Members Names database, a comprehensive database of all MPs elected to Parliament since 1983. The API is flexible and powerful, but it's not very easy to use. The mnis library is a toolkit that makes it easier to download and manipulate useful data from the API.

At the most basic level, the mnis api allows you to download key data on all MPs who were serving on a given date to a csv with a single line of code. It makes it easy to obtain the same summary data for MPs as a list of Python dictionaries, or alternatively to get the full data for each MP returned by the API. The library allows you to customise the parameters sent to the API through a simple interface and makes possible quite sophisticated analysis of MPs' careers.

The MNIS API can provide the following data on MPs by default:

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

The memberspartyapp still represents work in progress and demonstrates my ongoing education in the language of Python and aspects of Data Science. The application uses matplotlib and the library mpld3 which allows you to generate matplotlib data visualizations within a browser. It is shared "as is".

### Python requirements
The application is written in Python 3.6. It requires the [requests][requests] package, which pip will install automatically if it is not already present.

### Usage
To obtain the breakdown in gender for House of Commons, use /memberspartyapp/commons
To obtain the breakdown in gender for House of Lords, use /memberspartyapp/lords

### Next iteration
The next iteration of this application would include the following:

  - Refactoring of code to remove duplication where apparent
  - The development of a binary prediction model which uses Logistic Regression, a method for binary classification problems (problems with two class values) which could be used, for example, to predict political party based on gender in either House
  - To continue refinement of the data visualization logic

[mnisapi]: <http://data.parliament.uk/membersdataplatform/memberquery.aspx>
[requests]: <http://docs.python-requests.org/en/master/>
