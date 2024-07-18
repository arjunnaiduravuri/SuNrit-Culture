const box=document.querySelector(".form-box")
const links=document.querySelectorAll(".p h6 p")

const details=`<form action="" onsubmit="mm()">
<p class="h">Select category</p>
<label for=""></label>
<select class="form-select" id="" name="">
  <option>--Category--</option>
  <option>Business & Seminars</option>
  <option>Sports & Fitness</option>
  <option>Music & Concerts</option>
  <option>Food & Drinks</option>
</select>


<p class="e">Event Name</p>
<label for=""><input type="text" required size="132"></label>


<p class="j">Event URL</p>
<label for=""><input type="text" required size="132"></label>

<p class="j1">Description</p>
<textarea name="text" required id="" rows="10" cols="50">And sir dare view but over man. So at within mr to simple assure. Mr disposing continued it offending arranging in we. Extremity as if breakfast agreement. Off now mistress provided out horrible opinions. Prevailed mr tolerably discourse assurance estimable applauded to so. Him everything melancholy uncommonly but solicitude inhabiting projection off. Connection stimulated estimating excellence an to impression.



Unpleasant astonished an diminution up partiality. 



Noisy an their of meant. Death means up civil do an offer wound of. Called square an in afraid direct. Resolution diminution conviction so mr at unpleasing simplicity no. 



No it as breakfast up conveying earnestly immediate principle.
Him son disposed produced humoured overcame she bachelor improved.
Studied however out wishing but inhabit fortune windows.


At as in understood an remarkably solicitude. 



Mean them very seen she she. Use totally written the observe pressed justice. Instantly cordially far intention recommend estimable yet her his. Ladies stairs enough esteem add fat all enable. Needed its design number winter see. Oh be me sure wise sons no. Piqued ye of am spirit regret. Stimulated discretion impossible admiration in particular conviction up.



Is allowance instantly strangers applauded discourse so. Separate entrance welcomed sensible laughing why one moderate shy. We seeing piqued garden he. As in merry at forth least ye stood. And cold sons yet with. Delivered middleton therefore me at. Attachment companions man way excellence how her pianoforte. </textarea>

<p class="j2">Why to attend Event</p>
<textarea name="text" required id="" rows="10" cols="50" class="t1">Received the likewise law graceful his. Nor might set along charm now equal green. Pleased yet equally correct colonel not one. Say anxious carried compact conduct sex general nay certain. Mrs for recommend exquisite household eagerness preserved now. My improved honoured he am ecstatic quitting greatest formerly.



Dashwood contempt on mr unlocked resolved provided.



Stanhill wondered it it welcomed oh. Hundred no prudent he however smiling at an offence. If earnestly extremity he he propriety something admitting convinced ye. Pleasant in to although as if differed horrible. Mirth his quick its set front enjoy hoped had there. Who connection imprudence middletons too but increasing celebrated principles joy. Herself too improve gay winding ask expense are compact. 



New all paid few hard pure she.



Blind would equal while oh mr do style.
Lain led and fact none.
One preferred sportsmen resolving the happiness continued.
High at of in loud rich true.
Equally welcome her set nothing has gravity whether parties.
Fertile suppose shyness mr up pointed in staying on respect.


Arrived totally in as between private.



Favour of so as on pretty though elinor direct. Reasonable estimating be alteration we themselves entreaties me of reasonably. Direct wished so be expect polite valley. Whose asked stand it sense no spoil to. Prudent you too his conduct feeling limited and. Side he lose paid as hope so face upon be. Goodness did suitable learning put.



Enjoyed minutes related as at on on. Is fanny dried as often me. Goodness as reserved raptures to mistaken steepest oh screened he. Gravity he mr sixteen esteems. Mile home its new way with high told said. Finished no horrible blessing landlord dwelling dissuade if. Rent fond am he in on read. Anxious cordial demands settled entered in do to colonel.</textarea>

<button><i class="bi bi-sd-card-fill"></i> Save</button>

</form>`

const timings=`<form action="">
<div class="row date" style="height: 20vh;">
    <div class="col-12 col-lg-6 d-flex flex-column">
        <p>Start Date</p>
        <label for=""><input type="date" required size="40"></label>
    </div>

    <div class="col-12 col-lg-6 d1">
        <p>Start Time</p>
        <label for=""><input type="time" required size="40"></label>
    </div>
 </div>

 <div class="row end" style="height: 20vh;">
    <div class="col-12 col-lg-6 d-flex flex-column">
        <p>End Date</p>
        <label for=""><input type="date" required size="40"></label>
    </div>

    <div class="col-12 col-lg-6 e1">
        <p>End Time</p>
        <label for=""><input type="time" required size="40"></label>
    </div>
 </div>

 <div class="row start" style="height: 22vh;">
    <p><b>Start 27 Nov 2025 to Till 30 Nov 2025</b></p><hr>
    <h5 class="m"><b>Duration </b> 4 Days | 75:30 Hour</h5>
 </div>

 <button><i class="bi bi-sd-card-fill"></i> Save</button>
</div>

</form>`

const location1=`<div class="form">
<form>
   <div class="form-group">
     <label for="">Venue</label>
     <input type="text" required class="form-control" id="" value="Fremont Street Experience">
   </div>

   <div class="form-group">
     <label for="">Address</label>
     <input type="text" required class="form-control" id="" value="">
   </div>

   <div class="form-group">
       <label for="">City</label>
       <input type="text" required class="form-control" id="" value="Las Vegas">
     </div>

     <div class="form-group">
       <label for="">State</label>
       <input type="text" required class="form-control" id="" value="Nevada">
     </div>

     <div class="form-group">
       <label for="">Zipcode/Pincode</label>
       <input type="text" required class="form-control" id="" value="89102">
     </div>

     <div class="form-group">
       <label for="">Country</label>
       <input type="text"  required class="form-control" id="" value="United States">
     </div>
 
 </div>`

 const media=`<div>
 <div class="thumb">
     <h6>Thumbnail Image</h6>
     <div class="thumb-img">
         <img src="https://www.discoverhongkong.com/content/dam/dhk/intl/what-s-new/events/events-festivals-720x860.jpg" alt="">
     </div>
     <p>Upload 16:9 ratio thumbnail image of atleast 1280x720 px (jpg/jpeg/png)</p>
 </div>
 <div class="post">
     <h6>Post Image</h6>
     <div class="post-img">
         <img src="https://www.discoverhongkong.com/content/dam/dhk/intl/what-s-new/events/events-festivals-720x860.jpg" alt="">
     </div>
     <p>Upload 16:9 ratio poster image of atleast 1280x720 px (jpg/jpeg/png)</p>
     <label>Images Gallery</label><br>
     <input class="in" type="file" id="Upload" accept="image/*" multiple>
     <p>Upload images related to your Event</p>
     <div class="images">
         <div class="pic">
             <img src="https://www.discoverhongkong.com/content/dam/dhk/intl/what-s-new/events/events-festivals-720x860.jpg" alt="">
             <button class="x">x</button>
         </div>
         <div class="pic">
             <img src="https://www.discoverhongkong.com/content/dam/dhk/intl/what-s-new/events/events-festivals-720x860.jpg" alt="">
             <button class="x">x</button>
         </div>
     </div>
 </div>
</div>`
 const seo=`<div class="form">
 <form>
    <div class="form-group">
      <label for="">Meta title</label>
      <input type="text" class="form-control" id="" value="Expresso Food Fare">
    </div>

    <div class="form-group">
      <label for="">Meta tags</label>
      <input type="text" class="form-control" id="" value="Expresso food fare,eventmie">
    </div>

    <div class="form-group">
        <label for="">Meta description</label>
        <input type="text" class="form-control" id="" value="And sir dare view but over man. So at within mr to simple assure. Mr disposing continued it offending arranging in we. Extremity as if breakfast agreement. Off now mistress provided out horrible opinions. Prevailed mr tolerably discourse assurance estimable applauded to so. Him everything melancholy uncommonly but solicitude inhabiting projection off. Connection stimulated estimating excellence an to impression.">
      </div>

      <button><i class="bi bi-sd-card-fill"></i> Save</button>
      </form>

</div>`

const publish=`<div class="row start1" style="height: 50vh;">
<p>Publish Event</p>
<h6>Once you complete all the required steps, your event becomes eligible for Publish</h6>
<hr>
<h5 class="m">Un-Publish Event</h5>
<h6 class="m1">You can Un-publish event anytime, Un-published events are not visible on the website nor they can be shown with Event URL</h6>
<button><i class="bi bi-eye-slash-fill"></i> Un-Publish Event</button>
</div>`

const data=[
    {
        name:details
    },
    {
        name:timings
    },
    {
        name:location1
    },
    {
        name:media
    },
    {
        name:seo
    },
    {
        name:publish
    }
]
const he=document.querySelectorAll(".he")
links.forEach((e,i)=>{
    e.addEventListener("click",(ee)=>{
        box.innerHTML=data[i].name
        he.forEach((x,i1)=>{
            if(x.classList.contains("active")){
                x.classList.remove("active")
            }
            if(i==i1){
                x.classList.add("active")
            }
        })
    })
})