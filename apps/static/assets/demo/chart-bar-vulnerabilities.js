getData();
async function getData() {
  const response = await fetch(
    "http://localhost:5000/api/historico/crm4telcoosp/crm4telco-application-java"
  );
  const data = await response.json();
  console.log(data);
  labels = data.data;
  values = data.vulnerabilities;

  new Chart(document.getElementById("vulnerabilitiesBarChart"), {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: "Vulnerabilities",
        backgroundColor: "rgba(2,117,216,1)",
        borderColor: "rgba(2,117,216,1)",
        data: values,
      }],
    },
    options: {
      legend: { display: false },
      title: {
        display: false,
        text: "Proyectos",
      },
    }
  });
}