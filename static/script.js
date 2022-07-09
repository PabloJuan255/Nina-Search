//anim
divs = document.getElementsByTagName('div')
for(div in divs){
  div = divs[div]
  if(typeof(divs[div]) == 'object'){
    console.log(div)
    div.onmouseenter = function(){
      div.classList.toggle("diffborder");
    }
    div.onmouseleaves = function(){
      div.classList.toggle("diffborder");
    }
  }
}

//dont repeat results script
h2s = document.getElementsByTagName('h2')

for(i in h2s){
    x = h2s[i]
    for(j in h2s){
        y = h2s[j]
        if(x.id !== y.id && typeof(y == 'object')){
            if(x.textContent == y.textContent){
                y.parentElement.remove()
            }
        }
    }
}
// Repeating the script to make sure the results wont
// repeat.
for(i in h2s){
    x = h2s[i]
    for(j in h2s){
        y = h2s[j]
        if(x.id !== y.id && typeof(y == 'object')){
            if(x.textContent == y.textContent){
                y.parentElement.remove()
            }
        }
    }
}