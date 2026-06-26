console.log("REPORT JS LOADED");

async function loadReport() {

    try {

        const response = await fetch("/analytics-report");

        const data = await response.json();

        console.log("Report Data:", data);

        // ---------------------------
        // Update Cards
        // ---------------------------
        document.getElementById("quality-score").innerText =
            data.quality_score;

        document.getElementById("anomaly-count").innerText =
            data.anomaly_count;

        document.getElementById("total-records").innerText =
            data.total_records;

        document.getElementById("quality-status").innerText =
            data.quality_status;

        // ---------------------------
        // Table
        // ---------------------------
        const tableBody = document.getElementById("report-table-body");
        tableBody.innerHTML = "";

        data.history.forEach(item => {

            const row = `
        <tr>
            <td>${item.month}</td>
            <td>${item.score}</td>
            <td>${data.quality_score}</td>
            <td>${data.anomaly_count}</td>
        </tr>
    `;

            tableBody.innerHTML += row;
        });

        // ---------------------------
        // Chart
        // ---------------------------
        const ctx = document.getElementById("qualityChart");

        if (window.myChart) {
            window.myChart.destroy();
        }

        window.myChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: data.history.map(x => x.month),
                datasets: [{
                    label: "Quality Score",
                    data: data.history.map(x => x.score),
                    borderWidth: 2,
                    fill: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });

    } catch (error) {
        console.error("Report Error:", error);
    }
}


// ---------------------------
// Download PDF
// ---------------------------
function setupDownload() {

    const btn = document.getElementById("download-report-btn");

    btn.addEventListener("click", () => {

        if (!currentFileName) {

            alert("No report available");
            return;
        }

        window.location.href =
            `/download-report/${currentFileName}_report.pdf`;

    });
}
// INIT
document.addEventListener("DOMContentLoaded", () => {
    loadReport();
    setupDownload();
});