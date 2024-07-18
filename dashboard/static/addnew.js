const box=document.querySelectorAll(".form-box")
const links=document.querySelectorAll(".p h6 i")
const links2=document.querySelectorAll(".p h6 ")






function nextc(id){
    console.log("clicked")
    if(box[id+1].classList.contains("dis")){
        box[id].style.display="none"
        box[id+1].classList.remove("dis")
    }
    links[id].classList.remove("bi-exclamation-circle-fill")
    links[id].classList.add("bi-check-circle-fill")
    links2[id].classList.add("p0")
    // document.querySelector(".bi-check-circle-fill").style.color='green'
}
