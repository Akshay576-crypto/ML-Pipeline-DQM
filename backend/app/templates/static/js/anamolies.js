console.log("ANOMALIES JS LOADED");

async function loadAlerts() {

    try {

        const response = await fetch("/alert");

        const data = await response.json();

        console.log(data);

        document.getElementById("total-alerts").innerText =
            data.total_alerts;

        let high = 0;
        let medium = 0;
        let low = 0;

        const tableBody =
            document.getElementById("alert-table-body");

        tableBody.innerHTML = "";

        data.alerts.forEach((alert, index) => {

            if (alert.severity === "High")
                high++;

            else if (alert.severity === "MEDIUM")
                medium++;

            else
                low++;

            tableBody.innerHTML += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${alert.Type}</td>
                    <td>${alert.message}</td>
                    <td>${alert.severity}</td>
                </tr>
            `;
        });

        document.getElementById("high-risk").innerText =
            high;

        document.getElementById("medium-risk").innerText =
            medium;

        document.getElementById("low-risk").innerText =
            low;

    }

    catch (error) {

        console.error(
            "Alert Load Error:",
            error
        );
    }
}


// Chart

const ctx =
    document.getElementById("anomalyChart");

new Chart(ctx, {

    type: "bar",

    data: {

        labels: [
            "Alerts"
        ],

        datasets: [{

            label: "Detected Alerts",

            data: [1]

        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false
    }

});


document.addEventListener(
    "DOMContentLoaded",
    loadAlerts
);