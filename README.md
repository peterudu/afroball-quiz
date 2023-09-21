# afroBall Quiz

AfroBall Quiz is a python-based terminal interactive quiz application with a theme focus on African football The quiz application challenges users to participate on a round of 7 multiple choice questions on a vareity of African football topics. 

AfroBall Quiz is designed to engage its users, test their knowledge of African football, and most importantly ensure that they gain an enjoyable experience taking the quiz.

![Image of the website](/assets/images/)

[The live link to the hosted project](https://afroball-quiz-6f392208bd8b.herokuapp.com/) 

## User Experience (UX)
### User Stories
#### First Time Visitors Goals
- I want to be able to use the application on different screen-sized devices.
- I want an easy-to-understand quiz with helpful instructions and guidelines.
#### Returning Visitors Goals
- I want a quiz which is challenging and fun to take part in.
- I want to be able to use the app to assess my knowledge of African football.
#### Frequent Visitors Goals
- I want a quiz app with contemporary and up-to-date content.

## Design
### Imagery
### Wireframes
### Features
The afroBall Quiz application offers some features which are core to the making the quiz function and they include:

- Questions data catalogue - caf_question.json

  - The json file data catalogue is the source for questions and solutions data which is presented to the user of the quiz app. This questions data is imported and used to form a key element of the quiz.
  - The data catalogue is large and diverse. This can actually be extended by the author to make the quiz more exciting for app users.

  ![Questions data catalogue](/assets/images)

- Customized, personalized and interractive interface

  - The large ASCII art designed [afroBall title](/assets/) and welcome message speaks directly to the quiz user creating a user friendly experience.
  - The displayed [quiz statements and questions](/assets/) informs the quiz player exactly what he is required to do.
  - The quiz user constantly gets an [answer feedback](/assets/) on whether or not each answer attempt has been successful.

- Randomly mixed quiz questions

  - The integrated python random() method ensures that every new quiz session starts with a new sample of [mixed questions]() making the quiz unpredictable.
  - The afroBall quiz questions offer a multiple choice option helping the user to comprehend possible solutions.

- Handling user errors and input validation

  - When the user is prompted to pass on relevant quiz data, his input response is tested (using [try and except block]()) to ensure that correct data type and quantity is adopted.
  - If the user gives in an invalid data type the quiz app will display an [error message]() to the user.

- Display user quiz performance

  - The quiz presents the user ability to get and measure his quiz performance for each attempted question and also for the [overall score](/assets/) at the end of each quiz sesson.
  - The overall scores are displayed to the user in points and percentages 

### Accessibility
### Languages Used
The language used to create this quiz app was Python
### Frameworks, Libraries & Programs Used
Git was used for version control.

Github was used to save and store the files for the website.

Gitpod workspace was used to write and edit code for the quiz app.

Balsamiq was used to create wireframes for the quiz app.

[Diagrams.net (previously draw.io)](https://www.drawio.com/) was use to create the flow chart for the quiz app.

[Am I Responsive](https://ui.dev/amiresponsive) was used to show how the app would look on different devices.

[Heroku](https://www.heroku.com/) was used to deploy the live version of the terminal

## Deployment & Local Development
### Deployment
The quiz app was deployed using Code Institute mock terminal for Heroku. 
For the deployment the following steps are required:

1. Login to a newly created or already existing Heroku account.
2. Go to the Heroku dashboard and select "New" and the option to create a new Heroku app.
3. Give the new app a name and then choose your region.
4. From the dashboard options choose "Settings" and then go to the segment "Config Vars"
5. In Cofig Vars add the settings: KEY = PORT and VALUE = 8000.
6. Set the buildpacks to Python and NodeJS in that order.
7. On dashboard click the Deploy section.
8. Next under go to segment Deployment Method and select GitHub, then click the connect button.
9. Search for the GitHub repository name and click connect button to link Heroku app to GitHub
10. Next scroll under to choose either to use Automatic deployment or Manual deployment.
11. View build log until confirmation that the app has been successfully deployed.

### Local Development
To clone this project proceed with the following steps:

1. Login to GitHub and go to the repository of this project, https://github.com/peterudu/afroball-quiz.
2. Chose and click the green Code button.
3. Select a cloning method from one of options, either HTTPS, SSH or GitHub CLI and copy the offered link.
4. Open up the terminal of your code editor, select a directory for your project, type in the Git command - ‘git clone’ and then paste in the copied link from the github repository.

## Testing
### Automated Testing
### Manual Testing
#### Testing User Stories
Firsttime Visitors
| Goals | How are they achieved? |
| ---| ---|
| I want to be able to use the application on different screen-sized devices. | I developed the app with the goal of it being responsive and tests done certify that the quiz app can be accessed with a mobile phone, a tablet, a laptop or a desktop computer. |
| I want an easy-to-understand quiz with helpful instructions and guidelines. | With the aid of displayed quiz statements and simple multiple-choice questions the app guides and informs the app user on what he is required to do. |

Returning Visitors
| Goals | How are they achieved? |
| ---| ---|
| I want a quiz which is challenging and fun to take part in. | The quiz qestions were carefully selected and cover a broad range of continental African football issues ranging from the African football federation, the players and women's football. In addition by each new quiz session the app randomly selects a new set of questions from the question catalogue so the quiz is never predictable for the user |
| I want to be able to use the app to assess my knowledge of African football. | During the quiz session the user receives a feedback on every attempted question and at the end of the session displays a report of the overall quiz performance of the user based on the points scored and in percentage terms  |

Frequent Visitors
| Goals | How are they achieved? |
| ---| ---|
| I want a quiz app with contemporary and up-to-date content. | The author has built the app in such a way so that the quiz question catalogue can be adapted in future to include any new changes and developments in African football |
#### Full Testing
#### General Testing
### Fixed Bugs
### Unfixed Bugs

## Credits
### Code Used
### Content
### Media
#### Images
#### Video Clip
### Acknowledgements
I acknowledge the following people who helped me complete this project:
- [Jubril Akolade](https://www.linkedin.com/in/jubrillionaire/?originalSubdomain=ca) my Code Institute mentor
- The Code Institute Student Care team, community@codeinstitute.net and Heroku team for helping register my credits and thus process my project deployment. 


 
