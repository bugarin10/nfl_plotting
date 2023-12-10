# NFL Plotting 🏈

#### Background

Every year the NFL sponsors a datascience related Kaggle competition. This year the following prompt was proposed for the [NFL Big Data Bowl 2024](https://www.kaggle.com/competitions/nfl-big-data-bowl-2024):

`American football is a complex sport, but once an offensive player receives a handoff or catches a pass, all 11 defenders focus on one task -- tackle that ball carrier as soon as possible. Conversely, the ball carrier's role is to advance the ball down the field to gain as much yardage as possible until he is tackled, scores, or runs out of bounds. This year's competition offers up a general goal — create metrics that assign value to elements of tackling.`

As a part of this competition, the NFL provided AWS Next Gen Player Tracking Stats for specific games in the 2022 NFL season. For our final project, we chose to explore the data by creating a web application that animates the football plays provided by the NFL. We use the player tracking data to plot all 22 players (blue for offense, red for defense) along with the position of the football (brown), for the duration of 1 play. Our animation will display any play from the Buffalo vs Rams 2022 opening game. User input on the web application determines which play to display.

*Note: Because the competition is focused on tackling, the animation begins mid-play - a few frames before the football reaches the primary ball carrier. This means that the animations will not start with all 22 players on the line of scrimage.* 

#### ETL Pipeline 🔌🚰

The ETL (Extract, Transform, Load) pipeline starts by gathering data from our source folder which houses the `games.csv`, `plays.csv`, `tackles.csv`, `players.csv`, and `la_vs_buff.csv`. This raw data is then stored in a Database File System.The transformative phase follows, converting the raw data into Delta Lake tables. Delta Lake provides a structured and versioned storage solution, adding reliability and transactional capabilities to the data processing workflow. Each Delta Lake table corresponds to a specific dataset (games, plays, tackles, players, and la_vs_buff), making it convenient to interact with the data using SQL queries. This relational structure enhances the overall performance of queries and enables the establishment of relationships between different datasets, providing a more comprehensive view of the data.

<img width="848" alt="Screenshot 2023-12-09 at 9 16 56 PM" src="https://github.com/bugarin10/nfl_plotting/assets/125210401/aef5b999-9614-4610-9c6f-1a61b508d1f7">

#### Data Engineering ⚙️⚒️

A user initiates a play by executing an SQL query, connecting to Azure Databricks where the relevant tables are stored. This process retrieves executable data, which is then converted into a Pandas dataframe. Subsequently, the user can visualize a plot of the specific game play through the designated website. The system leverages IaC principles to manage and provision its infrastructure. Infrastructure as Code involves expressing infrastructure configurations in a script or declarative language, enabling the automated deployment and management of resources. In this context, the deployment and configuration of Azure Databricks, along with any associated infrastructure, are codified. This approach enhances reproducibility, scalability, and version control of the entire system's architecture.

#### Github Actions 💡✅

The goal of CI/CD is to enable rapid integration and testing of changes, and to enable continuous delivery of new versions of software by automating the process of building, testing, and deploying code changes.
This repository contains a CI/CD pipeline that is triggered by a push to the main branch. The pipeline is defined in .github/workflows. The files in this folder, each of which defines a different job in the pipeline responsible for `installing packages and dependencies`, `linting`, `formating`, and `testing`. 



