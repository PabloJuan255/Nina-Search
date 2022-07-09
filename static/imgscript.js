imgs = document.getElementsByTagName('img')

for(i in imgs){
  x = imgs[i]
    for(j in imgs){
        y = imgs[j]
        if(x.id !== y.id && typeof(y == 'object')){
            if(x.src == y.src){
                y.parentElement.remove()
            }
        }
    }
}
// Repeating the script to make sure the results wont
// repeat.
for(i in imgs){
  x = imgs[i]
    for(j in imgs){
        y = imgs[j]
        if(x.id !== y.id && typeof(y == 'object')){
            if(x.src == y.src){
                y.parentElement.remove()
            }
        }
    }
}