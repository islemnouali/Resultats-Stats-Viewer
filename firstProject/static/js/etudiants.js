function toggleTable() {
  var container = document.getElementById("tableContainer");
  var btn = document.querySelector(".expand-btn");
  if (container.classList.contains("expanded")) {
    container.classList.remove("expanded");
    btn.textContent = "Afficher tout";
  } else {
    container.classList.add("expanded");
    btn.textContent = "Réduire";
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const dataElement = document.getElementById("stats-data");
  if (dataElement) {
    const statsData = JSON.parse(dataElement.textContent);
    const admisCount = Number(statsData.admisCount || 0);
    const totalCount = Number(statsData.totalCount || 0);
    const Contrôle = totalCount - admisCount;

    const chartElem = document.getElementById("admisPieChart");
    if (chartElem && typeof Chart !== "undefined") {
      const ctx = chartElem.getContext("2d");
      new Chart(ctx, {
        type: "pie",
        data: {
          labels: ["Admis", "Contrôle"],
          datasets: [
            {
              data: [admisCount, Contrôle],
              backgroundColor: ["#00CFFF", "#E6F7FB"],
            },
          ],
        },
      });
    }
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const dataElement = document.getElementById("stats-data");
  if (dataElement) {
    const statsData = JSON.parse(dataElement.textContent);
    const valideCount = Number(statsData.valideCount || 0);
    const totalCount = Number(statsData.totalCount || 0);
    const nonValide = totalCount - valideCount;

    const chartElem = document.getElementById("sem1PieChart");
    if (chartElem && typeof Chart !== "undefined") {
      const ctx = chartElem.getContext("2d");
      new Chart(ctx, {
        type: "pie",
        data: {
          labels: ["Validé", "Non Validé"],
          datasets: [
            {
              data: [valideCount, nonValide],
              backgroundColor: ["#00CFFF", "#E6F7FB"],
            },
          ],
        },
      });
    }
  }
});


document.addEventListener("DOMContentLoaded", function () {
  const dataElement = document.getElementById("stats-data");
  if (dataElement) {
    const statsData = JSON.parse(dataElement.textContent);
    const valideCount = Number(statsData.valideCount || 0);
    const totalCount = Number(statsData.totalCount || 0);
    const nonValide = totalCount - valideCount;

    const chartElem = document.getElementById("sem2PieChart");
    if (chartElem && typeof Chart !== "undefined") {
      const ctx = chartElem.getContext("2d");
      new Chart(ctx, {
        type: "pie",
        data: {
          labels: ["Validé", "Non Validé"],
          datasets: [
            {
              data: [valideCount, nonValide],
              backgroundColor: ["#00CFFF", "#E6F7FB"],
            },
          ],
        },
      });
    }
  }
});