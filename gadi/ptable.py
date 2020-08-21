from datetime import date 
import urllib.request
from bs4 import BeautifulSoup
def petrol_price():
    today = date.today()
    wiki = "https://www.sify.com/finance/today-petrol-price/"
    page = urllib.request.urlopen(wiki)
    k = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <title>Fuel Price</title>
        <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
      </head>
      <body>
        <!-- Navigation -->
    <nav class="navbar navbar-dark bg-dark">
        <a class="navbar-brand" href="/">
          <img src="/static/images/logo.png" width="30" height="30" class="d-inline-block align-top" alt="logo">
          <font >gadi</font>
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse text-center" id="navbarTogglerDemo01">
              <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                <li class="nav-item ">
                  <a class="nav-link" href="/home">Home</a>
                </li>
                <li class="nav-item">
                        <a class="nav-link" href="/login">log-in</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="/about">About</a>
                </li>
                <li class="nav-item">
                        <a class="nav-link" href="/contact">Contact</a>
                </li>
                <li class="nav-item">
                        <a class="nav-link" href="/help">Help</a>
                </li>
              </ul>
              <form class="form-inline my-2 my-lg-0 justify-content-center">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
              </form>
            </div>
        </nav>
        <h3 style="background-color:#b3b3b3;">PETROL PRICE OF {today} :</h3>
        <center><table border=2 bgcolor="#b3b3b3">
        <th bgcolor="#4d4d4d" style="color:white;">Place</th>
        <th bgcolor="#4d4d4d" style="color:white;">Today's Price</th>
        <th bgcolor="#4d4d4d" style="color:white;">Yesterday's Price</th>
        <th bgcolor="#4d4d4d" style="color:white;">Difference</th>
        """
    soup = BeautifulSoup(page,features="lxml")
    all_tables=soup.find_all('table')
    right_table=soup.find('table')
    A=[]
    B=[]
    C=[]
    D=[]
    i = 0
    for row in right_table.findAll("tr"):
        cells = row.findAll('td')
        if len(cells)==4 and i!=0: #Only extract table body not heading
            A.append(" ".join(cells[0].find(text=True).split(" ")))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
        elif i==0:
            i+=1
    for i in range(len(A)):
        k=k+"<tr>"
        k += f"<td>{A[i]}</td>"
        k += f"<td>{B[i]}</td>"
        k += f"<td>{C[i]}</td>"
        k += f"<td>{D[i]}</td>"
        k=k+"</tr>\n"
    message = f"""
    {k}
    </table></center></body>
    </html>"""
    path = 'D:\\Gadi_By_FlasK\\Gadi_By_FlasK\\templates\\petrolprice.html'

    with open(path, 'w') as f:
        f.write(message)
        f.close()
