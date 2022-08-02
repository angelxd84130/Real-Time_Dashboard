
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h2 align="center">Real-Time Dashboard</h2>

  <p align="center">
    Real-Time transaction analysis dashboard  
    <br />  
    <a href="https://github.com/angelxd84130/Real-Time_Dashboard/issues">Report Bug</a>
    ·
    <a href="https://github.com/angelxd84130/Real-Time_Dashboard/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#data-extraction">Data Extraction</a></li>
        <li><a href="#data-processing">Data Processing</a></li>
        <li><a href="#visualization">Visualization</a></li>
        <li><a href="#evaluation">Evaluation</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The goal is to design a dashboard to monitor data in real time faster, and make relevant countermeasures based on the analyzed data.
This interactive dashboard shows both the transaction results and the error codes of failed transactions of different sports.   

Here's why:
* More reflective of real-time data than existing visualization tools  
* People who don't use visualization tools can also observe data from the dashboard  
* More flexible to modify the content and method of presentation  

### Data Extraction  
Using SQL to select data from MySQL.   
Since the required data has been processed & stored in MySQL tables in the [AirFlow-ETL](https://github.com/angelxd84130/Airflow-ETL) program, 
it's easier to extract the data we need from tables directly.   
- Adjust SQL based on observation time range  
![Past-Time][product-screenshot0]

- Adjust SQL based on observation different sports  
![Sports][product-screenshot1]  
  
  
### Data Processing  
Appropriately change the data structure according to the Plotly graph.
 

### Visualization   
Display analysis results according to selection.   
- Transaction Accumulation  
![Transaction-Accumulation][product-screenshot2]  
- Transaction Success Ratio  
  - A period     
  ![Peroid][product-screenshot3]  
  - Pre day  
  ![Day][product-screenshot4]  
- Error Codes Accumulation  
![Error-Codes-Acumulation][product-screenshot5]  
- Error Codes Distribution  
![Error-Codes-Distribution][product-screenshot6]  


### Evaluation
Through the 7-day experiment, about 1300 articles can be obtained, and the distribution of 6 categories can be seen from the plot below.   

  

### Built With

* [NewsAPI](https://newsapi.org/docs/client-libraries/python)
* [scikit-learn](https://scikit-learn.org/stable/#)
* [matplotlib](https://matplotlib.org/)
* [nltk](https://www.nltk.org/)



<!-- GETTING STARTED -->
## Getting Started

Start with a python file with any machine learning model ex.NaiveBayes.py  
Download code and repalce the api_key to your own.

### Prerequisites


1. Get a free API Key at [NewsAPI](https://newsapi.org/docs/client-libraries/python)  



<!-- USAGE EXAMPLES -->
## Usage

Use the plots to check result.  



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

Yu-Chieh Wang - [LinkedIn](https://www.linkedin.com/in/yu-chieh-wang/)  
email: angelxd84130@gmail.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Dash Sample APPs](https://github.com/plotly/dash-sample-apps)  




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/angelxd84130/Real-Time_Dashboard.svg?style=for-the-badge
[contributors-url]: https://github.com/angelxd84130/Real-Time_Dashboard/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/angelxd84130/Real-Time_Dashboard.svg?style=for-the-badge
[forks-url]: https://github.com/angelxd84130/Real-Time_Dashboard/network/members
[stars-shield]: https://img.shields.io/github/stars/angelxd84130/Real-Time_Dashboard.svg?style=for-the-badge
[stars-url]: https://github.com/angelxd84130/Real-Time_Dashboard/stargazers
[issues-shield]: https://img.shields.io/github/issues/angelxd84130/Real-Time_Dashboard.svg?style=for-the-badge
[issues-url]: https://github.com/angelxd84130/Real-Time_Dashboard/issues
[license-shield]: https://img.shields.io/github/license/angelxd84130/Real-Time_Dashboard.svg?style=for-the-badge
[license-url]: https://github.com/angelxd84130/Real-Time_Dashboard/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/yu-chieh-wang/
[product-screenshot0]: Past-Time.png
[product-screenshot1]: Sports.png
[product-screenshot2]: Transaction-Accumulation.png
[product-screenshot3]: Peroid.png
[product-screenshot4]: Day.png
[product-screenshot5]: Error-Codes-Acumulation.png
[product-screenshot6]: Error-Codes-Distribution.png
