# NFL Plotting 🏈 [![Install](https://github.com/bugarin10/nfl_plotting/actions/workflows/install.yml/badge.svg)](https://github.com/bugarin10/nfl_plotting/actions/workflows/install.yml) [![Format](https://github.com/bugarin10/nfl_plotting/actions/workflows/format.yml/badge.svg)](https://github.com/bugarin10/nfl_plotting/actions/workflows/format.yml) [![Lint](https://github.com/bugarin10/nfl_plotting/actions/workflows/lint.yml/badge.svg)](https://github.com/bugarin10/nfl_plotting/actions/workflows/lint.yml) [![Test](https://github.com/bugarin10/nfl_plotting/actions/workflows/test.yml/badge.svg)](https://github.com/bugarin10/nfl_plotting/actions/workflows/test.yml)

[NFL Plotting Website](https://nflplot.azurewebsites.net/)
Video [here](https://www.youtube.com/watch?v=wR4FVyW0uxY)


![AZURE](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![PYTHON](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![FLASK](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)

#### Background

Every year the NFL sponsors a datascience related Kaggle competition. This year the following prompt was proposed for the [NFL Big Data Bowl 2024](https://www.kaggle.com/competitions/nfl-big-data-bowl-2024):

`American football is a complex sport, but once an offensive player receives a handoff or catches a pass, all 11 defenders focus on one task -- tackle that ball carrier as soon as possible. Conversely, the ball carrier's role is to advance the ball down the field to gain as much yardage as possible until he is tackled, scores, or runs out of bounds. This year's competition offers up a general goal — create metrics that assign value to elements of tackling.`

As a part of this competition, the NFL provided AWS Next Gen Player Tracking Stats for specific games in the 2022 NFL season. For our final project, we chose to explore the data by creating a web application that animates the football plays provided by the NFL. We use the player tracking data to plot all 22 players (blue for offense, red for defense) along with the position of the football (brown), for the duration of 1 play. Our animation will display any play from the Buffalo vs Rams 2022 opening game. User input on the web application determines which play to display.

*Note: Because the competition is focused on tackling, the animation begins mid-play - a few frames before the football reaches the primary ball carrier. This means that the animations will not start with all 22 players on the line of scrimage.* 

![bfaa0876-a750-49c5-9d8c-966a7fa95eff](https://github.com/bugarin10/nfl_plotting/assets/125210401/9c02ede9-8b0c-4ab2-b3ec-a6451ddff528)

#### ETL Pipeline 🔌🚰

The ETL (Extract, Transform, Load) pipeline starts by gathering data from our source folder which houses the `games.csv`, `plays.csv`, `tackles.csv`, `players.csv`, and `la_vs_buff.csv`. This raw data is then stored in a Database File System.The transformative phase follows, converting the raw data into Delta Lake tables. Delta Lake provides a structured and versioned storage solution, adding reliability and transactional capabilities to the data processing workflow. Each Delta Lake table corresponds to a specific dataset (games, plays, tackles, players, and la_vs_buff), making it convenient to interact with the data using SQL queries. This relational structure enhances the overall performance of queries and enables the establishment of relationships between different datasets, providing a more comprehensive view of the data.

<img width="848" alt="Screenshot 2023-12-09 at 9 16 56 PM" src="https://github.com/bugarin10/nfl_plotting/assets/125210401/aef5b999-9614-4610-9c6f-1a61b508d1f7">

#### Data Engineering ⚙️⚒️

A user initiates a play by executing an SQL query, connecting to Azure Databricks where the relevant tables are stored. This process retrieves executable data, which is then converted into a Pandas dataframe. Subsequently, the user can visualize a plot of the specific game play through the designated website. The system leverages IaC principles to manage and provision its infrastructure. Infrastructure as Code involves expressing infrastructure configurations in a script or declarative language, enabling the automated deployment and management of resources. In this context, the deployment and configuration of Azure Databricks, along with any associated infrastructure, are codified. This approach enhances reproducibility, scalability, and version control of the entire system's architecture.

#### AI Pair Programming 🤖

We seamlessly incorporated cutting-edge AI Pair Programming tools, including GitHub Copilot, AWS CodeWhisper, and OpenAI's ChatGPT, to elevate our coding efficiency and precision. Leveraging these advanced AI technologies streamlined the code-writing process for each team member throughout the development stages—from constructing Databricks and Delta Lake tables to generating plots and building the Flask app and HTML. The integration of these tools not only facilitated a smoother workflow but also significantly enhanced the overall coding experience, marking a substantial leap forward in our development practices.

#### Load Test 

Load testing is a form of performance evaluation that gauges a system's capacity to manage a defined load or volume of simultaneous users or transactions. The main objective of load testing is to pinpoint performance bottlenecks, observe system behavior across diverse conditions, and ascertain the application's ability to efficiently handle the anticipated workload.In our case, we subjected our application to a load test with 2000 users attempting to utilize our microservice. The subsequent results illustrate the project's success in withstanding a substantial influx of traffic. The image below provides a detailed representation of the behaviors exhibited by each user, as encapsulated in the locustfile.py.

![total_requests_per_second_1702252168](https://github.com/bugarin10/nfl_plotting/assets/125210401/d2a3f17f-2fbc-452d-beab-590d15827397)

#### Flask 🧪

Basic web application using the Flask framework in Python. The web framework for building the application. A function from Flask that renders HTML templates. A custom function (from return_div module) that likely returns a Plotly plot as an HTML div element. The application has three routes `/:` this route renders the `index.html` template, `/plot.html:` This route renders the `plot.html` template and passes a plot generated by the return_div function as a variable. `/team.html:` This route renders the `team.html` template.

#### Docker 🐳

A Dockerfile is a script used to build a Docker image. The image is a platform for developing, shipping, and running applications in containers. The container is a lightweight, standalone, and executable software package that includes everything needed to run our software, including the code, runtime, libraries, and system tools. This essentially creates a snapshot of the application and its dependencies in a portable and reproducible manner. It also allows us to share and deploy the application consistently across different environments

#### Github Actions 💡✅

The goal of CI/CD is to enable rapid integration and testing of changes, and to enable continuous delivery of new versions of software by automating the process of building, testing, and deploying code changes.
This repository contains a CI/CD pipeline that is triggered by a push to the main branch. The pipeline is defined in .github/workflows. The files in this folder, each of which defines a different job in the pipeline responsible for `installing packages and dependencies`, `linting`, `formating`, and `testing`. 

#### Architecture Design

Below is a diagram of the web application development/deployment architecture. Azure DockerHub and Azure Web Apps were used to deploy the flask application. A SQL database hosted on Azure Databricks was used to store the data.

![image](https://github.com/bugarin10/nfl_plotting/assets/114833075/a12043cd-a6ff-41ab-8d7b-3366e42db5f6)


#### Latency Testing

The Azure Web App provides key metrics that serve as tangible indicators, affirming the successful push and deployment of the container to a public endpoint. These metrics encompass essential performance and utilization data, offering insights into the containerized application's behavior and responsiveness. Key indicators include response times, request throughput, error rates, and resource utilization metrics, collectively reflecting the health and efficiency of the deployed container. Additionally, monitoring aspects such as server response codes, latency, and network performance contribute to a comprehensive assessment of the container's integration with the Azure Web App infrastructure. These metrics not only validate the successful deployment but also serve as valuable benchmarks for ongoing performance monitoring and optimization efforts, ensuring a robust and reliable user experience on the public endpoint.

![9c434b7b-8ab5-4956-b1ad-8bfcf1b68eed](https://github.com/bugarin10/nfl_plotting/assets/125210401/f9ea4fff-5b76-44cb-a6d1-72e2941ac57a)
![9cf79733-7c24-43f8-b8f0-cb43307e1fcc](https://github.com/bugarin10/nfl_plotting/assets/125210401/7161e8b6-9dd7-4e7b-89e5-1048f9ab53a9)


#### Limitations 

- The application encounters a slight delay in execution as it establishes a connection with Databricks and initiates a pipeline, especially noticeable during the first plot generation for a particular play. This initial lag is inherent to the essential processes involved in connecting to external services and executing pipelines.

- The animation initiates midway through a play, limiting the visibility of the entire play sequence due to insufficient collected data. The start point of the animation is constrained by the available dataset, resulting in an incomplete depiction of the play's progression.

#### Future work

- To ameliorate this delay and enhance user experience, strategic measures such as implementing a caching mechanism for previously computed results, introducing asynchronous processing, and optimizing data retrieval processes can significantly mitigate the impact of the initial latency. Furthermore, incorporating lazy loading for plot generation, providing progress indicators to users, and executing background preprocessing during periods of low activity contribute to a smoother and more responsive user interface.
  
- Enhancing data collection mechanisms or extending the dataset may offer a solution to this limitation, enabling a more comprehensive and informative visualization of the entire play, providing users with a more detailed and insightful perspective.


