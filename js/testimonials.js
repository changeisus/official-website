var testimonials = [
    {
        "Name":"Mushira Shaikh",
        "age":"23",
        "testimony":"Change is us is a wonderful group of people who have committed to making earth a better place to live in by organising events like beach cleaning drives",
        "imageURL":"mushira_shaikh.jpg",
        "position":"Software Developer, Mumbai"
    },
    {
        "Name":"Arush Agrawal",
        "age":"18",
        "testimony":"Other than being fun, beach cleanups also ignite a sense of empowerment that the magnitude of change entirely depends on the number of individuals actually willing to make a difference.",
        "imageURL":"arush_agrawal.jpg",
        "position":"Student"
    },
    {
        "Name":"Tanisha Bhimonee",
        "age":"17",
        "testimony":"I initiated my social work journey with CIU. It provides me with a great opportunity to socialize and interact with so many new people along with bringing impactful changes to the society around me. Beach Clean-ups are engaging because the people here are so warm and welcoming, it feels like home.",
        "imageURL":"tanisha_bhimonee.jpg",
        "position":"Content Creator"
    },
    {
        "Name":"Gopa Jhaveri",
        "age":"55",
        "testimony":"'Change Is Us' the name says it all.  I feel so proud and satisfied to have volunteered with such young, dedicated and sincere minds-Shubh & Akshat- for a humungous cause for the city & environment.",
        "imageURL":"gopa_jhaveri.jpg",
        "position":"Special Educator"
    },
    {
        "Name":"Sameira Shroff",
        "age":"21",
        "testimony":"Very eye opening experience! I didn’t realise the extent of the problem until I cleaned up with my own hands. It goes so much deeper than we know and it feels great to be able to do my part and give back to the Earth!",
        "imageURL":"sameira_shroff.jpg",
        "position":"Concept Artist"
    },
    {
        "Name":"Rajesh Koppikar",
        "age":"55",
        "testimony":"Exhilarating and uplifting experience. One might say even spiritual. Gives you a sense of being one with nature. Made me aware and encouraged me to take proactive action.",
        "imageURL":"rajesh_koppikar.jpg",
        "position":"Periodontist"
    }
]


function xyz(){
    if ( testimonials.length==0 ) {
        setTimeout("xyz",100)
        return
    }
    var testimonials_parent=document.getElementById("testimonials-parent")
    var temp=""
    for( let testimony of testimonials){
    temp+=`
        <div class="item">
            <div class="cause-entry">
                <div class="testimonial-img-mobile">
                    <a
                    href="#"
                    class="img"
                    style="background-image: url(images/testimonials/${testimony["imageURL"]})"
                    ></a>
                </div>
                <div class="testimonial-img-desktop">
                    <a
                    href="#"
                    class="img"
                    style="background-image: url(images/testimonials/bg.jpg)"
                    ></a>
                    <img class="testimonial-img" src="images/testimonials/${testimony["imageURL"]}" />
                </div>
                <div class="text p-3 p-md-4">
                    <h3><a href="#">${testimony["Name"]}, ${testimony["age"]}</a></h3>
                    <p>
                    ${testimony["testimony"]}
                    </p>
                    <span class="donation-time mb-3 d-block"
                        >${testimony["position"]}</span
                    >
                </div>
            </div>
        </div>

    `
    }
    testimonials_parent.innerHTML=temp;
    }
  xyz()


