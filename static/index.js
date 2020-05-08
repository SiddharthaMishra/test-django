// window.onload = () => {
//     console.log("hello world");

//     // bind functions that make ajax requests to all the buttons
//     createModelButtons();

// };

// function createModel(pk) {
//     const inputField = document.getElementById("model-input-"+ pk);

//     const opts = {
//         method: "POST",
//         headers: {
//             'Accept': 'application/json, text/plain, */*',
//             "Content-Type": "application/json",

//         },
//         body: JSON.stringify({
//             name: inputField.value,
//             manufacturer: pk,
//         })
//     };
//     fetch("/api/models/", opts)
//         .then((res) => res.json())
//         .then((res) => console.log(res));
    
//     inputField.value = "";
// }

// function createModelButtons() {
//     const buttons = document.getElementsByClassName("add-model");

//     console.log(buttons);
//     for (let button of buttons) {
//         button.onclick = () => createModel(button.dataset.pk);
//     }
// }


function deleteObject(endpoint) {
    const opts = {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    };
    fetch(endpoint, opts)
        .then((res) => window.location.reload())

}