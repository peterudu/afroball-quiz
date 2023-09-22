# afroBall Quiz

AfroBall Quiz is a python-based [terminal interactive quiz application](/assets/images/quiz-start.webp) with a theme focus on African football The quiz application challenges users to participate on a round of 7 multiple choice questions on a vareity of African football topics. 

AfroBall Quiz is designed to engage its users, test their knowledge of African football, and most importantly ensure that they gain an enjoyable experience taking the quiz.

![Image of the quiz app](/assets/images/amiresponsive.webp)

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
### flowchart
 - [Flowchart](/assets/images/flowchart.webp) design of quiz app
### Wireframes
A simple Balsamiq wireframe of the quiz starting page was used as building guideline for large and small devices.
![Balsamiq wireframe](/assets/images/wireframe.webp)
### Features
The afroBall Quiz application offers some features which are core to the making the quiz function and they include:

- Questions data catalogue - caf_question.json

  - The [json file data catalogue](/assets/images/question-catalogue.webp) is the source for questions and solutions data which is presented to the user of the quiz app. This questions data is imported and used to form a key element of the quiz.
  - The data catalogue is large and diverse. This can actually be extended by the author to make the quiz more exciting for app users.

- Customized, personalized and interractive interface

  - The large ASCII art designed [afroBall title](/assets/images/quiz-title.webp) and welcome message speaks directly to the quiz user creating a user friendly experience.
  - The displayed [quiz statements and questions](/assets/images/app-statements-and-questions.webp) informs the quiz player exactly what he is required to do.
  - The quiz user constantly gets an [answer feedback](/assets/images/quiz-answer-feedback.webp) on whether or not each answer attempt has been successful.

- Randomly mixed quiz questions

  - The integrated python random() method ensures that every new quiz session starts with a new sample of [mixed questions](/assets/images/mixed-questions.webp) making the quiz unpredictable.
  - The afroBall quiz questions offer a multiple choice option helping the user to comprehend possible solutions.

- Handling user errors and input validation

  - When the user is prompted to pass on relevant quiz data, his input response is tested (using [try and except block](/assets/images/try-and-except-block.webp)) to ensure that correct data type and quantity is adopted.
  - If the user gives in an invalid data type the quiz app will display an [error message](/assets/images/error-message.webp) to the user.

- Display user quiz performance

  - The quiz presents the user ability to get and measure his quiz performance for each attempted question and also for the [overall score](/assets/images/overall-score.webp) at the end of each quiz sesson.
  - The overall scores are displayed to the user in points and percentages 

### Languages Used
The language used to create this quiz app was Python
### Frameworks, Libraries & Programs Used
Git was used for version control.

Github was used to save and store the files for the website.

Gitpod workspace was used to write and edit code for the quiz app.

Balsamiq was used to create wireframes for the quiz app.

[Birme](https://www.birme.net/?no_resize=true&image_format=webp) was used to change images to webp format.

[Diagrams.net (previously draw.io)](https://www.drawio.com/) was used to create the flow chart for the quiz app.

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
#### CI PEP8 Online Validation
- Test with CI PEP8 Online validator showed no errors found.
![CI PEP8 Online](/assets/images/ci-pep8.webp)

#### Python Syntax Checker Online
 - I ran the syntax through [python syntax checker](https://extendsclass.com/python-tester.html) with no errors detected.
 ![Python Syntax Checker](/assets/images/python-syntax-checker.webp)

#### JSONLint validator online
 - I ran the caf_questions.json file through [JSONLint validator](https://jsonlint.com/) with no errors detected - valid JSON.
![JSON validator](/assets/images/jsonlint-validator.webp)
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
Full testing was performed on:

- Laptop:
  - Lenovo V15-IGL
- Mobile Device:
  - LG Velvet

I used a laptop and mobile device to conduct the following test:
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ---| ---| ---| ---| ---|
| TERMINAL | | | | |  
| Customized, personalized and interractive interface | How personally does the app approach each individual user | From the first blick of the quiz page the user is asked to enter his name | When the user enters his name the app responds by sending him a welcome message which mentions his previously entered name. | pass |
| Randomly mixed quiz questions | Every new quiz session should consist of a new set of questions | I ran 6 consecutive quiz sessions after one another | The batch of questions asked in each new quiz session deferred from the previous session,. | pass |
|  Handling user errors and input validation | If the quiz user enters a wrong data type or quantity the app should respond by informing him that the input is invalid and the quiz should not proceed until this error is corrected. | I answered some multiple choice questions by entering alphabets instead of numbers or entering numbers greater than 4 or less than 1 | The app responded by sending me an error message each time and this continued until I typed in the correct data type or correct quantity. | pass |
| Display user quiz performance | After every attempted answer by the user the app should get a feedback message whether the attempt was correct or wrong and at the end of every quiz session the app should display the overall score performance to the user. | I played 3 quiz sessions each consisting of a sample of 7 questions | After attempting each question the app either display a "Wrong!" or "Correct!" message depending if the entered answer was accurate. At the end of each quiz session the app display an overall score performance based on a 7 points system and then also interpreted in percentage terms | pass |
| Signup page link | If clicked the user should be redirected to the signup page | Clicked link | Redirects to signup page. | pass |
#### General Testing
- The quiz application was tested on Chrome, Firefox and Edge browsers. The quip worked well on all the browsers.
### Fixed Bugs
### Unfixed Bugs

## Credits
### Code Used

- Code and structure on how to build an interactive python quiz was inspired by article by [Shay Lynn Khan](https://www.makeuseof.com/python-make-interactive-quiz-game/)
- Additional ideas on how to structure a python based quiz was also derived from [Geir Arne Hjelle](https://realpython.com/python-quiz-application/)

### Content

- Data on African football players and information about significant African football events were used as content to build the caf_questions.json file catalogue. These were sourced from the article "The 50 greatest African players of all time" in the [Bleacher Report](https://bleacherreport.com/) and from the [Confederation of African - CAF](https://www.cafonline.com/) website.
- Structure and layout used to build the quiz multiple-choice type questions was inspired by [Fun Trivia](https://www.funtrivia.com/) website

- Method and steps taken to deploy the project to Heroku was based on the example from [Code Institute Love Sandwiches Walkthrough Project](https://codeinstitute.net/de/)
- The structure and layout used to create the README file was modelled on example by [Kera Cudmore](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md)

### Acknowledgements
I acknowledge the following people who helped me complete this project:
- [Jubril Akolade](https://www.linkedin.com/in/jubrillionaire/?originalSubdomain=ca) my Code Institute mentor
- The Code Institute Student Care team, community@codeinstitute.net and Heroku team for helping register my credits and thus process my project deployment. 
