
console.log("UPLOAD JS LOADED");

async function uploadFile() {

    const file = document.getElementById("fileInput").files[0];
    const status = document.getElementById("status");

    if (!file) {
        status.innerText = "Please select a CSV file.";
        return;
    }

    try {

        status.innerText = "Uploading file...";

        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log(data);

        if (!response.ok) {
            throw new Error(data.message || "Upload failed");
        }

        status.innerText =
            `Upload Successful: ${data.filename} `;

    } catch (error) {

        console.error(error);

        status.innerText =
            `Upload Failed: ${error.message} `;
    }
}

