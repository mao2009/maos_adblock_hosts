
document.getElementById("hosts-container").onclick = () => {
    document.execCommand("copy");
}

const inputURL = document.getElementById("input-url")

inputURL.oninput =() =>{
    const match = inputURL.value.match(/http.*?:\/\/(.+?)[\/\n]/)
    if(match){
        document.getElementById("output-domain").innerHTML = match[1]
    }
}

document.getElementById("copy-domain").onclick = ()=>{
    document.getElementById("output-domain").select()
    document.execCommand("copy")
}
