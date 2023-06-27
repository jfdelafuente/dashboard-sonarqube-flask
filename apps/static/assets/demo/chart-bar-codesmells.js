getData();
async function getData() {
  const response = await fetch(
      "http://localhost:5000/api/historico/crm4telcoosp/crm4telco-application-java"
    );
    const data = await response.json();
    console.log(data);
    labels = data.data;
    values = data.codesmells;

  new Chart(document.getElementById("codesmellsBarChart"), {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: "Revenue",
        backgroundColor: "rgba(2,117,216,1)",
        borderColor: "rgba(2,117,216,1)",
        data: values,
      }],
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: "Proyectos",
      },
    }
  });
}