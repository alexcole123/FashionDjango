
setInterval(() => {
    const aboutHeader = document.getElementById("aboutHeader");
    if(aboutHeader){
        aboutHeader.style.color = "#" + Math.floor(Math.random() *16777215).toString(16);
    }

}, 3000);

function confirmDelete(event) {
    const ok = confirm("Are you sure?");
    if (!ok) event.preventDefault();
}

const messagesDiv = document.querySelector(".messages");
if(messagesDiv) {
    setTimeout(() => {
        messagesDiv.parentNode.removeChild(messagesDiv);
    }, 3000);
}


// --------------------------------

async function showClothingList() {
    const url = "http://127.0.0.1:8000/api/cloths";
    const cloths = await getJson(url)
    console.log(cloths)
    let html = `
        <table class="table table-hover table-bordered">
            <thead>
                <tr>
                    <th>Manufacturer</th>
                    <th>Price</th>
                    <th>Type</th>
                </tr>
            </thead>
            <tbody> 
    `;
    for(const c of cloths){
        html += `
            <tr>
                <td>${c.manufacturer}</td>
                <td>${c.price}</td>
                <td>${c.type}</td>
            </tr>
        `;
    }
    html += `
            </tbody>
        </table>
    `;
    const containerDiv = document.getElementById("containerDiv");
    containerDiv.innerHTML = html;
}

async function getJson(url){
    const response = await fetch(url);
    const json = await response.json();
    return json

}