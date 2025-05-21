from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>US Crime Statistics</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #222;
            color: #fff;
            background-image: radial-gradient(#000000 1px, transparent 1px), radial-gradient(#000000 1px, transparent 1px);
            background-position: 0 0, 25px 25px;
            background-size: 50px 50px;
        }

        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }

        h1, h2 {
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        .graph {
            width: 400px;
            height: 300px;
            background-color: #fff;
            margin-bottom: 20px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>US Crime Statistics</h1>
        <br>
        <div class="btn-group-vertical">
            <button class="btn btn-primary" onclick="redirectTo('page1.html')">Data Quality Initial Assessment</button>
            <button class="btn btn-primary" onclick="redirectTo('page1_1.html')">Exploratory Data Analysis</button>
            <button class="btn btn-primary" onclick="redirectTo('page2.html')">Q1. What are the most common types of crimes recorded in the dataset?</button>
            <button class="btn btn-primary" onclick="redirectTo('page3.html')">Q2. Can the data reveal any noticeable trends or patterns in crime reporting over a prolonged timeframe?</button>
            <button class="btn btn-primary" onclick="redirectTo('page4.html')">Q3. What's the analysis of Crime Rates Across Police Districts?</button>
            <button class="btn btn-primary" onclick="redirectTo('page5.html')">Q4. How do the patterns of drug, alcohol, property, and societal crimes vary across different times of the day, such as morning, afternoon, evening, and night?</button>
            <button class="btn btn-primary" onclick="redirectTo('page6.html')">Q5. How do the prevalences of specific crime types vary across different cities?</button>
            <button class="btn btn-primary" onclick="redirectTo('page7.html')">Q6. What is the distribution of crimes across different sectors and beats?</button>
            <button class="btn btn-primary" onclick="redirectTo('page8.html')">Q7. Is there a relationship between the time of day and the occurrence of certain crimes?</button>
            <button class="btn btn-primary" onclick="redirectTo('page9.html')">Q8. How do crime rates vary based on the day of the week?</button>
            <button class="btn btn-primary" onclick="redirectTo('page10.html')">Q9. What is the average response time of law enforcement (from dispatch to arrival) for reported crimes?</button>
            <button class="btn btn-primary" onclick="redirectTo('page11.html')">Q10. How do crime rates differ between weekdays and weekends, and is there a variation in the types of crimes reported?</button>
        </div>
    </div>

    <script>
        function redirectTo(page) {
            window.location.href = page;
        }
    </script>
</body>

</html>

    """

@app.get("/page1.html", response_class=HTMLResponse)
def page1():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Preliminary Data Analysis</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid white;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #444;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>This is the initial assessment of the US Crime Statistics dataset</h1>
        <div class="content">
            <h2>Pre-Cleaning Observation</h2>
            <p>Based on Data Type Checking and Statistical Summary observations:</p>
            <ul>
                <li>Consider altering the data types of CR Number, Zip Code, and Address Number to CHAR or STRING, as they are not involved in calculations, and representing them as strings could enhance trend comprehension.</li>
                <li>Similarly, propose changing Dispatch Date/Time, Start_Date_Time, and End_Date_Time to DATE types to facilitate time series trend analysis.</li>
            </ul>
            <p>This datatype adjustment enables simple statistical observations for enhanced insight generation using the describe() function.





            </p>

            <!-- Add the table below -->
            <h3>Column Metadata</h3>
            <table>
                <tr>
                    <th>#</th>
                    <th>Column</th>
                    <th>Metadata</th>
                </tr>
                <tr>
                    <td>0</td>
                    <td>Incident ID</td>
                    <td>Incident ID</td>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Offence Code</td>
                    <td>Code offended</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>CR Number</td>
                    <td>Case / Crime Report Number</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Dispatch Date / Time</td>
                    <td>The actual date and time a Officer was dispatched</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>NIBRS Code</td>
                    <td>FBI National Incident-Based Reporting System (NIBRS) Code</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Victims</td>
                    <td>Number of Victims</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Crime Name1</td>
                    <td>TType of Crime Commited (Crime against Society/Person/Property or Other)</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>Crime Name2</td>
                    <td>Crime Category (Describes the NIBRS_CODE)</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td>Crime Name3</td>
                    <td>Crime information(Describes the OFFENSE_CODE)</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td>Police District Name</td>
                    <td>Name of District where crime was commited</td>
                </tr>
                <tr>
                    <td>10</td>
                    <td>Block Address</td>
                    <td>Address in 100 block level</td>
                </tr>
                <tr>
                    <td>11</td>
                    <td>City</td>
                    <td>City where the crime took place</td>
                </tr>
                <tr>
                    <td>12</td>
                    <td>State</td>
                    <td>State where the crime took place</td>
                </tr>
                <tr>
                    <td>13</td>
                    <td>Zip Code</td>
                    <td>Zip Code of block where crime took place</td>
                </tr>
                <tr>
                    <td>14</td>
                    <td>Agency</td>
                    <td>Assigned Police Department</td>
                </tr>
                <tr>
                    <td>15</td>
                    <td>Place</td>
                    <td>Place description</td>
                </tr>
                <tr>
                    <td>16</td>
                    <td>Sector</td>
                    <td>Police sector name, a subset of District</td>
                </tr>
                <tr>
                    <td>17</td>
                    <td>Beat</td>
                    <td>Police patrol area, a subset of Sector</td>
                </tr>
                <tr>
                    <td>18</td>
                    <td>Dispatch Date / Time</td>
                    <td>The actual date and time a Officer was dispatched</td>
                </tr>
                <tr>
                    <td>19</td>
                    <td>PRA</td>
                    <td>Police Response Area, a subset of Beat</td>
                </tr>
                <tr>
                    <td>20</td>
                    <td>Street Prefix</td>
                    <td>North, South, East, West</td>
                </tr>
                <tr>
                    <td>21</td>
                    <td>Street Name</td>
                    <td>Street Name</td>
                </tr>
                <tr>
                    <td>22</td>
                    <td>Street Suffix</td>
                    <td>Street Suffix</td>
                </tr>
                <tr>
                    <td>23</td>
                    <td>Street Type</td>
                    <td>Quadrant (NW, SW, etc)</td>
                </tr>
                <tr>
                    <td>24</td>
                    <td>Start_Date_Time</td>
                    <td>Crime occurred from date/time</td>
                </tr>
                <tr>
                    <td>25</td>
                    <td>End_Date_Time</td>
                    <td>The date and time when the investigation was closed</td>
                </tr>
                <tr>
                    <td>26</td>
                    <td>Latitude</td>
                    <td>Latitude co-ordinates of crime area</td>
                </tr>
                <tr>
                    <td>27</td>
                    <td>Longitude</td>
                    <td>Longitude co-ordinates of crime area</td>
                </tr>
                <tr>
                    <td>28</td>
                    <td>Police District Number</td>
                    <td>Major Police Boundary</td>
                </tr>
                <tr>
                    <td>29</td>
                    <td>Location</td>
                    <td>Location (Latitude, Longitude)</td>
                </tr>
            </table>
            <br>
            <br>
            <!-- Missing Values Observation Table -->
            <h3>Missing Values Observation before cleaning the data</h3>
            <p>The total percentage of missing values is: 10.47%</p>
            <p>Combined Summary Table:</p>
            <table>
                <tr>
                    <th></th>
                    <th>Count of Missing Values</th>
                    <th>Percentage of Missing Values (%)</th>
                </tr>
                <tr>
                    <td>Offence Code</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>CR Number</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Dispatch Date / Time</td>
                    <td>49029.0</td>
                    <td>16.02</td>
                </tr>
                <tr>
                    <td>NIBRS Code</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Victims</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Crime Name1</td>
                    <td>272.0</td>
                    <td>0.09</td>
                </tr>
                <tr>
                    <td>Crime Name2</td>
                    <td>272.0</td>
                    <td>0.09</td>
                </tr>
                <tr>
                    <td>Crime Name3</td>
                    <td>272.0</td>
                    <td>0.09</td>
                </tr>
                <tr>
                    <td>Police District Name</td>
                    <td>94.0</td>
                    <td>0.03</td>
                </tr>
                <tr>
                    <td>Block Address</td>
                    <td>26206.0 </td>
                    <td>8.56</td>
                </tr>
                <tr>
                    <td>City</td>
                    <td>1277.0</td>
                    <td>0.42</td>
                </tr>
                <tr>
                    <td>State </td>
                    <td>1.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Zip Code</td>
                    <td>3179.0</td>
                    <td>1.04</td>
                </tr>
                <tr>
                    <td>Agency</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Place</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Sector</td>
                    <td>1530.0</td>
                    <td>0.5</td>
                </tr>
                <tr>
                    <td>Beat</td>
                    <td>1530.0</td>
                    <td>0.5</td>
                </tr>
                <tr>
                    <td>PRA</td>
                    <td>239.0</td>
                    <td>0.08</td>
                </tr>
                <tr>
                    <td>Address Number</td>
                    <td>26109.0</td>
                    <td>8.53</td>
                </tr>
                <tr>
                    <td>Street Prefix</td>
                    <td>292463.0</td>
                    <td>95.55</td>
                </tr>
                <tr>
                    <td>Street Name</td>
                    <td>1.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Street Suffix</td>
                    <td>300662.0</td>
                    <td>98.23</td>
                </tr>
                <tr>
                    <td>Street Type</td>
                    <td>339.0</td>
                    <td>0.11</td>
                </tr>
                <tr>
                    <td>Start_Date_Time</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>End_Date_Time</td>
                    <td>161658.0</td>
                    <td>52.81</td>
                </tr>
                <tr>
                    <td>Police District Number</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Location</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
            </table>
            <br>
            <br>
            <!-- Observations Section -->
            <h3>Observations</h3>
            <h4>Column Evaluation and Missing Data Analysis</h4>
            <hr>
            <p>Several columns (`Block Address`, `Address Number`, `Latitude`, `Longitude`, `Street Prefix`, and `Street Suffix`) are identified as redundant and will be removed due to either duplicative information or a high percentage of missing values.</p>
            
            <ul>
                <li>`Block Address`: Redundant composite of existing columns (`Address Number`, "BLK", `Street Name`, `Street Type`).</li>
                <li>`Address Number`: Impractical to recover missing data; overshadowed by more informative `Place` column.</li>
                <li>`Latitude` and `Longitude`: Redundant due to inclusion in the comprehensive `Location` column.</li>
                <li>`Street Prefix` and `Street Suffix`: Lack analytical significance with over 95% missing values, rendering them inconsequential.</li>
            </ul>
            
            <p>Additionally, missing values in `End_Date_Time` suggest ongoing investigations, aligning with dataset documentation. Proposed resolution involves estimating investigation conclusion based on crime type-specific average resolution times. For Dispatch Date / Time, further investigation is needed to determine reasons for missing values.
            </p>

            <br>
            <br>
            <h3>Analysis of Missing Values in "End_Date_Time" Column:</h3>
            <p>The occurrence of missing values in the "End_Date_Time" column suggests that certain cases remain actively under investigation. These instances may necessitate further inquiry or await additional developments before a conclusive resolution is attained.<br><br>

                Corroborating this observation, the provided dataset documentation (accessible at https://catalog.data.gov/dataset/crime) substantiates the indication that the "End_Date_Time" column encompasses records still in progress or subject to ongoing investigation. This implies that the absence of values is not attributed to data collection errors but rather reflects the ongoing nature of specific crime cases.<br><br>
                
                To address these missing values, a prospective approach involves calculating the average time typically required to resolve cases based on different crime types. This calculated average time can then be added to the investigation start date and time, subsequently serving as an estimation for the missing "End_Date_Time" values, thereby reflecting the conclusion of the respective investigations.</p>
            </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>


    """

@app.get("/page1_1.html", response_class=HTMLResponse)
def page1_1():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Exploratory Data Analysis</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid white;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #444;
            color: #fff;
        }
        .highlight {
            background-color: yellow;
            padding: 0 5px; /* Add padding for better visibility */
            color: black;
        }
        
    </style>
</head>
<body>
    <div class="container">
        <h1>This is the Exploratory Data Analysis (EDA) of the US Crime Statistics dataset</h1>
        <caption>Statistical Summary for Numeric Data:</caption>
        <table>
            <tr>
                <th></th>
                <th>Victims</th>
            </tr>
            <tr>
                <td>count</td>
                <td>306094.0</td>
            </tr>
            <tr>
                <td>mean</td>
                <td>1.0226923755447672</td>
            </tr>
            <tr>
                <td>std</td>
                <td>0.19231084669516194</td>
            </tr>
            <tr>
                <td>min</td>
                <td>1.0</td>
            </tr>
            <tr>
                <td>25%</td>
                <td>1.0</td>
            </tr>
            <tr>
                <td>50%</td>
                <td>1.0</td>
            </tr>
            <tr>
                <td>75%</td>
                <td>1.0</td>
            </tr>
            <tr>
                <td>max</td>
                <td>22.0</td>
            </tr>
        </table>
        <br>
        <br>
        <h3>2. <strong>Observations:</strong></h3>
        <p>The following columns have the missing values which either could be dropped or we will perform imputing steps using <em>mode()</em> with <em>groupby()</em> and <em>GoogleMaps</em> API services for retrieving missing and incorrect values. For, few we will use impute some random values or drop rows if there is no understanding.</p>
        <ul>
            <li>Using <em>mode()</em> and <em>groupby()</em>
                <ul>
                    <li>Crime Name1, Crime Name2, and Crime Name3</li>
                    <li>Police District Name</li>
                </ul>
            </li>
            <li>Drop the columns
                <ul>
                    <li>Sector, Beat, and PRA</li>
                </ul>
            </li>
            <li>Using <em>GoogleMaps</em>
                <ul>
                    <li>City, Zip Code, Address Number, Street Name, and Street Type</li>
                </ul>
            </li>
            <li>Drop columns Block Address,Address Number, Street Prefix and Street Suffix based on Data Cleaning</li>
            <l1>Drop rows where Location has '0.0, 0.0' and contains '90.0' as latitude and longitude.</l1>
        </ul>
        <br>
        <br>
        <ul>
            <li>After performing some groupby tasks on Excel, we could conclude that there is no such pattern using which we could come to a conclusion with which column we groupby either of these columns and apply <em>mode()</em> to fill missing values.</li>
            <li>The count of missing values is less than 1% of the total data in the dataframe.</li>
            <li>Wherever there is <em>TPPD</em> or <em>OTHER</em> in <code>Police District Number</code>, only there are missing values in columns <code>Sector</code> and <code>Beat</code>. Even after an internet search, we were unable to find any good and accurate evidence to prove what <em>TPPD</em> and <em>OTHER</em> mean in the <code>Police District Number</code> column.</li>
            <li>Columns <code>Sector</code> and <code>Beat</code> have the same count and rows of missing values, i.e., 1350.</li>
            <li>Therefore, we concluded to drop rows where all these columns have missing values.</li>
        </ul>
        

        <div class="container">
            
            <h3>Missing Values Observation after cleaning the data</h3>
            <h5>The total percentage of missing values after cleaning the data is: <span class="highlight">0.71%</span></h5>

            <table>
                <tr>
                    <th></th>
                    <th>Count of Missing Values</th>
                    <th>Percentage of Missing Values (%)</th>
                </tr>
                <tr>
                    <td>Offence Code</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>CR Number</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Dispatch Date / Time</td>
                    <td>48840.0</td>
                    <td>16.43</td>
                </tr>
                <tr>
                    <td>NIBRS Code</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Victims</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Crime Name1</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Crime Name2</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Crime Name3</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Police District Name</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>City</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>State</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Zip Code</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Agency</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Place</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Sector</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Beat</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>PRA</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Street Name</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Street Type</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Start_Date_Time</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>End_Date_Time</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Police District Number</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
                <tr>
                    <td>Location</td>
                    <td>0.0</td>
                    <td>0.0</td>
                </tr>
            </table>
            
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

"""

@app.get("/page2.html", response_class=HTMLResponse)
def page2():
    return """
<!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>What are the most common types of crimes recorded in the dataset?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 120%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q1. What are the most common types of crimes recorded in the dataset?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/01_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/01_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
        <h3>Insights:</h3>
        <ul>
            <li>The analysis of crime data reveals that 'Theft From Motor Vehicle' emerges as the predominant crime type. This is evidenced by its prominent representation in the bar chart, where it leads in frequency compared to other crime categories.</li>
            <li>In terms of prevalence, 'Drug/Narcotic Violations' and 'Simple Assault' are also significant, ranking second and third, respectively. This indicates a notable occurrence of these crime types within the studied dataset.</li>
            <li>A closer examination through a pie chart representation shows that 'Theft From Motor Vehicle' constitutes 16.2% of the top 10 crime categories. This percentage underscores its substantial proportion in the overall crime composition, marking it as the most substantial segment among the leading crime types.</li>
            <li>The deliberate exclusion of the category 'All Other Offenses' in the data visualizations serves a specific analytical purpose. It allows for a more focused examination of distinct crime types, rather than encompassing a broad and potentially diverse range of less frequent offenses. This approach facilitates a clearer understanding of specific crime trends and patterns, rather than diluting the analysis with a heterogeneous and less informative category.</li>
        </ul>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

"""

@app.get("/page3.html", response_class=HTMLResponse)
def page3():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Can the data reveal any trends in crime reporting over a prolonged timeframe?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 120%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q2. Can the data reveal any noticeable trends or patterns in crime reporting over a prolonged timeframe?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/02_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/02_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
        <h3>Insights:</h3>
        <p><strong>Insight 1:</strong></p>
        <ul>
            <li><strong>2016 - 2020:</strong></li>
                <ul>
                    <li>Between these years, the highest number of reported crimes occurred from mid to the end of the year.</li>
                    <li>This trend can be attributed to increased holidays, leading to more vacant homes, and higher theft rates in city centers and vacation spots.</li>
                </ul>
            <li><strong>2020 - 2022:</strong></li>
                <ul>
                    <li>During this period, a surge in crime is observed at the start of the year, possibly due to holiday-related travel and an increase in burglaries.</li>
                    <li>The years also experienced a rise in cybercrime during the COVID-19 lockdown, contributing to spikes in crime reports in different months.</li>
                </ul>
        </ul>
        <p><strong>Insight 2:</strong></p>
        <ul>
            <li>There is a consistent decline in reported crime rates after 2020, likely influenced by COVID-19 restrictions that limited people's mobility.</li>
            <li>However, there are spikes in crime, especially cybercrimes, suggesting shifts in criminal activity patterns during certain months.</li>
        </ul>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

"""

@app.get("/page4.html", response_class=HTMLResponse)
def page4():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>what's the analysis of Crime Rates Across Police Districts?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 120%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q3. What's the analysis of Crime Rates Across Police Districts?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/03_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/03_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
        <h3>Insights:</h3>
        <ul>
            <li>The data visualization distinctly indicates that the City of Takoma Park exhibits the lowest crime rate, accounting for merely 2.2% of the total, which is significantly lower compared to other cities where crime rates are predominantly in double digits.</li>
            <li>In contrast, Silver Spring emerges as the city with the highest crime rate, constituting 21.1% of the total. This is closely followed by Wheaton and Montgomery Village, which rank second and third, respectively, in terms of high crime rates.</li>
            <li>The pronounced disparity in crime rates between the City of Takoma Park and other cities may be attributed to factors such as a lower population density, varying socioeconomic conditions, and differing law enforcement strategies.</li>
        </ul>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

"""

@app.get("/page5.html", response_class=HTMLResponse)
def page5():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>How do the patterns of drug, alcohol, property, and societal crimes vary across different times of the day, such as morning, afternoon, evening, and night?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 120%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q4. How do the patterns of drug, alcohol, property, and societal crimes vary across different times of the day, such as morning, afternoon, evening, and night?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/04_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/04_bar_1.png?raw=true" alt="box plot of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/04_bar_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/04_bar_3.png?raw=true" alt="box plot of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/04_bar_4.png?raw=true" alt="box plot of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/04_bar_5.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
        <h3>Insights:</h3>
        <ul>
            <li>Analytical scrutiny of crime data visualizations reveals a pronounced trend of increased criminal activity during evening and nighttime hours. This pattern is particularly evident in the frequency of crimes occurring in these time periods.</li>
            <li>The evening and night hours are notably associated with a higher incidence of specific crime types, including drug and narcotic offenses, vehicular accidents, trespassing, assault, violations of weapon laws, and incidents influenced by alcohol consumption.</li>
            <li>This trend may be attributed to several factors. Firstly, the propensity for increased alcohol consumption post-work hours or during weekends can lead to a rise in such criminal behaviors. Secondly, the cover of darkness may embolden individuals to engage in trespassing and other illicit activities.</li>
            <li>Conversely, daytime hours, particularly mornings, witness a different pattern of criminal activity. Crimes such as burglary, property vandalism, shoplifting, motor vehicle theft, identity theft, and assault are more frequently reported during these times.</li>
            <li>This shift in crime type can be linked to behavioral patterns where individuals typically leave their homes for work, thereby presenting opportunities for property-related crimes. The absence of occupants in residential areas during work hours potentially facilitates the commission of such crimes, reflecting a strategic choice by offenders to exploit the reduced risk of detection.</li>
        </ul>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

"""

@app.get("/page6.html", response_class=HTMLResponse)
def page6():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>How do the prevalences of specific crime types vary across different cities?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 120%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q5. How do the prevalences of specific crime types vary across different cities?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/05_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/05_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
        <h3>Insights:</h3>
        <ul>
            <li>Analysis of the data indicates that crimes categorized as 'Crime Against Property' are predominantly reported. This category encompasses offenses such as trespassing, burglary, and property vandalism.</li>
            <li>Further insights derived from the visualizations reveal that Silver Spring ranks highest in criminal activities related to property, followed by crimes against society and other types of offenses.</li>
            <li>The top five cities with the highest incidence of crimes against property, society, and individuals are Silver Spring, Gaithersburg, Rockville, Germantown, and Bethesda. These cities are notable for their high development and population density within Montgomery County, Maryland. This correlation suggests a potential link between urban development, population density, and crime rates, warranting further investigation into the socio-economic factors influencing these trends.</li>
        </ul>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

"""

@app.get("/page7.html", response_class=HTMLResponse)
def page7():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Preliminary Data Analysis</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 120%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q6. What is the distribution of crimes across different sectors and beats?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/06_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/06_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
        <h3>Insights:</h3>
        <p>Across various sectors, Sector P emerges as the most crime-prone, closely followed by sectors A, G, D, R, and L. This ranking is based on the frequency and intensity of reported criminal activities, indicating a potential correlation between sector-specific factors and crime prevalence.</p>
        <p>In stark contrast, Sector T is identified as the sector with the minimal incidence of crime. This significantly lower crime rate could be attributed to a range of factors, including effective law enforcement strategies, socio-economic conditions, or community engagement in crime prevention.</p>
        <p>Delving deeper into the data, specific beats within each high-crime sector are identified as focal points of criminal activity. In Sector P, Beat P63 registers the highest crime rate, while in Sector A, it is Beat 1A3. Similarly, Beats 3G1, 2D2, 6R2, 4L2, and 8TR are the most crime-affected within Sectors G, D, R, L, and T, respectively. These beats may require targeted interventions and resource allocation to effectively manage and mitigate crime.</p>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

    """


@app.get("/page8.html", response_class=HTMLResponse)
def page8():
    return """
    
<!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Is there a relationship between the time of day and the occurrence of certain crimes?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 120%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q7. Is there a relationship between the time of day and the occurrence of certain crimes?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/07_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/07_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
        <h3>Insights:</h3>
        <p>The observed pattern of increased crime reports during midnight and nighttime hours, accompanied by a decrease around dawn, can be attributed to various factors:</p>
        <ol>
            <li><strong>Cover of Darkness:</strong> Criminals exploit the reduced visibility during midnight and evening hours, using the cover of darkness to carry out illegal activities unnoticed.</li>
            <li><strong>Social Activities:</strong> Elevated social interactions during evening and night hours, such as gatherings and nightlife, contribute to a higher likelihood of reported incidents.</li>
            <li><strong>Alcohol Consumption:</strong> Higher alcohol consumption during late evening and nighttime, particularly in social settings, may lead to disturbances and altercations, resulting in an increase in reported crimes.</li>
            <li><strong>Reduced Surveillance:</strong> A decrease in public and residential surveillance around midnight provides an opportune environment for certain criminal activities to occur without immediate detection.</li>
            <li><strong>Shift in Patrol Patterns:</strong> Law enforcement agencies adjust patrol patterns to focus on nighttime hours based on historical crime trends, increasing the likelihood of incidents being reported.</li>
            <li><strong>Victim Vulnerability:</strong> Victims are more vulnerable during nighttime hours due to isolation or limited assistance, leading to an exploitation of this vulnerability by criminals and subsequently an increase in reported crimes.</li>
            <li><strong>Deterrent Effect at Dawn:</strong> The increasing daylight around dawn serves as a deterrent to criminal activities, as improved visibility makes engaging in illegal actions riskier, potentially resulting in a decrease in reported crimes.</li>
        </ol>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>


    """



@app.get("/page9.html", response_class=HTMLResponse)
def page9():
    return """
<!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>How do crime rates vary based on the day of the week?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 120%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q8. How do crime rates vary based on the day of the week?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/08_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/08_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
    </div>

    <div class="container">
        <h3>Insights: Observation of Weekly Crime Patterns</h3>
        <p>
            There is a consistent pattern in the dataset wherein crime rates exhibit peaks on Fridays, followed by Wednesdays and Thursdays, with the lowest incidence reported on Sundays. Several contributing factors to this trend can be identified:
        </p>

        <ol>
            <li><strong>Weekend Social Dynamics:</strong> The initiation of the weekend on Fridays leads to elevated social activities, potentially contributing to a heightened reporting of incidents.</li>
            <li><strong>Late-Week Fatigue Influence:</strong> Increased stress or fatigue towards the end of the workweek, specifically on Thursdays and Fridays, may amplify the likelihood of reported incidents.</li>
            <li><strong>Nightlife Impact:</strong> Fridays, synonymous with nightlife and socializing, may witness increased crime reports due to heightened evening activities.</li>
            <li><strong>Midweek Socialization:</strong> Sustained elevated social interactions on Wednesdays and Thursdays may exert an influence, potentially shaping the number of reported incidents.</li>
            <li><strong>Workweek Routines:</strong> Policing resources may be strategically allocated based on historical trends, with Fridays receiving heightened attention due to consistently higher crime reports.</li>
            <li><strong>Weekend Preparations:</strong> Sundays, characterized by reduced social activities as individuals prepare for the workweek, may result in a decrease in reported incidents.</li>
            <li><strong>Policing Resource Allocation:</strong> Law enforcement agencies may allocate resources and adapt patrol patterns based on observed crime trends, thereby influencing reporting frequencies.</li>
            <li><strong>Data Collection Practices:</strong> Reporting agencies, with varying operational hours or staffing levels on weekends, might impact the number of reported crimes.</li>
            <li><strong>Routine Activities Theory:</strong> According to the routine activities theory, crime occurrence is influenced by the convergence of a motivated offender, a suitable target, and the absence of a capable guardian. These elements may align differently on Fridays compared to Sundays, contributing to the observed weekly variation in crime rates.</li>
        </ol>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

    """


@app.get("/page10.html", response_class=HTMLResponse)
def page10():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page1.html -->
<!DOCTYPE html>
<html>
<head>
    <title>What is the average response time of law enforcement (from dispatch to arrival) for reported crimes?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .center-align {
            justify-content: center;
            align-items: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }
        .image-container img {
            width: 50%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q9. What is the average response time of law enforcement (from dispatch to arrival) for reported crimes?</h1>
        <div class="center-align">
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/09_1.png?raw=true" alt="distribution of law enforcement response time">
            </div>
            <div class="image-container">
                <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/09_2.png?raw=true" alt="box plot of law enforcement response time">
            </div>
        </div>
    </div>
    <div class="container">
        <h3>Insights into Weekday-Weekend Crime Variation:</h3>
        <p>In scrutinizing the visualizations depicting the average response time of law enforcement from dispatch to arrival for reported crimes, notable patterns and potential contributing factors have been discerned.</p>
        <br>
        <p>Decline in Response Time Frequency:
            The temporal analysis reveals a discernible decline in the frequency of law enforcement response times, particularly evident from late 2019 to early 2020. A plausible contributing factor to this trend is the global pandemic, namely COVID-19. Although establishing a causal relationship between the pandemic and the observed decline is challenging, a conspicuous correlation is evident. The implementation of mandatory quarantines, especially in major metropolitan areas, may have led to a reduction in the deployment of law enforcement officers, thereby influencing response times.</p>
        <br>
        <h4>Analytical Approaches:</h3>

    <p><strong>Temporal Analysis:</strong><br>
    Implementing time series analysis identifies anomalies and trends in law enforcement response times, offering insights into temporal dynamics.</p>

    <p><strong>Correlation Assessment:</strong><br>
    Computing Pearson correlation coefficients quantifies the strength and direction of the relationship between response times and key events, revealing external influences.</p>

    <p><strong>Spatial Mapping:</strong><br>
    Utilizing geospatial mapping discerns regional variations in response times, enhancing understanding of localized pandemic impacts.</p>

    <p><strong>Cohort Stratification:</strong><br>
    Stratifying data based on geographic and demographic factors allows nuanced examination of response time variations across distinct segments.</p>

    <p><strong>Regression Modeling:</strong><br>
    Constructing regression models assesses the statistical significance of the pandemic's impact on response times, considering potential confounding variables.</p>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>


    """


@app.get("/page11.html", response_class=HTMLResponse)
def page11():
    return """
    <!-- FILEPATH: /C:/Users/Abin/OneDrive/Desktop/MSc Data Science/Applied Data Programming/Coursework 1/US_crime_statistics/templates/page11.html -->
<!DOCTYPE html>
<html>
<head>
    <title>How do crime rates differ between weekdays and weekends, and is there a variation in the types of crimes reported?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .content {
            margin-top: 50px;
            text-align: justify;
            background-color: #000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .image-container img {
            width: 50%;
            height: auto;
            margin: 10px;
        }
        .image-container2 img {
            width: 50;
            height: auto;
            margin: 10px;
            align-items: center;
            justify-content: center;
            display: flex;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Q10. How do crime rates differ between weekdays and weekends, and is there a variation in the types of crimes reported?</h1>
        <div class="image-container">
            <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/10_pie_1.png?raw=true" alt="weekdays">
            <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/10_pie_2.png?raw=true" alt="weekends">
        </div>
        <div class="image-container2">
            <img src="https://github.com/Spartan-119/MSc-Data-Science/blob/main/adp/10_1.png?raw=true" alt="crime variation">
        </div>

        <!-- Insights Section -->
        <h3>Insights into Weekday-Weekend Crime Variation:</h3>
        <p>In response to the inquiry on weekday-weekend crime rate distinctions and crime type variations, a comprehensive examination reveals distinct patterns. Notably, "crime against property" consistently predominates during both weekdays and weekends, succeeded by "other" crimes, "crime against society," and, lastly, "crime against person."</p>

        <h4>Statistical Rationale:</h4>

        <p><strong>1. Robust Prevalence of Property Crimes:</strong></p>
        <ul>
            <li>Statistical metrics, including mean and median comparisons, substantiate the enduring significance of "crime against property" across temporal domains.</li>
        </ul>

        <p><strong>2. Stability in "Other" Crimes:</strong></p>
        <ul>
            <li>The consistent frequency of "other" crimes suggests relative stability, warranting further exploration through standard deviation analysis.</li>
        </ul>

        <p><strong>3. Gradual Decline in Severity:</strong></p>
        <ul>
            <li>A sequential decrease from "crime against society" to "crime against person" implies nuanced variations in offense nature and severity.</li>
        </ul>

        <h4>Scientific Significance:</h4>

        <p>These observed patterns reflect the intricate interplay of socio-economic factors on crime types. Advanced statistical models and temporal analysis techniques could offer deeper insights. The findings emphasize the multifaceted nature of criminal activities, prompting a nuanced approach to understanding and addressing diverse crime facets within distinct temporal contexts.</p>
        
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </div>
</body>
</html>

    """


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
