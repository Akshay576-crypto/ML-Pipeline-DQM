// Load Dashboard Cards
async function loadDashboard() {

    try {

        const response = await fetch("/dashboard-history");

        if (!response.ok) {
            throw new Error("Failed to fetch dashboard data");
        }

        const data = await response.json();
        document.getElementById("quality-score").innerText =
            Number(data.average_quality_score || 0).toFixed(2);

        document.getElementById("anomaly-percentage").innerText =
            data.total_anamolies || 0;

        document.getElementById("total-runs").innerText =
            data.total_runs || 0;
    } catch (error) {

        console.error("Dashboard Error:", error);

        document.getElementById("quality-score").innerText = "Error";
        document.getElementById("anomaly-percentage").innerText = "Error";
        document.getElementById("total-runs").innerText = "Error";
    }
}


// Load Quality Trend Chart
async function loadQualityChart() {

    console.log("Quality chart started");

    const canvas = document.getElementById("qualityChart");

    if (!canvas) {
        console.log("Canvas not found");
        return;
    }

    console.log("Canvas found");

    new Chart(canvas, {
        type: "line",
        data: {
            labels: ["A", "B", "C", "D"],
            datasets: [{
                label: "Test",
                data: [10, 20, 30, 40]
            }]
        }
    });

    console.log("Test chart rendered");
}// Initialize Page
document.addEventListener("DOMContentLoaded", () => {

    console.log("Dashboard Loaded");

    loadDashboard();
    loadQualityChart();

});