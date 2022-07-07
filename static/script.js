h1s = document.getElementsByTagName('h1')

for(i in h1s){
    for(j in h1s){
        if(h1s[i].id !== h1s[j].id && typeof(h1s[j] == 'object')){
            if(h1s[i].textContent == h1s[j].textContent){
                h1s[j].parentElement.remove()
            }
        }
    }
}
// Repeating the script to make sure the results wont
// repeat.
for(i in h1s){
    for(j in h1s){
        if(h1s[i].id !== h1s[j].id && typeof(h1s[j] == 'object')){
            if(h1s[i].textContent == h1s[j].textContent){
                h1s[j].parentElement.remove()
            }
        }
    }
}