const cir=document.querySelectorAll(".cir");
const messages0=document.querySelector(".messages0")
const messages1=document.querySelector(".messages1")
const messages2=document.querySelector(".messages2")
const messages3=document.querySelector(".messages3")
const messages=document.querySelector(".messages")

let details=[
    {
        id:0,
        img:"assests/images/about_3_1.jpg",
        location:"Four Seasons Hotel",
        date:"20 March,2024",
        time:"9:30 - 10:30 AM",
        title:"UI / UX Developer Meet",
        para:"Ensure that the event venue is accessible to all participants, including those with disabilities, and provide features like live captioning or sign language interpretation if possible like presentations, videos"
    },
    {
        id:1,
        img:"assests/images/about_2_1.jpg",
        location:"vnk",
        date:"26 May,2024",
        time:"9952-5522",
        title:"Web Developer",
        para:"Ensure that the event venue is accessible to all participants, including those with disabilities, and provide features like live captioning or sign language interpretation if possible like presentations, videos"
    },
    {
        id:6,
        img:"assests/images/about_2_1.jpg",
        location:"vnk",
        date:"26 May,2024",
        time:"9952-5522",
        title:"software engineer",
        para:"Ensure that the event venue is accessible to all participants, including those with disabilities, and provide features like live captioning or sign language interpretation if possible like presentations, videos"
    },
   
    {
        id:2,
        img:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZDtpLHESPf0qBrMxM7dhBwyms_RI8UBMIjoKKdvXlYw&s",
        location:"vnk",
        date:"20 July,2024",
        time:"9952-5522",
        title:"software engineer",
        para:"Ensure that the event venue is accessible to all participants, including those with disabilities, and provide features like live captioning or sign language interpretation if possible like presentations, videos"
    },
    {
        id:9,
        img:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZDtpLHESPf0qBrMxM7dhBwyms_RI8UBMIjoKKdvXlYw&s",
        location:"vnk",
        date:"20 July,2024",
        time:"9952-5522",
        title:"Python engineer",
        para:"Ensure that the event venue is accessible to all participants, including those with disabilities, and provide features like live captioning or sign language interpretation if possible like presentations, videos"
    },
    
    {
        id:3,
        img:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZDtpLHESPf0qBrMxM7dhBwyms_RI8UBMIjoKKdvXlYw&s",
        location:"vnk",
        date:"15 August,2024",
        time:"9952-5522",
        title:"Java engineer",
        para:"Ensure that the event venue is accessible to all participants, including those with disabilities, and provide features like live captioning or sign language interpretation if possible like presentations, videos"
    },
   
    {
        id:7,
        img:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZDtpLHESPf0qBrMxM7dhBwyms_RI8UBMIjoKKdvXlYw&s",
        location:"vnk",
        date:"15 August,2024",
        time:"9952-5522",
        title:"software engineer",
        para:"Ensure that the event venue is accessible to all participants, including those with disabilities, and provide features like live captioning or sign language interpretation if possible like presentations, videos"
    },
    {
        id:5,
        img:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZDtpLHESPf0qBrMxM7dhBwyms_RI8UBMIjoKKdvXlYw&s",
        location:"vnk",
        date:"20 March,2024",
        time:"9952-5522",
        title:"software engineer",
        para:"Ensure that the event venue is accessible to all participants, including those with disabilities, and provide features like live captioning or sign language interpretation if possible like presentations, videos"
    },
]
let arr=[];
window.addEventListener("load",(emp)=>{
    for(let i=0;i<4;i++){
        if(!arr.includes(i)){
            arr.push(i)
        }
        const result=details.filter((item)=>item.date===cir[i].children[0].innerHTML)
        result.map((item,im)=>{
            append(item.img,item.title,item.location,item.para,item.time,i)
        })
        messages.childNodes.forEach((el,il)=>{
            if(il%2!=0){
                el.style.display="none"
            }
        })
        messages.childNodes[1].style.display="block"
    }
})

cir.forEach((e,im)=>{
    e.addEventListener("click",ee=>{
        cir.forEach((em)=>{
            if(em.classList.contains("active")){
                em.classList.remove("active");
            }
        })
        e.classList.add("active");
        
        if(arr.includes(im)){
            messages.childNodes.forEach((el,il)=>{
                if(il%2!=0){
                    el.style.display="none"
                }
            })
            let curr;
            if(im==0){
                curr=1
            }
            else if(im==1){
                curr=3
            }
            else if(im=2){
                curr=5
            }
            else{
                curr=7
            }
            messages.childNodes[curr].style.display="block"
            
        }
       
       
    })
});
function append(image,title,location,para,time,id) {
    const messageBox=document.createElement("div")
    messageBox.classList.add("message-box")
    messageBox.innerHTML = `
        <div class="mes-image">
            <img src=${image} alt="">
        </div>
        <div class="mes-con">
            <div class="mes-con-top">
                <div class="top-info">
                    <i class="bi bi-geo-alt"></i>
                    <p class="text-muted">${location}</p>
                </div>
                <div class="top-info">
                    <i class="bi bi-clock"></i>
                    <p class="text-muted">${time}</p>
                </div>
            </div>
            <h1>${title}</h1>
            <p class="p text-muted">${para}</p>
            <div class="mes-con-bottom">
                <div class="mes-circle">
                    <div class="mes-b-image">
                        <img src="assests/images/team_1_3.jpg" alt="">
                        <div class="mes-mic">
                            <i class="fa-solid fa-microphone-lines"></i>
                        </div>
                    </div>
                </div>
                <div class="mes-circle">
                    <div class="mes-b-image">
                        <img src="assests/images/team_1_2.jpg" alt="">
                        <div class="mes-mic">
                            <i class="fa-solid fa-microphone-lines"></i>
                        </div>
                    </div>
                </div>
                <div class="mes-circle">
                    <div class="mes-b-image">
                        <img src="assests/images/team_1_4.jpg" alt="">
                        <div class="mes-mic">
                            <i class="fa-solid fa-microphone-lines"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="mes-buttons">
            <button class="b1"><a href="eventdetails.html">VIEW DETAILS</a></button>
            <button class="b2"><a href="tickets.html">Buy Tickets</button>
            
        </div>
    `;
    
    
    messages.children[id].appendChild(messageBox)
    
}