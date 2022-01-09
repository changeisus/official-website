import os

	    	# <div class="d-md-flex">

		    # 	<a href="images/cause-3.jpg" class="gallery image-popup d-flex justify-content-center align-items-center img ftco-animate" style="background-image: url(images/cause-3.jpg);">
		    # 		<div class="icon d-flex justify-content-center align-items-center">
		    # 			<span class="icon-search"></span>
		    # 		</div>
		    # 	</a>
		    # 	<a href="images/cause-4.jpg" class="gallery image-popup d-flex justify-content-center align-items-center img ftco-animate" style="background-image: url(images/cause-4.jpg);">
		    # 		<div class="icon d-flex justify-content-center align-items-center">
		    # 			<span class="icon-search"></span>
		    # 		</div>
		    # 	</a>
		    # 	<a href="images/cause-5.jpg" class="gallery image-popup d-flex justify-content-center align-items-center img ftco-animate" style="background-image: url(images/cause-5.jpg);">
		    # 		<div class="icon d-flex justify-content-center align-items-center">
		    # 			<span class="icon-search"></span>
		    # 		</div>
		    # 	</a>
	    	# </div>

temp='<div class="d-md-flex">'
for i,j in enumerate(os.listdir("./images/partners")):
    temp+=(f'''
                <a href="images/partners/{j}" class="gallery image-popup d-flex justify-content-center align-items-center img ftco-animate" style="background-image: url(images/partners/{j});">
                    <div class="icon d-flex justify-content-center align-items-center">
                        <span class="icon-search"></span>
                    </div>
                </a>
                ''')
    if i%4==0 and i!=0:
        temp+="</div>\n"
        temp+='<div class="d-md-flex">\n'
print(temp)

# import os
# for f in os.listdir("./images/partners"):

#     r = f.replace(" ","_")
#     if( r != f):
#         os.chdir(r"C:\Users\Tulip\Desktop\official-website\images\partners")
#         os.rename(f,r)
