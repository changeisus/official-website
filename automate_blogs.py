        

from msilib.schema import ControlEvent
from urllib.error import ContentTooShortError
import requests
from bs4 import BeautifulSoup

DEFAULT_IMG = 'https://lh3.googleusercontent.com/-5iURCIuk0QY/YY32qBcD6NI/AAAAAAAAATk/dEoL7QXjE5cXBpDw0V4au8ST56QSKkITgCLcBGAsYHQ/image.png' 
DEFAULT_AUTHOR = 'Arham Shah'



def create_single_blog(title,author,date,imageURL,content,hyperlink):
    return f'''
    <div class="col-md-4 d-flex ftco-animate">
          	<div class="blog-entry align-self-stretch">
              <a href="{hyperlink}" class="block-20" style="background-image: url('{imageURL}');">
              </a>
              <div class="text p-4 d-block">
              	<div class="meta mb-3">
                  <div><a href="{hyperlink}">{date}</a></div>
                  <div><a href="{hyperlink}">{author}</a></div>
                </div>
                <h3 class="heading mt-3"><a href="{hyperlink}">{title}</a></h3>
                <p>{content}</p>
              </div>
            </div>
          </div>
    '''

def createFile(blogs):
    blogs_temp=""
    for i in blogs:
        # cleaning the string because html couldnt parse those characters
        content=i["content"][0:100]
        content=content.replace("’","'")
        content=content.replace("“","'")
        content=content.replace("”","'")
        content=content.strip()
        # print(content)
        blogs_temp+=create_single_blog(i["title"],i["author"],i["date"],i["imageURL"],content+"...",i["hyperlink"])
        # print((i["title"],i["author"],i["date"],i["imageURL"],i["content"],i["hyperlink"]))

    entire_page='''

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>CHANGE IS US - Changing Today for Tomorrow</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
        <link href="https://fonts.googleapis.com/css?family=Dosis:200,300,400,500,700" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Overpass:300,400,400i,600,700" rel="stylesheet">

        <link rel="stylesheet" href="css/open-iconic-bootstrap.min.css">
        <link rel="stylesheet" href="css/animate.css">
        
        <link rel="stylesheet" href="css/owl.carousel.min.css">
        <link rel="stylesheet" href="css/owl.theme.default.min.css">
        <link rel="stylesheet" href="css/magnific-popup.css">

        <link rel="stylesheet" href="css/aos.css">

        <link rel="stylesheet" href="css/ionicons.min.css">

        <link rel="stylesheet" href="css/bootstrap-datepicker.css">
        <link rel="stylesheet" href="css/jquery.timepicker.css">

        
        <link rel="stylesheet" href="css/flaticon.css">
        <link rel="stylesheet" href="css/icomoon.css">
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        
    <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
        <div class="container">
            <a class="navbar-brand" href="index.html">Change Is Us</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav"
            aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
            </button>
    
            <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a href="index.html" class="nav-link">Home</a></li>
                <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" href="#">About</a>
                <div class="dropdown-menu">
                    <a href="about.html#problems" class="dropdown-item">Problem</a>
                    <a href="about.html#solution" class="dropdown-item">Solution</a>
                    <a href="about.html#ourteam" class="dropdown-item">Our Team</a>
                    <a href="about.html#ouradvisors" class="dropdown-item">Our Advisors</a>
                </div>
                </li>
                <li class="nav-item"><a href="apply.html" class="nav-link">Apply</a></li>
                <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" href="#">Projects</a>
                <div class="dropdown-menu">
                    <a href="project.html#cleanup" class="dropdown-item">Beach Clean up Drives</a>
                    <a href="project.html#donation" class="dropdown-item">Donation Drives</a>             
                </div>
                </li>
                <li class="nav-item active"><a href="blog.html" class="nav-link">Blogs</a></li>
                <li class="nav-item"><a href="gallery.html" class="nav-link">Gallery</a></li>
                <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" href="#">Impact</a>
                <div class="dropdown-menu">
                    <a href="https://docs.google.com/presentation/d/1gCgncnPpnOV-lC5f5nNkuuQByAhRXivbv7FKQ_qyV7o/edit?usp=sharing" target="_blank" class="dropdown-item">2019 - 2021</a>
                </div>
                </li>
                <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" href="#">Collaborations</a>
                <div class="dropdown-menu">
                    <a href="partners.html#partners" class="dropdown-item">Our Partners</a>
                    <a href="partners.html#collaborators" class="dropdown-item">Our Collaborators</a>
                </div>
                </li>
                <li class="nav-item"><a href="contact.html" class="nav-link">Contact Us</a></li>
            </ul>
            </div>
        </div>
        </nav>
        <!-- END nav -->
        
        <div class="hero-wrap" style="background-image: url('images/bg_2.jpg');" data-stellar-background-ratio="0.5">
        <div class="overlay"></div>
        <div class="container">
            <div class="row no-gutters slider-text align-items-center justify-content-center" data-scrollax-parent="true">
            <div class="col-md-7 ftco-animate text-center" data-scrollax=" properties: { translateY: '70%' }">
                <p class="breadcrumbs" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }"><span class="mr-2"><a href="index.html">Home</a></span> <span>Blog</span></p>
                <h1 class="mb-3 bread" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }">Blogs</h1>
            </div>
            </div>
        </div>
        </div>

        
        <section class="ftco-section">
        <div class="container">
            <div class="row d-flex" id="blogs-parent">'''+blogs_temp+'''



        </section>

        <footer class="ftco-footer ftco-section img pt-4 pb-2">
        <div class="overlay"></div>
        <div class="container">
            <div class="row mb-1">
            <div class="col-md-4">
                <div class="ftco-footer-widget mb-0">
                <h2 class="ftco-heading-2">About Us</h2>
                <p>
                    Change Is Us is a youth-led initiative working tirelessly to create positive
                    societal and environmental change. Save the planet and spread smiles among the
                    under-privileged. Join us in our endeavour today!
                </p>
                <ul class="ftco-footer-social list-unstyled float-md-left float-lft mt-5">
                    <li class="ftco-animate"><a href="https://instagram.com/change.is.us?utm_medium=copy_link"
                        target="_blank"><span class="icon-instagram"></span></a></li>
                    <li class="ftco-animate"><a href="https://www.linkedin.com/company/change-is-us-11" target="_blank"><span
                        class="icon-linkedin"></span></a></li>
                    <li class="ftco-animate"><a href="https://twitter.com/changeisus11?t=u7ZlHmzLcl-GjDqrc8oQMw&s=08"
                        target="_blank"><span class="icon-twitter"></span></a></li>
                    <li class="ftco-animate"><a href="https://www.facebook.com/Change-Is-Us-113061006834617/"
                        target="_blank"><span class="icon-facebook"></span></a></li>
                </ul>
                </div>
            </div>
            <div class="col-md-3 ml-md-4">
                <div class="ftco-footer-widget mb-4 ml-md-0">
                <h2 class="ftco-heading-2">Site Links</h2>
                <ul class="list-unstyled">
                    <div class="row">
                    <div class="col-6">
                        <li><a href="index.html" target="_blank" class="py-3 d-block">Home</a></li>
                        <li><a href="about.html" target="_blank"" class=" py-3 d-block">About</a></li>
                        <li><a href="apply.html" target="_blank" class="py-3 d-block">Apply</a></li>
                        <li><a href="project.html" target="_blank" class="py-3 d-block">Project</a></li>
                    </div>
                    <div class="col-6">
                        <li><a href="blog.html" target="_blank" class="py-3 d-block">Blogs</a></li>
                        <li><a href="#" target="_blank" class="py-3 d-block">Impact</a></li>
                        <li><a href="partners.html" target="_blank" class="py-3 d-block">Partners</a></li>
                        <li><a href="contact.html" target="_blank" class="py-3 d-block">Contact</a></li>
                    </div>
                    </div>
                </ul>
                </div>
            </div>
            <div class="col-md-4 ml-md-4">
                <div class="ftco-footer-widget mb-4">
                <h2 class="ftco-heading-2">Reach Us</h2>
                <div class="block-23 mb-3">
                    <ul>
                    <li class="py-2"><span class="icon icon-map-marker"></span><span class="text">Girgaum Chowpatty Beach,
                        Beachfront Opposite Cafe Ideal</span></li>
                    <li class="py-2"><span class="icon icon-phone"></span><span class="text">+91 773896986, +91
                        9869843834</span></li>
                    <li class="py-2"><a href="mailto:changeisus.website@gmail.com"><span
                            class="icon icon-envelope"></span><span class="text">changeisus.website@gmail.com</span></a></li>
                    </ul>
                </div>
                </div>
            </div>
            </div>
            <div class="row">
            <div class="col-md-12 text-center">
                <p>
                Copyright &copy;
                <script>document.write(new Date().getFullYear());</script> |
                All rights reserved by <span class="heading"><a href="index.html">Change Is Us</span></a>
                </p>
                <!-- <p> -->
                <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                <!-- Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="icon-heart" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a> -->
                <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                <!-- </p> -->
            </div>
            </div>
        </div>
        </footer>
        
    

    <!-- loader -->
    <div id="ftco-loader" class="show fullscreen"><svg class="circular" width="48px" height="48px"><circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee"/><circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10" stroke="#F96D00"/></svg></div>


    <script src="js/jquery.min.js"></script>
    <script src="js/jquery-migrate-3.0.1.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/jquery.easing.1.3.js"></script>
    <script src="js/jquery.waypoints.min.js"></script>
    <script src="js/jquery.stellar.min.js"></script>
    <script src="js/owl.carousel.min.js"></script>
    <script src="js/jquery.magnific-popup.min.js"></script>
    <script src="js/aos.js"></script>
    <script src="js/jquery.animateNumber.min.js"></script>
    <script src="js/bootstrap-datepicker.js"></script>
    <script src="js/jquery.timepicker.min.js"></script>
    <script src="js/scrollax.min.js"></script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
    <script src="js/google-map.js"></script>
    <script src="js/main.js"></script>
        
    </body>
    </html>
    '''

    with open("blog.html","w+") as f:
        f.write(entire_page)
        f.close()


if __name__=='__main__':
    URL = "https://changeisus11.blogspot.com/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib') 

    first_entry = True
    total_blogs = 0
    number_of_pages = 1
    blogs=[]
    while len(soup.find_all('a', class_='blog-pager-older-link flat-button ripple')) != 0:

        if not first_entry:
            URL = str(soup.find('a', class_='blog-pager-older-link flat-button ripple')['href'])
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            number_of_pages+=1
        first_entry = False
            
        frame = soup.find_all('article', class_='post-outer-container')
        print('====== Extracting ',len(frame),'blogs from page ',number_of_pages,' =======')
        total_blogs+=len(frame)
        for j,i in enumerate(frame):
            blog={}
            title = i.h3.get_text().strip()
            date = i.time.get_text().strip()
            if i.img!=None:
                imageURL = i.img['src']
            else:
                imageURL = DEFAULT_IMG
            hyperlink = i.h3.a['href']
            content = i.find('div',class_='snippet-item r-snippetized').get_text().strip()
            author = DEFAULT_AUTHOR
            blog['id']=j
            blog['title'] = title
            blog['author'] = author
            blog['imageURL'] = imageURL
            blog['hyperlink'] = hyperlink
            blog['content'] = content
            blog['date'] = date
            blogs.append(blog)
            # print(j)
            # print(title)
            # print(date)
            # print(imageURL)
            # print(hyperlink)
            # print(content)
            # print()

    # print(blogs)
    print('_____ Total ',total_blogs,'Blogs extracted _____')
    createFile(blogs)